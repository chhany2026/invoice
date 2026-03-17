# 🚀 Cambodia Payment Methods & Beautiful Print - Quick Start Guide

## What's New? 🎉

Your invoice and receipt system now supports **Cambodia-specific payment methods** with **beautiful professional print templates**.

---

## 💳 PAYMENT METHODS

### 1. **Cash (💵 KHR/USD)**
- Choose currency: Riel (KHR) or Dollar (USD)
- Add optional notes (e.g., "Received in Phnom Penh")
- ✅ **Best for**: On-site payments

### 2. **KHQR (Bakong) - 🇰🇭**
- Modern QR-based payment system
- Works with all Cambodian banks
- ✅ **Best for**: Fast, traceable payments

### 3. **ABA Bank**
- Account transfer
- Any ABA branch in Cambodia
- ✅ **Best for**: Business accounts

### 4. **ACLEDA Bank**
- Large commercial bank
- Account transfer
- ✅ **Best for**: Standard bank transfers

---

## 🎨 NEW PRINT FEATURES

### Invoice Print
**What it includes:**
- Company logo & name
- Invoice number & date
- Customer details (bill-to, ship-to)
- **All items** with warranty info
- **Total breakdown** (subtotal, tax, shipping)
- **Payment methods** available
- **KHQR QR code** for payment
- Professional footer

**Access**: 📄 Click **[Print]** button on any invoice

### Receipt Print
**What it includes:**
- Receipt number & timestamp
- **Compact item list**
- **Grand total** (large, easy to read)
- Payment method used
- **Warranty stamp**
- KHQR code (for re-payment if needed)
- Thank you message

**Access**: 🧾 Click **[Print Receipt]** button after payment

---

## 🎯 HOW TO USE

### Creating an Invoice with Payment

#### Step 1: Create Invoice
1. Fill in customer details (name, email, phone)
2. Add products/items
3. **Select currency**: USD, EUR, GBP, KHR, etc.
4. **Set tax**: Manual tax amount or percentage
5. Click **✓ Create & Issue Invoice**

#### Step 2: Record Payment
1. Go to **Payments** tab
2. **Select Payment Type**:
   - 💵 **Cash** → Choose currency (KHR/USD)
   - 🏦 **Bank** → Select bank (KHQR/ABA/ACLEDA)
3. Enter payment details:
   - Amount
   - Notes (if cash)
   - Transaction reference (if bank)
4. Click **✅ Record Payment**

#### Step 3: Print
1. View invoice → Click **🖨️ Print** for professional print
2. View invoice → Click **🧾 Print Receipt** for thermal receipt

---

## 🏪 CONFIGURE YOUR COMPANY

**(Future dashboard feature)**

Set up your company details so they appear on all invoices:
- Upload company logo
- KHQR merchant ID (for QR codes)
- ABA account number
- ACLEDA account number
- Custom invoice footer text
- Custom receipt footer text

---

## 📊 EXAMPLE SCENARIOS

### Scenario 1: Local Customer - Cash Payment (KHR)
```
1. Create an invoice in KHR currency
2. Customer brings cash
3. Go to Payments → Cash → KHR currency
4. Enter amount: 2,000,000 KHR
5. Click "Record Payment"
6. Print receipt with KHQR QR code
```

### Scenario 2: Bank Transfer - KHQR
```
1. Create an invoice in KHR
2. Customer scans KHQR code
3. Customer pays via Bakong app
4. You receive notification
5. Go to Payments → Bank → KHQR
6. Enter transaction ID from Bakong
7. Click "Record Payment"
8. Invoice marked as PAID
9. Print receipt
```

### Scenario 3: ABA Bank Transfer
```
1. Create an invoice in USD
2. Customer transfers to ABA account
3. You receive confirmation
4. Go to Payments → Bank → ABA Bank
5. Enter transaction/slip number
6. Click "Record Payment"
7. Print professional invoice
```

---

## 📁 FILES YOU NEED TO KNOW

| File | Purpose |
|------|---------|
| `DASHBOARD.html` | Main UI with payment form |
| `INVOICE_PRINT_TEMPLATE.html` | Invoice print design |
| `RECEIPT_PRINT_TEMPLATE.html` | Receipt print design |
| `backend/app/models_invoice.py` | Database schema |
| `backend/app/routes_invoice.py` | API endpoints |
| `upgrade_database.py` | Database migration |

---

## 🌍 LANGUAGES & CURRENCIES

### Languages (6 total)
- English
- Spanish
- French
- German
- Portuguese
- **Khmer (ខ្មែរ)** ✨

### Currencies (6 total)
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- **KHR (Cambodian Riel)** ✨

---

## ✨ SPECIAL FEATURES

### Khmer Language Support
- UI available in Khmer
- Khmer currency (KHR) support
- Right-to-left text handling
- Local payment terminology

### Multi-Currency
- Automatic currency display on invoices
- Different currency for each invoice
- Payment currency can differ from invoice

### Manual Tax System
- ✅ No automatic tax calculation
- ✅ You decide tax per invoice
- ✅ Enter amount or percentage
- ✅ Both fields update automatically

### Professional Branding
- Company logo on invoices/receipts
- Custom footer text
- Professional color scheme
- Print-optimized fonts

---

## 🔧 TROUBLESHOOTING

### Payment Not Recording?
- ✓ Check invoice is selected
- ✓ Check amount is entered
- ✓ Check payment method is selected
- ✓ Refresh browser if needed

### Print not opening?
- ✓ Invoice must be saved first
- ✓ Browser popup blocker might be on
- ✓ Try "Print" button instead of browser print

### KHQR code not showing?
- ✓ Must be configured in Company Settings
- ✓ Check KHQR merchant ID is entered
- ✓ May require Bakong API integration (future)

---

## 📞 SUPPORT

All payment methods are configured and ready to use! If you need:
- Different bank accounts
- Logo upload
- Currency customization
- Additional payment methods

These can be added via the admin dashboard (coming soon).

---

## 🎓 LEARNING PATH

1. **Start**: Create a simple invoice
2. **Practice**: Record a cash payment
3. **Explore**: Try different payment methods
4. **Print**: Generate invoice and receipt
5. **Customize**: Add your company details

---

## ✅ READY TO USE!

Your system is now fully configured with:
- ✅ 4 payment methods (Cash, KHQR, ABA, ACLEDA)
- ✅ Beautiful invoice template
- ✅ Thermal receipt template
- ✅ Khmer language support
- ✅ KHR currency support
- ✅ Manual tax system
- ✅ Professional print features

**Start creating invoices and recording payments now!**

---

*Version 2.0 - Cambodia Localization*
*Last Updated: March 14, 2026*
