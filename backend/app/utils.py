"""
Utility functions for the warranty product system
"""

from flask import request
import qrcode
from io import BytesIO
import base64


def get_pagination_params():
    """
    Extract pagination parameters from request args
    Returns: (page, per_page)
    """
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        
        # Validate
        if page < 1:
            page = 1
        if per_page < 1 or per_page > 100:
            per_page = 20
            
        return page, per_page
    except (ValueError, TypeError):
        return 1, 20


def generate_qr_code(data):
    """
    Generate QR code from data string
    Returns: base64 encoded image or image bytes
    """
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Convert to bytes
        img_io = BytesIO()
        img.save(img_io, 'PNG')
        img_io.seek(0)
        
        # Encode to base64 for embedding in HTML
        img_base64 = base64.b64encode(img_io.getvalue()).decode()
        return f"data:image/png;base64,{img_base64}"
    except Exception as e:
        print(f"QR code generation failed: {e}")
        return None


def format_currency(amount, currency='USD'):
    """Format amount as currency string"""
    currency_symbols = {
        'USD': '$',
        'EUR': '€',
        'GBP': '£',
        'JPY': '¥',
        'INR': '₹',
        'CNY': '¥',
        'AUD': 'A$',
        'CAD': 'C$',
    }
    symbol = currency_symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"


def get_remote_address():
    """Get client IP address"""
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0]
    return request.remote_addr
