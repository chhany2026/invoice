from . import db
from datetime import datetime
import uuid

class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    warranties = db.relationship('Warranty', back_populates='customer', lazy=True, cascade='all, delete-orphan')
    invoices = db.relationship('Invoice', back_populates='customer', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(255), nullable=False, index=True)
    model = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.Text)
    manufacturer = db.Column(db.String(255))
    
    # Pricing information
    base_price = db.Column(db.Float)
    sale_price = db.Column(db.Float)
    cost_price = db.Column(db.Float)
    currency = db.Column(db.String(10), default='USD')
    
    # Inventory
    stock_quantity = db.Column(db.Integer, default=0)
    min_stock_level = db.Column(db.Integer, default=0)
    sku = db.Column(db.String(100), unique=True)
    
    # Warranty defaults
    default_warranty_months = db.Column(db.Integer, default=12)
    
    # Status
    is_active = db.Column(db.Boolean, default=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    warranties = db.relationship('Warranty', back_populates='product', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'category': self.category,
            'description': self.description,
            'manufacturer': self.manufacturer,
            'base_price': self.base_price,
            'sale_price': self.sale_price,
            'cost_price': self.cost_price,
            'currency': self.currency,
            'stock_quantity': self.stock_quantity,
            'min_stock_level': self.min_stock_level,
            'sku': self.sku,
            'default_warranty_months': self.default_warranty_months,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }


class Warranty(db.Model):
    __tablename__ = 'warranties'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    serial_number = db.Column(db.String(255), unique=True, nullable=False, index=True)
    qr_code = db.Column(db.String(500), unique=True, index=True)
    product_id = db.Column(db.String(36), db.ForeignKey('products.id'), nullable=False)
    customer_id = db.Column(db.String(36), db.ForeignKey('customers.id'), nullable=False)
    
    # Proper relationships (backrefs are defined in Product and Customer models)
    product = db.relationship('Product', back_populates='warranties')
    customer = db.relationship('Customer', back_populates='warranties')
    invoice_items = db.relationship('InvoiceLineItem', back_populates='warranty')
    
    purchase_date = db.Column(db.DateTime, nullable=False)
    warranty_start_date = db.Column(db.DateTime, nullable=False)
    warranty_end_date = db.Column(db.DateTime, nullable=False)
    warranty_duration_months = db.Column(db.Integer, nullable=False)
    
    purchase_location = db.Column(db.String(255))
    purchase_price = db.Column(db.Float)
    currency = db.Column(db.String(10), default='USD')
    
    status = db.Column(db.String(50), default='active', index=True)  # active, expired, claimed, transferred
    notes = db.Column(db.Text)
    
    qr_code_image = db.Column(db.LargeBinary)  # Store QR code as image
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'serial_number': self.serial_number,
            'qr_code': self.qr_code,
            'product_id': self.product_id,
            'customer_id': self.customer_id,
            'product': self.product.to_dict() if self.product else None,
            'customer': self.customer.to_dict() if self.customer else None,
            'purchase_date': self.purchase_date.isoformat(),
            'warranty_start_date': self.warranty_start_date.isoformat(),
            'warranty_end_date': self.warranty_end_date.isoformat(),
            'warranty_duration_months': self.warranty_duration_months,
            'purchase_location': self.purchase_location,
            'purchase_price': self.purchase_price,
            'currency': self.currency,
            'status': self.status,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
