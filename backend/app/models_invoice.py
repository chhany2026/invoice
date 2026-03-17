"""
Invoice & Receipt Models
Handles invoicing, payment tracking, and receipt generation
"""

from datetime import datetime
from decimal import Decimal
from sqlalchemy import Index, ForeignKey, Numeric, DateTime, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.sqlite import JSON
import uuid
from . import db


class Invoice(db.Model):
    """
    Main invoice model for tracking sales transactions
    Linked to both products and warranties
    """
    __tablename__ = 'invoices'

    # Primary Key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

    # Invoice Details
    invoice_number = db.Column(db.String(50), unique=True, nullable=False, index=True)
    invoice_date = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    due_date = db.Column(DateTime)
    
    # Customer Reference
    customer_id = db.Column(db.String(36), ForeignKey('customers.id'), nullable=False, index=True)
    
    # Address Information
    billing_address = db.Column(db.String(500))
    shipping_address = db.Column(db.String(500))
    
    # Monetary Values (using Numeric for precision)
    subtotal = db.Column(Numeric(12, 2), nullable=False, default=0)
    tax_amount = db.Column(Numeric(12, 2), default=0)
    discount_amount = db.Column(Numeric(12, 2), default=0)
    shipping_cost = db.Column(Numeric(12, 2), default=0)
    grand_total = db.Column(Numeric(12, 2), nullable=False, default=0)
    
    # Payment Information
    payment_method = db.Column(db.String(50))  # cash, card, check, bank_transfer, etc.
    payment_status = db.Column(db.String(50), default='pending')  # pending, partial, paid, refunded
    amount_paid = db.Column(Numeric(12, 2), default=0)
    payment_date = db.Column(DateTime)
    payment_reference = db.Column(db.String(255))  # Transaction ID from payment gateway
    
    # Global Settings
    currency = db.Column(db.String(3), default='USD')  # USD, EUR, GBP, etc.
    language = db.Column(db.String(10), default='en')  # en, es, fr, de, etc.
    timezone = db.Column(db.String(50))  # UTC, PST, EST, etc.
    tax_rate = db.Column(Numeric(5, 2), default=0)  # Tax percentage
    
    # Status & Notes
    invoice_status = db.Column(db.String(50), default='draft')  # draft, issued, sent, paid, overdue, cancelled
    notes = db.Column(db.Text)
    internal_notes = db.Column(db.Text)
    terms_and_conditions = db.Column(db.Text)
    
    # Metadata
    company_id = db.Column(db.String(36))  # For multi-tenant support
    created_by = db.Column(db.String(36))
    created_at = db.Column(DateTime, default=datetime.utcnow)
    modified_by = db.Column(db.String(36))
    modified_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = db.Column(DateTime)  # Soft delete support
    
    # Relationships
    customer = relationship('Customer', back_populates='invoices', lazy='joined')
    line_items = relationship('InvoiceLineItem', backref='invoice', lazy='joined', cascade='all, delete-orphan')
    payments = relationship('Payment', backref='invoice', lazy='joined', cascade='all, delete-orphan')
    receipt = relationship('Receipt', backref='invoice', uselist=False, cascade='all, delete-orphan')
    
    # Indexes for performance
    __table_args__ = (
        Index('idx_invoice_customer_date', 'customer_id', 'invoice_date'),
        Index('idx_invoice_status', 'invoice_status'),
        Index('idx_invoice_payment_status', 'payment_status'),
    )
    
    def __repr__(self):
        return f'<Invoice {self.invoice_number} - ${self.grand_total} {self.currency}>'
    
    def to_dict(self):
        """Convert invoice to dictionary"""
        return {
            'id': self.id,
            'invoice_number': self.invoice_number,
            'invoice_date': self.invoice_date.isoformat() if self.invoice_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'customer_id': self.customer_id,
            'customer': self.customer.to_dict() if self.customer else None,
            'subtotal': float(self.subtotal),
            'tax_amount': float(self.tax_amount),
            'discount_amount': float(self.discount_amount),
            'shipping_cost': float(self.shipping_cost),
            'grand_total': float(self.grand_total),
            'payment_method': self.payment_method,
            'payment_status': self.payment_status,
            'amount_paid': float(self.amount_paid),
            'outstanding': float(self.grand_total - (self.amount_paid or 0)),
            'currency': self.currency,
            'language': self.language,
            'invoice_status': self.invoice_status,
            'line_items': [item.to_dict() for item in self.line_items],
            'notes': self.notes,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class InvoiceLineItem(db.Model):
    """
    Line items in an invoice
    Each item can be linked to a product and warranty
    """
    __tablename__ = 'invoice_line_items'
    
    # Primary Key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Foreign Keys
    invoice_id = db.Column(db.String(36), ForeignKey('invoices.id'), nullable=False, index=True)
    product_id = db.Column(db.String(36), ForeignKey('products.id'))
    
    # Item Details
    description = db.Column(db.String(500), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    unit_price = db.Column(Numeric(12, 2), nullable=False)
    discount = db.Column(Numeric(12, 2), default=0)  # Line-level discount
    tax_rate = db.Column(Numeric(5, 2), default=0)  # Line-level tax
    line_total = db.Column(Numeric(12, 2), nullable=False)
    
    # Warranty Information (auto-populated from product)
    warranty_id = db.Column(db.String(36), ForeignKey('warranties.id'))
    warranty_duration_months = db.Column(db.Integer)
    serial_number = db.Column(db.String(255))  # Product serial number
    
    # Metadata
    created_at = db.Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    product = relationship('Product', lazy='joined')
    warranty = relationship('Warranty', back_populates='invoice_items')
    
    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'description': self.description,
            'quantity': self.quantity,
            'unit_price': float(self.unit_price),
            'discount': float(self.discount),
            'tax_rate': float(self.tax_rate),
            'line_total': float(self.line_total),
            'warranty_duration_months': self.warranty_duration_months,
            'serial_number': self.serial_number,
            'warranty_id': self.warranty_id,
        }


class Receipt(db.Model):
    """
    Receipt model - generates receipts from invoices
    Handles multiple delivery methods (print, email, SMS, WhatsApp)
    """
    __tablename__ = 'receipts'
    
    # Primary Key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Foreign Key
    invoice_id = db.Column(db.String(36), ForeignKey('invoices.id'), unique=True, nullable=False)
    
    # Receipt Details
    receipt_number = db.Column(db.String(50), unique=True)
    
    # Delivery Methods
    printed = db.Column(Boolean, default=False)
    email_sent = db.Column(Boolean, default=False)
    sms_sent = db.Column(Boolean, default=False)
    whatsapp_sent = db.Column(Boolean, default=False)
    
    # Tracking
    printed_at = db.Column(DateTime)
    email_sent_at = db.Column(DateTime)
    opened_at = db.Column(DateTime)  # For email tracking
    clicked_at = db.Column(DateTime)  # Clicked warranty link from email
    
    # Content
    receipt_format = db.Column(db.String(50))  # thermal58, thermal80, pdf, email
    qr_code = db.Column(LargeBinary)  # Stored QR code image
    warranty_qr_url = db.Column(db.String(500))  # URL to warranty lookup
    
    # Metadata
    created_at = db.Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'invoice_id': self.invoice_id,
            'receipt_number': self.receipt_number,
            'printed': self.printed,
            'email_sent': self.email_sent,
            'sms_sent': self.sms_sent,
            'whatsapp_sent': self.whatsapp_sent,
            'printed_at': self.printed_at.isoformat() if self.printed_at else None,
            'email_sent_at': self.email_sent_at.isoformat() if self.email_sent_at else None,
            'warranty_qr_url': self.warranty_qr_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class Payment(db.Model):
    """
    Payment tracking model
    Handles partial payments, refunds, and multiple payment methods
    Supports bank transfers (KHQR, ABA, ACLEDA) and cash
    """
    __tablename__ = 'payments'
    
    # Primary Key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Foreign Key
    invoice_id = db.Column(db.String(36), ForeignKey('invoices.id'), nullable=False, index=True)
    
    # Payment Details
    amount = db.Column(Numeric(12, 2), nullable=False)
    payment_date = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    payment_method = db.Column(db.String(50), nullable=False)  # cash, bank, khqr, aba, acleda, card, check
    status = db.Column(db.String(50), default='completed')  # pending, completed, failed, refunded
    
    # Payment Gateway Information
    gateway = db.Column(db.String(50))  # bank, khqr, aba, acleda, stripe, paypal, square, cash
    transaction_id = db.Column(db.String(255))
    reference_number = db.Column(db.String(255))
    
    # Bank Payment Details (for KHQR, ABA, ACLEDA, etc.)
    bank_name = db.Column(db.String(255))  # Bank name
    bank_account_holder = db.Column(db.String(255))  # Account holder name
    bank_account_number = db.Column(db.String(100))  # Account number
    bank_routing_number = db.Column(db.String(100))  # Routing/Branch code
    khqr_code = db.Column(db.Text)  # Base64 KHQR QR code image
    
    # Cash Payment Details
    cash_currency = db.Column(db.String(3))  # KHR (Riel) or USD for cash payments
    
    # Refund Information
    refund_amount = db.Column(Numeric(12, 2))
    refund_reason = db.Column(db.Text)
    refund_date = db.Column(DateTime)
    
    # Notes
    notes = db.Column(db.Text)
    
    # Metadata
    created_by = db.Column(db.String(36))
    created_at = db.Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'invoice_id': self.invoice_id,
            'amount': float(self.amount),
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'payment_method': self.payment_method,
            'status': self.status,
            'gateway': self.gateway,
            'transaction_id': self.transaction_id,
            'bank_name': self.bank_name,
            'bank_account_holder': self.bank_account_holder,
            'bank_account_number': self.bank_account_number,
            'cash_currency': self.cash_currency,
            'refund_amount': float(self.refund_amount) if self.refund_amount else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class CompanySettings(db.Model):
    """
    Company/Store settings for invoices and receipts
    Supports multi-tenant and multi-location operations
    """
    __tablename__ = 'company_settings'
    
    # Primary Key
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    # Basic Information
    company_name = db.Column(db.String(255), nullable=False)
    logo_url = db.Column(db.Text)
    logo_base64 = db.Column(db.Text)  # Logo stored as base64 for printing
    
    # Address
    street_address = db.Column(db.String(500))
    city = db.Column(db.String(100))
    state_province = db.Column(db.String(100))
    postal_code = db.Column(db.String(20))
    country = db.Column(db.String(100))
    
    # Contact Information
    phone = db.Column(db.String(20))
    email = db.Column(db.String(255))
    website = db.Column(db.String(255))
    
    # Tax Information
    tax_id = db.Column(db.String(50))  # US Tax ID / EIN
    vat_number = db.Column(db.String(50))  # EU VAT Number
    
    # Bank Details - Primary
    bank_name = db.Column(db.String(255))
    account_holder = db.Column(db.String(255))
    account_number = db.Column(db.String(50))
    routing_number = db.Column(db.String(50))
    swift_code = db.Column(db.String(50))
    iban = db.Column(db.String(50))
    
    # Cambodia Bank Payment Methods (JSON format for flexibility)
    khqr_merchant_id = db.Column(db.String(255))  # KHQR Merchant ID
    khqr_code_base64 = db.Column(db.Text)  # KHQR QR code as base64
    aba_account_number = db.Column(db.String(100))  # ABA Bank account
    aba_account_holder = db.Column(db.String(255))  # ABA Account holder
    acleda_account_number = db.Column(db.String(100))  # ACLEDA Bank account
    acleda_account_holder = db.Column(db.String(255))  # ACLEDA Account holder
    
    # Preferred Payment Methods (comma-separated)
    preferred_payment_methods = db.Column(db.Text, default='cash,bank')
    
    # Receipt/Invoice Footer Text
    invoice_footer_text = db.Column(db.Text)
    receipt_footer_text = db.Column(db.Text)
    
    # Default Settings
    default_currency = db.Column(db.String(3), default='USD')
    default_language = db.Column(db.String(10), default='en')
    default_timezone = db.Column(db.String(50), default='UTC')
    
    # Invoice Settings
    invoice_prefix = db.Column(db.String(20), default='INV')
    invoice_sequence = db.Column(db.Integer, default=1)
    payment_terms_days = db.Column(db.Integer, default=30)
    
    # Terms & Policies
    terms_and_conditions = db.Column(db.Text)
    return_policy = db.Column(db.Text)
    warranty_policy = db.Column(db.Text)
    
    # Metadata
    created_at = db.Column(DateTime, default=datetime.utcnow)
    modified_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'logo_url': self.logo_url,
            'logo_base64': self.logo_base64,
            'street_address': self.street_address,
            'city': self.city,
            'state_province': self.state_province,
            'postal_code': self.postal_code,
            'country': self.country,
            'phone': self.phone,
            'email': self.email,
            'website': self.website,
            'tax_id': self.tax_id,
            'vat_number': self.vat_number,
            'bank_name': self.bank_name,
            'account_holder': self.account_holder,
            'account_number': self.account_number,
            'khqr_merchant_id': self.khqr_merchant_id,
            'aba_account_number': self.aba_account_number,
            'acleda_account_number': self.acleda_account_number,
            'preferred_payment_methods': self.preferred_payment_methods,
            'default_currency': self.default_currency,
            'default_language': self.default_language,
            'default_timezone': self.default_timezone,
            'invoice_prefix': self.invoice_prefix,
            'payment_terms_days': self.payment_terms_days,
        }
