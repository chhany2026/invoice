"""
Invoice & Receipt API Routes
Handles invoice creation, payments, receipt generation, and reporting
"""

from flask import Blueprint, request, jsonify, send_file, render_template_string
from datetime import datetime, timedelta, timezone
from decimal import Decimal
import uuid
import io

# Helper function to parse ISO format strings with 'Z' suffix
def parse_iso_datetime(date_string):
    """Parse ISO format datetime string, handling 'Z' suffix for UTC"""
    if not date_string:
        return None
    # Replace 'Z' with '+00:00' for proper ISO format parsing
    if isinstance(date_string, str):
        date_string = date_string.replace('Z', '+00:00')
    dt = datetime.fromisoformat(date_string)
    # Remove timezone info to work with naive datetime (SQLite compatible)
    if dt.tzinfo is not None:
        dt = dt.replace(tzinfo=None)
    return dt
import base64
import json

from . import db
from .models import Customer, Product, Warranty
from .models_invoice import Invoice, InvoiceLineItem, Receipt, Payment, CompanySettings
from .utils import generate_qr_code, get_pagination_params

invoice_bp = Blueprint('invoice', __name__, url_prefix='/api/invoice')


# ============================================================================
# INVOICE MANAGEMENT ENDPOINTS
# ============================================================================

@invoice_bp.route('', methods=['POST'])
def create_invoice():
    """
    Create a new invoice with line items
    Auto-creates warranties from line items with warranty info
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('customer_id') or not data.get('line_items'):
            return jsonify({'error': 'Missing required fields: customer_id, line_items'}), 400
        
        # Get customer
        customer = Customer.query.get(data['customer_id'])
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        
        # Create invoice
        invoice = Invoice(
            invoice_number=generate_invoice_number(),
            invoice_date=parse_iso_datetime(data.get('invoice_date')) or datetime.utcnow(),
            due_date=parse_iso_datetime(data.get('due_date')),
            customer_id=data['customer_id'],
            billing_address=data.get('billing_address'),
            shipping_address=data.get('shipping_address'),
            currency=data.get('currency', 'USD'),
            language=data.get('language', 'en'),
            timezone=data.get('timezone', 'UTC'),
            tax_rate=Decimal(data.get('tax_rate', 0)),
            notes=data.get('notes'),
            terms_and_conditions=data.get('terms_and_conditions'),
            invoice_status='draft'
        )
        
        # Process line items
        subtotal = Decimal(0)
        tax_total = Decimal(0)
        
        for item_data in data['line_items']:
            product = Product.query.get(item_data.get('product_id'))
            
            unit_price = Decimal(str(item_data['unit_price']))
            quantity = int(item_data['quantity'])
            discount = Decimal(str(item_data.get('discount', 0)))
            tax_rate = Decimal(str(item_data.get('tax_rate', invoice.tax_rate)))
            
            # Calculate line total
            line_subtotal = (unit_price * quantity) - discount
            line_tax = line_subtotal * (tax_rate / 100)
            line_total = line_subtotal + line_tax
            
            # Create line item
            line_item = InvoiceLineItem(
                invoice_id=invoice.id,
                product_id=item_data.get('product_id'),
                description=item_data.get('description') or (product.name if product else 'Item'),
                quantity=quantity,
                unit_price=unit_price,
                discount=discount,
                tax_rate=tax_rate,
                line_total=line_total,
                warranty_duration_months=item_data.get('warranty_duration_months'),
                serial_number=item_data.get('serial_number')
            )
            
            invoice.line_items.append(line_item)
            subtotal += line_subtotal
            tax_total += line_tax
        
        # Calculate totals
        invoice.subtotal = subtotal
        # Use manual tax_amount if provided, otherwise use calculated tax
        invoice.tax_amount = Decimal(str(data.get('tax_amount', tax_total)))
        invoice.discount_amount = Decimal(str(data.get('discount_amount', 0)))
        invoice.shipping_cost = Decimal(str(data.get('shipping_cost', 0)))
        invoice.grand_total = subtotal + invoice.tax_amount + invoice.shipping_cost - invoice.discount_amount
        
        db.session.add(invoice)
        db.session.flush()
        
        # Create warranties for items with warranty info
        for line_item in invoice.line_items:
            if line_item.warranty_duration_months and line_item.product_id:
                warranty_start = invoice.invoice_date
                # Calculate warranty end date (start + duration in months)
                warranty_end = warranty_start + timedelta(days=30 * line_item.warranty_duration_months)
                
                warranty = Warranty(
                    serial_number=line_item.serial_number or f'SN-{invoice.invoice_number}',
                    product_id=line_item.product_id,
                    customer_id=data['customer_id'],
                    purchase_date=invoice.invoice_date,
                    warranty_start_date=warranty_start,
                    warranty_end_date=warranty_end,
                    warranty_duration_months=line_item.warranty_duration_months,
                    purchase_location=f'{customer.city}, {customer.country}',
                    purchase_price=float(line_item.line_total),
                    currency=invoice.currency,
                    status='active',
                    notes=f'Linked to Invoice {invoice.invoice_number}'
                )
                db.session.add(warranty)
                line_item.warranty_id = warranty.id
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Invoice {invoice.invoice_number} created successfully',
            'invoice_id': invoice.id,
            'invoice_number': invoice.invoice_number,
            'grand_total': float(invoice.grand_total),
            'status': invoice.invoice_status,
            'warranties_created': len([li for li in invoice.line_items if li.warranty_id])
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    """Get invoice details by ID"""
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({'error': 'Invoice not found'}), 404
    
    return jsonify(invoice.to_dict()), 200


@invoice_bp.route('/number/<invoice_number>', methods=['GET'])
def get_invoice_by_number(invoice_number):
    """Get invoice by invoice number"""
    invoice = Invoice.query.filter_by(invoice_number=invoice_number).first()
    if not invoice:
        return jsonify({'error': 'Invoice not found'}), 404
    
    return jsonify(invoice.to_dict()), 200


@invoice_bp.route('', methods=['GET'])
def list_invoices():
    """
    List invoices with filters
    Query params: customer_id, status, from_date, to_date, page, per_page
    """
    try:
        # Get filters
        customer_id = request.args.get('customer_id')
        status = request.args.get('status')
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        payment_status = request.args.get('payment_status')
        
        # Build query
        query = Invoice.query
        
        if customer_id:
            query = query.filter_by(customer_id=customer_id)
        if status:
            query = query.filter_by(invoice_status=status)
        if payment_status:
            query = query.filter_by(payment_status=payment_status)
        
        if from_date:
            query = query.filter(Invoice.invoice_date >= parse_iso_datetime(from_date))
        if to_date:
            query = query.filter(Invoice.invoice_date <= parse_iso_datetime(to_date))
        
        # Pagination
        page, per_page = get_pagination_params()
        paginated = query.order_by(Invoice.invoice_date.desc()).paginate(page=page, per_page=per_page)
        
        return jsonify({
            'data': [inv.to_dict() for inv in paginated.items],
            'total': paginated.total,
            'pages': paginated.pages,
            'current_page': page
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    """Update invoice details"""
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        data = request.get_json()
        
        # Updateable fields
        if 'notes' in data:
            invoice.notes = data['notes']
        if 'internal_notes' in data:
            invoice.internal_notes = data['internal_notes']
        if 'billing_address' in data:
            invoice.billing_address = data['billing_address']
        if 'shipping_address' in data:
            invoice.shipping_address = data['shipping_address']
        
        invoice.modified_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Invoice updated',
            'invoice': invoice.to_dict()
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>/issue', methods=['POST'])
def issue_invoice(invoice_id):
    """
    Issue (finalize) an invoice
    Prevents further edits and marks as sent
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        if invoice.invoice_status != 'draft':
            return jsonify({'error': 'Only draft invoices can be issued'}), 400
        
        invoice.invoice_status = 'issued'
        invoice.modified_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Invoice {invoice.invoice_number} issued',
            'status': invoice.invoice_status,
            'invoice_url': f'/invoice/{invoice.id}'
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>/cancel', methods=['POST'])
def cancel_invoice(invoice_id):
    """Cancel an invoice"""
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        if invoice.payment_status == 'paid':
            return jsonify({'error': 'Cannot cancel paid invoices'}), 400
        
        invoice.invoice_status = 'cancelled'
        invoice.modified_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Invoice cancelled'
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# PAYMENT ENDPOINTS
# ============================================================================

@invoice_bp.route('/<invoice_id>/payment', methods=['POST'])
def record_payment(invoice_id):
    """
    Record a payment for an invoice
    Supports partial payments
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        data = request.get_json()
        amount = Decimal(str(data['amount']))
        
        # Validate payment amount
        outstanding = invoice.grand_total - (invoice.amount_paid or 0)
        if amount > outstanding:
            return jsonify({'error': f'Payment exceeds outstanding balance (${float(outstanding)})'}), 400
        
        # Create payment record
        payment = Payment(
            invoice_id=invoice_id,
            amount=amount,
            payment_date=parse_iso_datetime(data.get('payment_date')) or datetime.utcnow(),
            payment_method=data.get('payment_method', 'cash'),
            gateway=data.get('gateway'),
            transaction_id=data.get('transaction_id'),
            reference_number=data.get('reference_number'),
            status='completed',
            notes=data.get('notes')
        )
        
        # Update invoice
        invoice.amount_paid = (invoice.amount_paid or 0) + amount
        invoice.payment_date = payment.payment_date
        invoice.payment_method = payment.payment_method
        
        # Update payment status
        if invoice.amount_paid >= invoice.grand_total:
            invoice.payment_status = 'paid'
            invoice.invoice_status = 'paid'
        elif invoice.amount_paid > 0:
            invoice.payment_status = 'partial'
        
        invoice.modified_at = datetime.utcnow()
        db.session.add(payment)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Payment recorded',
            'payment_id': payment.id,
            'amount_paid': float(invoice.amount_paid),
            'outstanding': float(invoice.grand_total - invoice.amount_paid),
            'invoice_status': invoice.invoice_status
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>/payments', methods=['GET'])
def get_invoice_payments(invoice_id):
    """Get all payments for an invoice"""
    invoice = Invoice.query.get(invoice_id)
    if not invoice:
        return jsonify({'error': 'Invoice not found'}), 404
    
    return jsonify({
        'invoice_id': invoice_id,
        'payments': [p.to_dict() for p in invoice.payments],
        'total_amount': float(invoice.grand_total),
        'amount_paid': float(invoice.amount_paid or 0),
        'outstanding': float((invoice.grand_total or 0) - (invoice.amount_paid or 0))
    }), 200


@invoice_bp.route('/<invoice_id>/payment/<payment_id>/refund', methods=['POST'])
def refund_payment(invoice_id, payment_id):
    """
    Refund a payment
    Supports partial refunds
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        payment = Payment.query.get(payment_id)
        if not payment or payment.invoice_id != invoice_id:
            return jsonify({'error': 'Payment not found'}), 404
        
        data = request.get_json()
        refund_amount = Decimal(str(data.get('refund_amount', payment.amount)))
        
        if refund_amount > payment.amount:
            return jsonify({'error': 'Refund amount exceeds payment amount'}), 400
        
        payment.refund_amount = refund_amount
        payment.refund_reason = data.get('refund_reason')
        payment.refund_date = datetime.utcnow()
        payment.status = 'refunded'
        
        # Update invoice
        refunded_amount = refund_amount
        invoice.amount_paid = (invoice.amount_paid or 0) - refunded_amount
        
        if invoice.amount_paid <= 0:
            invoice.payment_status = 'pending'
        else:
            invoice.payment_status = 'partial'
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Payment refunded',
            'refund_amount': float(refund_amount),
            'amount_paid': float(invoice.amount_paid),
            'outstanding': float(invoice.grand_total - (invoice.amount_paid or 0))
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# RECEIPT ENDPOINTS
# ============================================================================

@invoice_bp.route('/<invoice_id>/receipt/generate', methods=['POST'])
def generate_receipt(invoice_id):
    """
    Generate receipt from invoice
    Supports multiple formats: pdf, thermal, email
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        # Check if receipt already exists
        receipt = invoice.receipt
        if not receipt:
            receipt = Receipt(
                invoice_id=invoice_id,
                receipt_number=f'REC-{invoice.invoice_number.replace("INV", "")}'
            )
            db.session.add(receipt)
            db.session.flush()
        
        data = request.get_json() or {}
        format = data.get('format', 'pdf')
        receipt.receipt_format = format
        
        # Generate warranty QR code URL
        warranty_items = [li.warranty_id for li in invoice.line_items if li.warranty_id]
        if warranty_items:
            receipt.warranty_qr_url = f'/warranty/lookup/{warranty_items[0]}'
        
        # Handle email delivery
        if data.get('send_email'):
            receipt.email_sent = True
            receipt.email_sent_at = datetime.utcnow()
            # TODO: Implement email sending
        
        receipt.created_at = datetime.utcnow()
        db.session.commit()
        
        receipt_data = {
            'invoice': invoice.to_dict(),
            'receipt_number': receipt.receipt_number,
            'format': format,
            'warranty_qr_url': receipt.warranty_qr_url
        }
        
        return jsonify({
            'success': True,
            'message': 'Receipt generated',
            'receipt_id': receipt.id,
            'receipt_number': receipt.receipt_number,
            'receipt_url': f'/receipt/{receipt.id}',
            'warranties': len([li for li in invoice.line_items if li.warranty_id])
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>/receipt/send', methods=['POST'])
def send_receipt(invoice_id):
    """
    Send receipt via email, SMS, or WhatsApp
    """
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        receipt = invoice.receipt
        if not receipt:
            return jsonify({'error': 'Receipt not found. Generate receipt first'}), 404
        
        data = request.get_json()
        method = data.get('method', 'email')  # email, sms, whatsapp
        destination = data.get('destination')
        
        if not destination:
            if method == 'email':
                destination = invoice.customer.email
            elif method == 'sms' or method == 'whatsapp':
                destination = invoice.customer.phone
        
        # Mark as sent (actual sending implementation would go here)
        if method == 'email':
            receipt.email_sent = True
            receipt.email_sent_at = datetime.utcnow()
        elif method == 'sms':
            receipt.sms_sent = True
        elif method == 'whatsapp':
            receipt.whatsapp_sent = True
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': f'Receipt sent via {method}',
            'method': method,
            'destination': destination
        }), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


# ============================================================================
# REPORTING ENDPOINTS
# ============================================================================

@invoice_bp.route('/report/summary', methods=['GET'])
def get_invoice_summary():
    """
    Get sales summary for date range
    Query params: from_date, to_date
    """
    try:
        from_date = request.args.get('from_date')
        to_date = request.args.get('to_date')
        
        query = Invoice.query
        
        if from_date:
            query = query.filter(Invoice.invoice_date >= parse_iso_datetime(from_date))
        if to_date:
            query = query.filter(Invoice.invoice_date <= parse_iso_datetime(to_date))
        
        invoices = query.all()
        
        total_amount = sum(float(inv.grand_total or 0) for inv in invoices)
        paid_amount = sum(float(inv.amount_paid or 0) for inv in invoices)
        outstanding = total_amount - paid_amount
        
        status_counts = {
            'draft': len([i for i in invoices if i.invoice_status == 'draft']),
            'issued': len([i for i in invoices if i.invoice_status == 'issued']),
            'paid': len([i for i in invoices if i.invoice_status == 'paid']),
            'overdue': len([i for i in invoices if i.invoice_status == 'overdue']),
            'cancelled': len([i for i in invoices if i.invoice_status == 'cancelled']),
        }
        
        payment_method_totals = {}
        for inv in invoices:
            method = inv.payment_method or 'unknown'
            if method not in payment_method_totals:
                payment_method_totals[method] = 0
            payment_method_totals[method] += float(inv.amount_paid or 0)
        
        return jsonify({
            'period': {
                'from_date': from_date,
                'to_date': to_date
            },
            'summary': {
                'total_invoices': len(invoices),
                'total_amount': total_amount,
                'paid_amount': paid_amount,
                'outstanding_amount': outstanding,
                'average_invoice': total_amount / len(invoices) if invoices else 0,
                'payment_success_rate': (len([i for i in invoices if i.payment_status == 'paid']) / len(invoices) * 100) if invoices else 0
            },
            'by_status': status_counts,
            'by_payment_method': payment_method_totals
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/report/customer/<customer_id>', methods=['GET'])
def get_customer_purchase_history(customer_id):
    """Get customer purchase history and warranty info"""
    try:
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        
        invoices = Invoice.query.filter_by(customer_id=customer_id).order_by(Invoice.invoice_date.desc()).all()
        
        history = []
        for inv in invoices:
            warranty_count = len([li for li in inv.line_items if li.warranty_id])
            history.append({
                'invoice_number': inv.invoice_number,
                'date': inv.invoice_date.isoformat() if inv.invoice_date else None,
                'amount': float(inv.grand_total or 0),
                'status': inv.invoice_status,
                'payment_status': inv.payment_status,
                'warranties': warranty_count,
                'items': len(inv.line_items)
            })
        
        return jsonify({
            'customer': customer.to_dict(),
            'total_invoices': len(invoices),
            'total_spent': sum(float(inv.grand_total or 0) for inv in invoices),
            'active_warranties': len(Warranty.query.filter_by(customer_id=customer_id, status='active').all()),
            'purchase_history': history
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# PRINT & DISPLAY ENDPOINTS
# ============================================================================

@invoice_bp.route('/<invoice_id>/print', methods=['GET'])
def print_invoice(invoice_id):
    """Generate a beautiful print view for an invoice"""
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        # Get company settings
        company = CompanySettings.query.first()
        if not company:
            company = CompanySettings(company_name='Company Name')
        
        # Prepare payment methods
        payment_methods = []
        if company.khqr_merchant_id:
            payment_methods.append({
                'name': 'KHQR (Bakong)',
                'details': {
                    'Merchant ID': company.khqr_merchant_id
                }
            })
        if company.aba_account_number:
            payment_methods.append({
                'name': 'ABA Bank',
                'details': {
                    'Account Number': company.aba_account_number,
                    'Account Holder': company.aba_account_holder or 'N/A'
                }
            })
        if company.acleda_account_number:
            payment_methods.append({
                'name': 'ACLEDA Bank',
                'details': {
                    'Account Number': company.acleda_account_number,
                    'Account Holder': company.acleda_account_holder or 'N/A'
                }
            })
        
        # Prepare warranty items
        warranty_items = []
        for line_item in invoice.line_items:
            if line_item.warranty_duration_months:
                warranty_end = invoice.invoice_date + timedelta(days=30*line_item.warranty_duration_months)
                warranty_items.append({
                    'description': line_item.description,
                    'warranty_months': line_item.warranty_duration_months,
                    'warranty_end_date': warranty_end.strftime('%Y-%m-%d') if warranty_end else 'N/A'
                })
        
        # Prepare template data
        template_data = {
            'invoice_number': invoice.invoice_number,
            'invoice_date': invoice.invoice_date.strftime('%B %d, %Y') if invoice.invoice_date else '',
            'due_date': invoice.due_date.strftime('%B %d, %Y') if invoice.due_date else '',
            'status': (invoice.invoice_status or 'draft').upper(),
            'payment_status': (invoice.payment_status or 'pending').upper(),
            'company_name': company.company_name or 'Company',
            'company_logo': company.logo_base64,
            'company_address': company.street_address or '',
            'company_city': company.city or '',
            'company_phone': company.phone or '',
            'company_email': company.email or '',
            'company_website': company.website or '',
            'customer_name': invoice.customer.name if invoice.customer else 'Customer',
            'customer_email': invoice.customer.email if invoice.customer else '',
            'customer_phone': invoice.customer.phone if invoice.customer else '',
            'billing_address': invoice.billing_address or '',
            'shipping_address': invoice.shipping_address or '',
            'currency': invoice.currency or 'USD',
            'items': [
                {
                    'description': item.description,
                    'quantity': item.quantity,
                    'unit_price': float(item.unit_price),
                    'line_total': float(item.line_total),
                    'warranty_months': item.warranty_duration_months,
                    'serial_number': item.serial_number
                }
                for item in invoice.line_items
            ],
            'subtotal': float(invoice.subtotal or 0),
            'tax_amount': float(invoice.tax_amount or 0),
            'discount_amount': float(invoice.discount_amount or 0),
            'shipping_cost': float(invoice.shipping_cost or 0),
            'grand_total': float(invoice.grand_total or 0),
            'payment_methods': payment_methods,
            'warranty_items': warranty_items,
            'notes': invoice.notes or '',
            'footer_text': company.invoice_footer_text or 'Thank you for your business!',
            'generation_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            'khqr_code': company.khqr_code_base64
        }
        
        # Read the print template based on language
        import os
        language = invoice.language if invoice.language else 'en'
        
        # Select template based on language
        if language == 'km':
            template_filename = 'INVOICE_PRINT_TEMPLATE_KM.html'
        else:
            template_filename = 'INVOICE_PRINT_TEMPLATE.html'
        
        template_path = os.path.join(os.path.dirname(__file__), '..', '..', template_filename)
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        return render_template_string(template, **template_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@invoice_bp.route('/<invoice_id>/receipt/print', methods=['GET'])
def print_receipt(invoice_id):
    """Generate a beautiful print view for a receipt"""
    try:
        invoice = Invoice.query.get(invoice_id)
        if not invoice:
            return jsonify({'error': 'Invoice not found'}), 404
        
        # Get company settings
        company = CompanySettings.query.first()
        if not company:
            company = CompanySettings(company_name='Company Name')
        
        # Get or create receipt
        receipt = Receipt.query.filter_by(invoice_id=invoice_id).first()
        if not receipt:
            receipt = Receipt(invoice_id=invoice_id, receipt_number=f'RCP-{datetime.utcnow().strftime("%Y%m%d%H%M%S")}')
            db.session.add(receipt)
            db.session.commit()
        
        # Get last payment
        payment = Payment.query.filter_by(invoice_id=invoice_id).order_by(Payment.payment_date.desc()).first()
        
        # Prepare warranty items
        warranty_items = []
        for line_item in invoice.line_items:
            if line_item.warranty_duration_months:
                warranty_end = invoice.invoice_date + timedelta(days=30*line_item.warranty_duration_months)
                warranty_items.append({
                    'product': line_item.description,
                    'warranty_duration': f'{line_item.warranty_duration_months} months',
                    'warranty_end_date': warranty_end.strftime('%Y-%m-%d') if warranty_end else 'N/A'
                })
        
        # Prepare template data
        template_data = {
            'receipt_number': receipt.receipt_number,
            'receipt_date': datetime.utcnow().strftime('%B %d, %Y'),
            'receipt_time': datetime.utcnow().strftime('%H:%M:%S'),
            'invoice_number': invoice.invoice_number,
            'company_name': company.company_name or 'Company',
            'company_address': company.street_address or '',
            'company_city': company.city or '',
            'company_phone': company.phone or '',
            'company_email': company.email or '',
            'customer_name': invoice.customer.name if invoice.customer else 'Customer',
            'customer_email': invoice.customer.email if invoice.customer else '',
            'customer_phone': invoice.customer.phone if invoice.customer else '',
            'currency': invoice.currency or 'USD',
            'items': [
                {
                    'description': item.description,
                    'quantity': item.quantity,
                    'unit_price': float(item.unit_price),
                    'line_total': float(item.line_total),
                    'serial_number': item.serial_number
                }
                for item in invoice.line_items
            ],
            'subtotal': float(invoice.subtotal or 0),
            'tax_amount': float(invoice.tax_amount or 0),
            'discount_amount': float(invoice.discount_amount or 0),
            'shipping_cost': float(invoice.shipping_cost or 0),
            'grand_total': float(invoice.grand_total or 0),
            'payment_method': payment.payment_method.upper() if payment else 'PENDING',
            'payment_status': (invoice.payment_status or 'PENDING').upper(),
            'transaction_reference': payment.reference_number if payment else '',
            'cash_currency': payment.cash_currency if payment else '',
            'warranty_items': warranty_items,
            'qr_code': receipt.qr_code if receipt.qr_code else None,
            'khqr_code': company.khqr_code_base64,
            'footer_text': company.receipt_footer_text or 'Thank you for your business!',
            'generation_date': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Read the print template based on language
        import os
        language = invoice.language if invoice.language else 'en'
        
        # Select template based on language
        if language == 'km':
            template_filename = 'RECEIPT_PRINT_TEMPLATE_KM.html'
        else:
            template_filename = 'RECEIPT_PRINT_TEMPLATE.html'
        
        template_path = os.path.join(os.path.dirname(__file__), '..', '..', template_filename)
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        return render_template_string(template, **template_data)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def generate_invoice_number():
    """Generate unique invoice number"""
    # Get or create company settings
    settings = CompanySettings.query.first()
    if not settings:
        settings = CompanySettings(company_name='Default Company')
        db.session.add(settings)
        db.session.commit()
    
    # Generate invoice number
    prefix = settings.invoice_prefix or 'INV'
    sequence = settings.invoice_sequence or 1
    invoice_number = f'{prefix}-{datetime.utcnow().year}-{str(sequence).zfill(6)}'
    
    # Increment sequence
    settings.invoice_sequence = sequence + 1
    db.session.commit()
    
    return invoice_number
