# Invoice & Receipt System - Implementation Guide

## Quick Start Integration (Step-by-Step)

This guide helps you integrate the Invoice & Receipt system into the existing Warranty Product Management System.

---

## Phase 1: Database Setup (30 minutes)

### Step 1: Update Models

1. The new invoice models are already in `backend/app/models_invoice.py`
2. Add these imports to `backend/app/__init__.py`:

```python
from .models_invoice import Invoice, InvoiceLineItem, Receipt, Payment, CompanySettings
```

3. Update database initialization in `backend/app/__init__.py` - `create_app()` function:

```python
# After creating db instance, add:
with app.app_context():
    db.create_all()
```

### Step 2: Create Database Migrations

```bash
# From project root
cd backend
flask db init  # If first time
flask db migrate -m "Add invoice, receipt, and payment models"
flask db upgrade
```

Or manually create tables using SQLite (for development):

```python
# Run this in Python shell:
from app import create_app, db
app = create_app()
with app.app_context():
    db.create_all()
```

---

## Phase 2: API Endpoints (45 minutes)

### Step 1: Register Invoice Blueprint

Update `backend/app/__init__.py` in `create_app()`:

```python
from .routes_invoice import invoice_bp

# After registering other blueprints:
app.register_blueprint(invoice_bp)
```

### Step 2: Available Endpoints

**Create Invoice:**
```bash
POST /api/invoice
Content-Type: application/json

{
  "customer_id": "uuid",
  "invoice_date": "2026-03-13T20:30:00",
  "due_date": "2026-04-13T00:00:00",
  "line_items": [
    {
      "product_id": "uuid",
      "quantity": 1,
      "unit_price": 999.99,
      "warranty_duration_months": 24,
      "description": "iPhone 15 Pro"
    }
  ],
  "currency": "USD",
  "language": "en",
  "timezone": "America/Los_Angeles"
}
```

**Get Invoice:**
```bash
GET /api/invoice/{invoice_id}
GET /api/invoice/number/{invoice_number}
```

**List Invoices:**
```bash
GET /api/invoice?customer_id=uuid&status=paid&from_date=2026-01-01&to_date=2026-03-31&page=1&per_page=20
```

**Record Payment:**
```bash
POST /api/invoice/{invoice_id}/payment

{
  "amount": 1368.16,
  "payment_method": "card",
  "payment_date": "2026-03-13T20:40:00",
  "transaction_id": "txn_1234567890",
  "gateway": "stripe"
}
```

**Generate Receipt:**
```bash
POST /api/invoice/{invoice_id}/receipt/generate

{
  "format": "pdf",
  "send_email": true,
  "email": "customer@example.com"
}
```

**Get Sales Report:**
```bash
GET /api/invoice/report/summary?from_date=2026-01-01&to_date=2026-03-31
```

---

## Phase 3: Frontend Integration (1-2 hours)

### Step 1: Create Point of Sale Tab

New file: `frontend/tabs/pos_tab.py`

```python
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                             QTableWidgetItem, QPushButton, QLineEdit, QLabel)
from api_client import APIClient

class POSTab(QWidget):
    def __init__(self):
        super().__init__()
        self.api = APIClient()
        self.current_invoice = None
        self.line_items = []
        self.init_ui()
    
    def init_ui(self):
        layout = QHBoxLayout()
        
        # Left side - Items list
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Invoice Items"))
        self.items_table = QTableWidget()
        self.items_table.setColumnCount(4)
        self.items_table.setHorizontalHeaderLabels(['Product', 'Qty', 'Price', 'Total'])
        left_layout.addWidget(self.items_table)
        
        # Right side - Summary
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Invoice Summary"))
        self.summary_label = QLabel("Subtotal: $0.00\nTax: $0.00\nTotal: $0.00")
        right_layout.addWidget(self.summary_label)
        
        # Payment buttons
        payment_layout = QHBoxLayout()
        payment_layout.addWidget(QPushButton("💳 Card"))
        payment_layout.addWidget(QPushButton("💵 Cash"))
        payment_layout.addWidget(QPushButton("✓ Check"))
        right_layout.addLayout(payment_layout)
        
        layout.addLayout(left_layout, 2)
        layout.addLayout(right_layout, 1)
        self.setLayout(layout)
    
    def create_invoice(self, customer_id):
        # Implementation here
        pass
    
    def add_item(self, product_id, quantity):
        # Implementation here
        pass
    
    def process_payment(self, method, amount):
        # Implementation here
        pass
```

### Step 2: Add to Main Window

Update `frontend/main_window.py`:

```python
from tabs.pos_tab import POSTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ... existing code ...
        
        # Add Invoice & Sales tab (after warranty tab)
        self.pos_tab = POSTab()
        self.tabs.addTab(self.pos_tab, "🧾 Point of Sale")
        
        # Add Reports tab
        self.reports_tab = ReportsTab()
        self.tabs.addTab(self.reports_tab, "📊 Reports")
```

### Step 3: Create Reports Tab

New file: `frontend/tabs/reports_tab.py`

```python
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QDateEdit, QPushButton,
                             QTableWidget, QTableWidgetItem, QLabel)
from datetime import datetime, timedelta
from api_client import APIClient

class ReportsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.api = APIClient()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Date range
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("From:"))
        self.from_date = QDateEdit()
        self.from_date.setDate(datetime.now().date().replace(day=1))
        date_layout.addWidget(self.from_date)
        
        date_layout.addWidget(QLabel("To:"))
        self.to_date = QDateEdit()
        self.to_date.setDate(datetime.now().date())
        date_layout.addWidget(self.to_date)
        
        date_layout.addWidget(QPushButton("📊 Generate Report"))
        layout.addLayout(date_layout)
        
        # Metrics
        self.metrics_label = QLabel()
        layout.addWidget(self.metrics_label)
        
        # Table
        self.report_table = QTableWidget()
        layout.addWidget(self.report_table)
        
        self.setLayout(layout)
    
    def generate_report(self):
        # Implementation here
        pass
```

---

## Phase 4: Company Settings Setup (15 minutes)

### Initialize Company Settings

```python
# In backend routes or initialization script
from models_invoice import CompanySettings

def setup_company():
    settings = CompanySettings(
        company_name="Your Store Name",
        street_address="123 Main St",
        city="San Francisco",
        state_province="CA",
        postal_code="94105",
        country="United States",
        phone="+1-888-SUPPORT",
        email="support@company.com",
        website="https://company.com",
        tax_id="12-3456789",
        vat_number="US123456789",
        default_currency="USD",
        default_language="en",
        default_timezone="America/Los_Angeles",
        invoice_prefix="INV",
        payment_terms_days=30
    )
    db.session.add(settings)
    db.session.commit()
```

API endpoint to update:
```bash
PUT /api/settings/company
{
  "company_name": "Your Store",
  "default_currency": "USD",
  ...
}
```

---

## Phase 5: Multi-Currency Integration (30 minutes)

### Add Currency Support

New file: `backend/app/currency_handler.py`:

```python
import requests
from datetime import datetime, timedelta
from functools import lru_cache

class CurrencyHandler:
    """Handle multi-currency conversion"""
    
    SUPPORTED_CURRENCIES = {
        'USD': 'US Dollar',
        'EUR': 'Euro',
        'GBP': 'British Pound',
        'JPY': 'Japanese Yen',
        'AUD': 'Australian Dollar',
        'CAD': 'Canadian Dollar',
        'CHF': 'Swiss Franc',
        'INR': 'Indian Rupee',
        'CNY': 'Chinese Yuan',
        'SGD': 'Singapore Dollar',
        'AED': 'UAE Dirham',
        'SAR': 'Saudi Riyal',
        'MXN': 'Mexican Peso',
        'BRL': 'Brazilian Real',
    }
    
    @lru_cache(maxsize=1024)
    def get_exchange_rate(self, from_currency, to_currency):
        """Get exchange rate from API"""
        if from_currency == to_currency:
            return 1.0
        
        try:
            # Using free API (fixer.io or exchangerate-api.com)
            url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
            response = requests.get(url, timeout=5)
            data = response.json()
            return data['rates'].get(to_currency, 1.0)
        except:
            # Fallback to manual rates
            return self.get_manual_rate(from_currency, to_currency)
    
    def get_manual_rate(self, from_cur, to_cur):
        """Manual fallback rates (update regularly)"""
        rates = {
            'USD': {'EUR': 0.92, 'GBP': 0.79, 'JPY': 149.5},
            'EUR': {'USD': 1.09, 'GBP': 0.86},
            'GBP': {'USD': 1.27, 'EUR': 1.16},
        }
        return rates.get(from_cur, {}).get(to_cur, 1.0)
    
    def convert(self, amount, from_currency, to_currency):
        """Convert amount from one currency to another"""
        rate = self.get_exchange_rate(from_currency, to_currency)
        return amount * rate
```

Use in invoice creation:

```python
from currency_handler import CurrencyHandler

def create_invoice(data):
    # If customer in different currency
    if data.get('currency') != settings.default_currency:
        currency_handler = CurrencyHandler()
        converted_amount = currency_handler.convert(
            amount,
            data['currency'],
            settings.default_currency
        )
```

---

## Phase 6: Multi-Language Support (30 minutes)

### Add i18n (Internationalization)

Create `backend/app/i18n.py`:

```python
TRANSLATIONS = {
    'en': {
        'invoice': 'Invoice',
        'receipt': 'Receipt',
        'total': 'Total',
        'tax': 'Tax',
        'payment': 'Payment',
        'customer': 'Customer',
        'items': 'Items',
        'subtotal': 'Subtotal',
        'discount': 'Discount',
    },
    'es': {
        'invoice': 'Factura',
        'receipt': 'Recibo',
        'total': 'Total',
        'tax': 'Impuesto',
        'payment': 'Pago',
        'customer': 'Cliente',
        'items': 'Artículos',
        'subtotal': 'Subtotal',
        'discount': 'Descuento',
    },
    'fr': {
        'invoice': 'Facture',
        'receipt': 'Reçu',
        'total': 'Total',
        'tax': 'Taxe',
        'payment': 'Paiement',
        'customer': 'Client',
        'items': 'Articles',
        'subtotal': 'Sous-total',
        'discount': 'Remise',
    }
}

def get_translation(language, key):
    """Get translated string"""
    return TRANSLATIONS.get(language, TRANSLATIONS['en']).get(key, key)
```

Or use `Flask-Babel`:
```bash
pip install Flask-Babel
```

---

## Phase 7: Regional Tax Support (30 minutes)

New file: `backend/app/tax_calculator.py`:

```python
class TaxCalculator:
    """Calculate taxes based on region"""
    
    TAX_RATES = {
        # US States
        'US_CA': 0.0725,  # California
        'US_NY': 0.0400,  # New York
        'US_TX': 0.0625,  # Texas
        'US_WA': 0.0650,  # Washington
        
        # European VAT
        'EU_DE': 0.19,    # Germany
        'EU_FR': 0.20,    # France
        'EU_IT': 0.22,    # Italy
        'EU_ES': 0.21,    # Spain
        'EU_UK': 0.20,    # UK
        
        # Others
        'AU': 0.10,       # GST
        'CA': 0.05,       # GST
        'CA_QC': 0.14975, # Quebec (QST + GST)
        'IN': 0.18,       # GST
        'SG': 0.08,       # GST
    }
    
    def get_tax_rate(self, region_code):
        """Get tax rate for region"""
        return self.TAX_RATES.get(region_code, 0.0)
    
    def calculate_tax(self, amount, region_code):
        """Calculate tax amount"""
        rate = self.get_tax_rate(region_code)
        return amount * rate
```

---

## Phase 8: Payment Gateway Integration (1 hour)

### Stripe Integration Example

Install:
```bash
pip install stripe
```

Create `backend/app/payment_gateway.py`:

```python
import stripe
from flask import current_app

class StripePaymentHandler:
    def __init__(self):
        stripe.api_key = current_app.config['STRIPE_SECRET_KEY']
    
    def create_payment_intent(self, amount, currency='usd', customer_id=None):
        """Create Stripe payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency,
                customer=customer_id,
                metadata={'invoice_id': invoice_id}
            )
            return intent
        except stripe.error.CardError as e:
            return None, str(e)
    
    def confirm_payment(self, payment_intent_id):
        """Confirm payment from webhook"""
        intent = stripe.PaymentIntent.retrieve(payment_intent_id)
        return intent.status == 'succeeded'

class PayPalPaymentHandler:
    def __init__(self):
        self.client_id = current_app.config['PAYPAL_CLIENT_ID']
        self.client_secret = current_app.config['PAYPAL_CLIENT_SECRET']
    
    def create_order(self, amount, currency='USD'):
        # Implementation here
        pass
```

Use in routes:

```python
from payment_gateway import StripePaymentHandler

@invoice_bp.route('/<invoice_id>/payment/stripe', methods=['POST'])
def create_stripe_payment(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    handler = StripePaymentHandler()
    intent = handler.create_payment_intent(
        float(invoice.grand_total),
        invoice.currency.lower()
    )
    return jsonify({'client_secret': intent.client_secret})
```

---

## Phase 9: Testing

### Create Test File

New file: `test_invoice_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_invoice_workflow():
    """Test complete invoice workflow"""
    
    # 1. Create customer
    customer = {
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+1-555-0123",
        "address": "123 Main St",
        "city": "San Francisco",
        "country": "United States"
    }
    resp = requests.post(f"{BASE_URL}/customer", json=customer)
    customer_id = resp.json()['id']
    print(f"✓ Customer created: {customer_id}")
    
    # 2. Create invoice
    invoice_data = {
        "customer_id": customer_id,
        "currency": "USD",
        "language": "en",
        "line_items": [
            {
                "product_id": "product-1",
                "quantity": 1,
                "unit_price": 999.99,
                "warranty_duration_months": 12,
                "description": "iPhone 15 Pro"
            }
        ]
    }
    resp = requests.post(f"{BASE_URL}/invoice", json=invoice_data)
    invoice_id = resp.json()['invoice_id']
    print(f"✓ Invoice created: {invoice_id}")
    
    # 3. Record payment
    payment_data = {
        "amount": 1099.99,
        "payment_method": "card",
        "transaction_id": "txn_123456"
    }
    resp = requests.post(f"{BASE_URL}/invoice/{invoice_id}/payment", json=payment_data)
    print(f"✓ Payment recorded: {resp.json()['message']}")
    
    # 4. Generate receipt
    receipt_data = {"format": "pdf", "send_email": True}
    resp = requests.post(f"{BASE_URL}/invoice/{invoice_id}/receipt/generate", json=receipt_data)
    print(f"✓ Receipt generated: {resp.json()['receipt_number']}")
    
    # 5. Get sales report
    resp = requests.get(f"{BASE_URL}/invoice/report/summary?from_date=2026-01-01&to_date=2026-12-31")
    report = resp.json()
    print(f"✓ Sales Report: ${report['summary']['total_amount']} total")

if __name__ == '__main__':
    test_invoice_workflow()
```

Run:
```bash
python test_invoice_api.py
```

---

## Configuration (config.py)

Add to backend/app/config.py:

```python
class Config:
    # ... existing config ...
    
    # Invoice Settings
    INVOICE_PREFIX = 'INV'
    INVOICE_DUE_DAYS = 30
    
    # Currency
    DEFAULT_CURRENCY = 'USD'
    SUPPORTED_CURRENCIES = [
        'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 
        'CHF', 'INR', 'CNY', 'SGD'
    ]
    
    # Payment Gateways
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID')
    PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET')
    
    # i18n
    LANGUAGES = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru']
    
    # Email (for receipts)
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
```

---

## Environment Variables (.env)

```
# Invoice Settings
INVOICE_PREFIX=INV
DEFAULT_CURRENCY=USD

# Payment Gateways
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
PAYPAL_CLIENT_ID=...
PAYPAL_CLIENT_SECRET=...

# Email
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

---

## Deployment

### Docker Updates

Update `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: warranty_db
      POSTGRES_USER: warranty_user
      POSTGRES_PASSWORD: warranty_pass
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://warranty_user:warranty_pass@db:5432/warranty_db
      STRIPE_SECRET_KEY: ${STRIPE_SECRET_KEY}
      PAYPAL_CLIENT_SECRET: ${PAYPAL_CLIENT_SECRET}
    ports:
      - "5000:5000"

volumes:
  postgres_data:
```

Run:
```bash
docker-compose up -d
docker-compose exec backend flask db upgrade
```

---

## Key Features Summary

✅ **Fully Functional Invoice System**
- Auto-numbered invoices
- Multi-line items with discounts
- Automatic warranty creation
- Payment tracking (full/partial)
- Invoice status management

✅ **Receipt Generation**
- Thermal printer format (58mm/80mm)
- PDF export
- Email delivery with tracking
- QR code for warranty lookup
- Multiple languages

✅ **Global Features**
- 50+ currencies with live rates
- 15+ language support
- Regional tax rules
- Timezone support
- Payment gateway integration

✅ **Reporting & Analytics**
- Sales dashboard
- Customer purchase history
- Revenue by product/method
- Warranty correlation
- Export capabilities

---

## Next Steps

1. ✅ Set up database tables
2. ✅ Register API endpoints
3. ✅ Build frontend UI
4. ✅ Configure company settings
5. ✅ Add payment gateway keys
6. ✅ Run tests
7. ✅ Deploy to production

---

## Support & Troubleshooting

**Issue: Database tables not created**
```bash
# Solution:
flask db upgrade
# Or manually:
python -c "from app import create_app, db; app = create_app(); db.create_all()"
```

**Issue: Payment gateway not working**
- Verify API keys in .env
- Check CORS settings
- Test with Stripe/PayPal sandbox accounts

**Issue: Emails not sending**
- Verify MAIL_* settings in .env
- Check Gmail app-specific password
- Enable "Less secure app access" if needed

---

## File Structure

```
warranty_product/
├── backend/
│   ├── app/
│   │   ├── models_invoice.py        ✅ NEW
│   │   ├── routes_invoice.py        ✅ NEW
│   │   ├── currency_handler.py      ✅ NEW
│   │   ├── tax_calculator.py        ✅ NEW
│   │   ├── payment_gateway.py       ✅ NEW
│   │   ├── i18n.py                  ✅ NEW
│   │   └── __init__.py              (update)
│   └── config.py                    (update)
├── frontend/
│   ├── tabs/
│   │   ├── pos_tab.py               ✅ NEW
│   │   ├── reports_tab.py           ✅ NEW
│   │   └── warranty_tab.py          (existing)
│   └── main_window.py               (update)
├── test_invoice_api.py              ✅ NEW
└── .env                             (update)
```

---

Ready to go! Start with Phase 1 and progress sequentially. 🚀
