from flask import Blueprint, request, jsonify
from . import db
from .models import Warranty, Product, Customer
from datetime import datetime, timedelta
import qrcode
from io import BytesIO
import uuid

# Create blueprints
warranty_bp = Blueprint('warranty', __name__, url_prefix='/api/warranty')
product_bp = Blueprint('product', __name__, url_prefix='/api/product')
customer_bp = Blueprint('customer', __name__, url_prefix='/api/customer')
qr_bp = Blueprint('qr', __name__, url_prefix='/api/qr')


# ==================== WARRANTY ROUTES ====================
@warranty_bp.route('', methods=['POST'])
def create_warranty():
    """Create a new warranty record"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['serial_number', 'product_id', 'customer_id', 
                          'purchase_date', 'warranty_duration_months']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Check if serial number already exists
        if Warranty.query.filter_by(serial_number=data['serial_number']).first():
            return jsonify({'error': 'Serial number already registered'}), 409
        
        # Parse dates
        purchase_date = datetime.fromisoformat(data['purchase_date'])
        warranty_start = purchase_date
        warranty_end = warranty_start + timedelta(days=30 * data['warranty_duration_months'])
        
        # Create warranty record
        warranty = Warranty(
            serial_number=data['serial_number'],
            qr_code=data.get('qr_code', str(uuid.uuid4())),
            product_id=data['product_id'],
            customer_id=data['customer_id'],
            purchase_date=purchase_date,
            warranty_start_date=warranty_start,
            warranty_end_date=warranty_end,
            warranty_duration_months=data['warranty_duration_months'],
            purchase_location=data.get('purchase_location'),
            purchase_price=data.get('purchase_price'),
            currency=data.get('currency', 'USD'),
            status='active',
            notes=data.get('notes')
        )
        
        db.session.add(warranty)
        db.session.commit()
        
        return jsonify({
            'message': 'Warranty created successfully',
            'warranty': warranty.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@warranty_bp.route('/<warranty_id>', methods=['GET'])
def get_warranty(warranty_id):
    """Get warranty details by ID"""
    warranty = Warranty.query.get(warranty_id)
    if not warranty:
        return jsonify({'error': 'Warranty not found'}), 404
    return jsonify(warranty.to_dict()), 200


@warranty_bp.route('/serial/<serial_number>', methods=['GET'])
def get_warranty_by_serial(serial_number):
    """Get warranty details by serial number"""
    warranty = Warranty.query.filter_by(serial_number=serial_number).first()
    if not warranty:
        return jsonify({'error': 'Warranty not found'}), 404
    return jsonify(warranty.to_dict()), 200


@warranty_bp.route('/<warranty_id>', methods=['PUT'])
def update_warranty(warranty_id):
    """Update warranty record"""
    try:
        warranty = Warranty.query.get(warranty_id)
        if not warranty:
            return jsonify({'error': 'Warranty not found'}), 404
        
        data = request.get_json()
        
        # Update fields if provided
        for field in ['purchase_location', 'purchase_price', 'status', 'notes']:
            if field in data:
                setattr(warranty, field, data[field])
        
        db.session.commit()
        return jsonify({
            'message': 'Warranty updated successfully',
            'warranty': warranty.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@warranty_bp.route('/search', methods=['GET'])
def search_warranties():
    """Search warranties by customer, product, or status"""
    try:
        customer_id = request.args.get('customer_id')
        product_id = request.args.get('product_id')
        status = request.args.get('status')
        
        query = Warranty.query
        
        if customer_id:
            query = query.filter_by(customer_id=customer_id)
        if product_id:
            query = query.filter_by(product_id=product_id)
        if status:
            query = query.filter_by(status=status)
        
        warranties = query.all()
        return jsonify([w.to_dict() for w in warranties]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== PRODUCT ROUTES ====================
@product_bp.route('', methods=['POST'])
def create_product():
    """Create a new product"""
    try:
        data = request.get_json()
        
        if 'name' not in data or 'model' not in data:
            return jsonify({'error': 'Missing required fields: name, model'}), 400
        
        # Check if SKU already exists
        if data.get('sku') and Product.query.filter_by(sku=data['sku']).first():
            return jsonify({'error': 'SKU already exists'}), 409
        
        product = Product(
            name=data['name'],
            model=data['model'],
            category=data.get('category'),
            description=data.get('description'),
            manufacturer=data.get('manufacturer'),
            base_price=data.get('base_price'),
            sale_price=data.get('sale_price'),
            cost_price=data.get('cost_price'),
            currency=data.get('currency', 'USD'),
            stock_quantity=data.get('stock_quantity', 0),
            min_stock_level=data.get('min_stock_level', 0),
            sku=data.get('sku'),
            default_warranty_months=data.get('default_warranty_months', 12),
            is_active=data.get('is_active', True)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify({
            'message': 'Product created successfully',
            'product': product.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@product_bp.route('', methods=['GET'])
def list_products():
    """List all products"""
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products]), 200


@product_bp.route('/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        data = request.get_json()
        
        # Check SKU uniqueness if being updated
        if data.get('sku') and data['sku'] != product.sku:
            existing = Product.query.filter_by(sku=data['sku']).first()
            if existing and existing.id != product_id:
                return jsonify({'error': 'SKU already exists'}), 409
        
        # Update fields
        updatable_fields = [
            'name', 'model', 'category', 'description', 'manufacturer',
            'base_price', 'sale_price', 'cost_price', 'currency',
            'stock_quantity', 'min_stock_level', 'sku', 'default_warranty_months', 'is_active'
        ]
        
        for field in updatable_fields:
            if field in data:
                setattr(product, field, data[field])
        
        db.session.commit()
        
        return jsonify({
            'message': 'Product updated successfully',
            'product': product.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@product_bp.route('/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product"""
    try:
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        # Check if product has warranties
        if product.warranties:
            return jsonify({'error': 'Cannot delete product with active warranties'}), 400
        
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({'message': 'Product deleted successfully'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@product_bp.route('/search', methods=['GET'])
def search_products():
    """Search products by name, model, serial code, or category"""
    try:
        query_string = request.args.get('q', '').strip()
        category = request.args.get('category', '')
        
        if not query_string and not category:
            return jsonify({'error': 'Please provide search query or category'}), 400
        
        query = Product.query
        
        if query_string:
            # Search in name, model, manufacturer, description
            search_filter = f"%{query_string}%"
            query = query.filter(
                db.or_(
                    Product.name.ilike(search_filter),
                    Product.model.ilike(search_filter),
                    Product.manufacturer.ilike(search_filter),
                    Product.description.ilike(search_filter)
                )
            )
        
        if category:
            query = query.filter_by(category=category)
        
        products = query.all()
        
        # Enrich with warranty info
        results = []
        for product in products:
            product_dict = product.to_dict()
            # Get related warranties
            warranties = Warranty.query.filter_by(product_id=product.id).all()
            product_dict['total_sold'] = len(warranties)
            product_dict['active_warranties'] = len([w for w in warranties if w.status == 'active'])
            results.append(product_dict)
        
        return jsonify({
            'count': len(results),
            'products': results
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ==================== CUSTOMER ROUTES ====================
@customer_bp.route('', methods=['POST'])
def create_customer():
    """Create a new customer"""
    try:
        data = request.get_json()
        
        if 'name' not in data:
            return jsonify({'error': 'Missing required field: name'}), 400
        
        # Check if email already exists
        if data.get('email') and Customer.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already exists'}), 409
        
        customer = Customer(
            name=data['name'],
            email=data.get('email'),
            phone=data.get('phone'),
            address=data.get('address'),
            city=data.get('city'),
            country=data.get('country')
        )
        
        db.session.add(customer)
        db.session.commit()
        
        return jsonify({
            'message': 'Customer created successfully',
            'customer': customer.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@customer_bp.route('', methods=['GET'])
def list_customers():
    """List all customers"""
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers]), 200


@customer_bp.route('/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get customer details with their warranties"""
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    customer_data = customer.to_dict()
    customer_data['warranties'] = [w.to_dict() for w in customer.warranties]
    return jsonify(customer_data), 200


# ==================== QR CODE ROUTES ====================
@qr_bp.route('/generate', methods=['POST'])
def generate_qr():
    """Generate QR code for warranty"""
    try:
        data = request.get_json()
        
        if 'serial_number' not in data:
            return jsonify({'error': 'Missing required field: serial_number'}), 400
        
        # Create QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data['serial_number'])
        qr.make(fit=True)
        
        # Convert to image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to bytes
        img_bytes = BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        return {
            'qr_code': img_bytes.getvalue().hex(),
            'serial_number': data['serial_number']
        }, 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
