# Invoice & Receipt System - User Guide

## Table of Contents

1. [Quick Start](#quick-start)
2. [Creating Invoices](#creating-invoices)
3. [Managing Payments](#managing-payments)
4. [Generating Receipts](#generating-receipts)
5. [View Reports](#view-reports)
6. [Global Features](#global-features)
7. [FAQ & Troubleshooting](#faq--troubleshooting)

---

## Quick Start

### First-Time Setup (5 minutes)

1. **Open the Application**
   - Launch Warranty Product System
   - Go to **Settings** → **Company Information**

2. **Enter Company Details**
   - Company Name
   - Address
   - Contact Information
   - Tax ID / VAT Number
   - Logo (optional)

3. **Configure Default Settings**
   - Default Currency (USD, EUR, GBP, etc.)
   - Default Language (English, Spanish, French, etc.)
   - Timezone (Auto-detected)
   - Tax Rate for your region

4. **Test with Sample Invoice**
   - Go to **Point of Sale** tab
   - Create a test invoice
   - Record a test payment

---

## Creating Invoices

### Step 1: Start New Invoice

```
Click: Point of Sale → "+ New Invoice"
```

**Invoice details auto-filled:**
- Invoice Number: INV-2026-001234 (auto-generated)
- Date: Today's date
- Currency: Your default (e.g., USD)

### Step 2: Select Customer

**Option A: Existing Customer**
- Click "🔍 Search Customer"
- Type customer name or email
- Click to select

**Option B: New Customer**
- Click "+ Add Customer"
- Enter:
  - Name
  - Email
  - Phone
  - Address
  - City / Country
- Click "Save"

### Step 3: Add Line Items

**Method 1: Scan Barcode**
- Click "📱 Scan Barcode"
- Point scanner at product barcode
- Item auto-added to invoice
- Enter quantity if needed

**Method 2: Search Product**
- Click "🔍 Search Product"
- Type product name (e.g., "iPhone 15")
- Click product to add
- Quantity defaults to 1

**Method 3: Manual Entry**
- Click "+ Add Item"
- Enter product details:
  - Product Name
  - Quantity
  - Unit Price
  - Warranty Duration (optional)
- Click "Add"

### Step 4: Review Items

Each item shows:
- ✓ Product name
- ✓ Quantity
- ✓ Unit price
- ✓ Warranty info (e.g., "12mo included")
- ✓ Line total

**To edit an item:**
- Click item → "✏️ Edit" → Change details → "Save"

**To remove an item:**
- Click item → "🗑️ Remove"

### Step 5: Apply Discounts & Tax

**Line-Level Discount:**
- Click item → "Discount" field → Enter amount
- Example: $25.00 for bulk discount

**View Summary:**
```
Subtotal:        $1,289.96
Tax (8%):        $103.20    (auto-calculated)
Discount:        -$25.00
Shipping:        $0.00
────────────────────────
TOTAL:           $1,368.16
```

### Step 6: Add Notes (Optional)

**Invoice Notes:**
- Special customer requests
- Delivery instructions
- Gift message

**Internal Notes:**
- Staff-only notes
- Special handling
- Commission info

---

## Managing Payments

### Recording Full Payment

```
Invoice Amount: $1,368.16
Payment Status: Pending
```

**Step 1: Select Payment Method**

Click one of:
- 💳 **Card** (Visa, Mastercard, Amex)
- 💵 **Cash**
- ✓ **Check**
- 🏦 **Bank Transfer**
- 📱 **Mobile Pay**

### Step 2: Process Payment

**For Card:**
1. Press "💳 Card"
2. Terminal/POS reader processes payment
3. Enter transaction ID when complete
4. Click "✓ Confirm Payment"

**For Cash:**
1. Press "💵 Cash"
2. Count cash received
3. Amount defaults to invoice total
4. Click "✓ Mark Paid"

**For Other Methods:**
1. Press corresponding button
2. Enter payment reference
3. Amount can be partial
4. Click "✓ Record Payment"

### Step 3: Verify Payment Status

After recording payment, invoice shows:
```
Status: ✓ PAID
Amount Paid: $1,368.16
Outstanding: $0.00
Payment Method: Cash
Payment Date: 13 Mar 2026 20:30
```

### Partial Payments

**Scenario:** Customer pays some, balance later

```
Invoice: $1,000.00
Payment 1: $600.00 (Cash)
Status: ⏳ PARTIAL PAYMENT
Outstanding: $400.00

Payment 2: $400.00 (Check)
Status: ✓ PAID
Outstanding: $0.00
```

**To record:**
1. Click "💳 Payment"
2. Enter amount: $600.00
3. Click "Record Partial Payment"
4. Same process for second payment

### Refunds

**Scenario:** Customer returns item

**Steps:**
1. Open original invoice
2. Scroll to "Payments" section
3. Click payment to refund
4. Click "⤴️ Refund"
5. Enter:
   - Refund amount: $1,368.16
   - Reason: "Return / Customer requested"
6. Click "✓ Process Refund"

**Result:**
```
Status: Refunded
Amount Paid: $0.00
Outstanding: $1,368.16
```

---

## Generating Receipts

### Step 1: Invoice Must Be Paid

```
Invoice Status: ✓ PAID (required)
If Status: "Draft" or "Pending Payment" → Cannot generate receipt yet
```

### Step 2: Generate Receipt

Click **🧾 Generate Receipt**

**Choose Format:**
- 📄 **PDF** - Email to customer
- 🖨️ **Thermal (58mm)** - Small thermal printer
- 🖨️ **Thermal (80mm)** - Standard thermal printer
- 📧 **Email** - Digital delivery

### Step 3: For Thermal Printer

**Preview Receipt (on screen)**
- Shows all details
- Invoice number
- Customer info
- Items purchased
- Total amount paid
- Payment method
- Warranty information
- QR code for warranty lookup

**Click 🖨️ Print**
- Receipt prints on thermal printer
- Shows in about 3 seconds
- Heat-sensitive paper, legible for 1+ year

### Step 4: For Email Receipt

**Steps:**
1. Select "📧 Email" format
2. Verify customer email
3. Optional: Add custom message
   - "Thank you for your purchase"
   - "Your warranty is now active"
4. Click "📧 Send Email"

**Customer receives:**
- Professional HTML email
- PDF attachment of receipt
- Warranty details
- QR code link to warranty info
- Customer portal access link

**Tracking:**
- ✓ Email sent at: 13 Mar 2026 20:30:45
- 👁️ Email opened at: 13 Mar 2026 20:32:15
- 🔗 Warranty link clicked: Yes (13 Mar 2026 20:32:30)

### Step 5: WhatsApp/SMS Option

**Available for:**
- 📱 WhatsApp receipt
- 📲 SMS receipt (text)

**WhatsApp Example:**
```
Hi John! 👋

Your purchase receipt is ready:
INV-2026-001234

Items: iPhone 15 Pro, AppleCare+
Total: $1,368.16
Payment: Received ✓

Check your warranty:
[QR Code]
https://warranty.local/lookup/SN-2024-001234

Valid until: 13 Mar 2028

Questions? Reply to this message or
contact support@company.com
```

---

## View Reports

### Sales Dashboard

**Path:** 📊 Reports Tab

**Today's Performance:**

```
Total Sales:        $12,456.78  ↑ 12.3%
Invoices Created:   34          ↑ 5 more
Payments Received:  $12,100.00  ✓ 97%
Outstanding:        $356.78     ⚠️ 2.8%
```

### Top Products (Today)

| Product | Sold | Revenue | Warranties |
|---------|------|---------|-----------|
| iPhone 15 Pro | 12 | $11,999.88 | 12 |
| AppleCare+ 24mo | 18 | $4,499.82 | 18 |
| MacBook Pro | 3 | $5,999.97 | 3 |
| iPad Air | 5 | $2,999.95 | 5 |

### Payment Methods

| Method | Amount | % | Count |
|--------|--------|---|-------|
| 💳 Card | $9,850.00 | 79% | 26 |
| 💵 Cash | $2,250.00 | 18% | 7 |
| ✓ Check | $356.00 | 3% | 1 |

### Date Range Reports

**Select Dates:**
1. Click "From:" date picker
2. Select start date (e.g., Mar 1, 2026)
3. Click "To:" date picker
4. Select end date (e.g., Mar 13, 2026)
5. Click "📊 Generate Report"

**Generate/Export:**

Click buttons:
- 📊 **View Report** - On-screen display
- 📥 **Export Excel** - .xlsx file
- 📧 **Email Summary** - Send to manager
- 📄 **PDF Report** - Download PDF

### Customer Purchase History

**Path:** Customer Info → "📜 Purchase History"

Shows all invoices for customer:

```
John Doe - Purchase History

INV-2026-001234  13 Mar 2026  $1,368.16  ✓ PAID    2 warranties
INV-2026-001230  8 Mar 2026   $899.99    ✓ PAID    1 warranty
INV-2026-001220  1 Mar 2026   $2,450.00  ⏳ PENDING (due 31 Mar)
INV-2026-001200  15 Feb 2026  $599.99    ✓ PAID    1 warranty

Total Spent: $5,318.13
Active Warranties: 4
```

Click invoice → View/Print/Email

---

## Global Features

### 1. Multi-Currency Support

**What it does:** Handle different currencies with automatic conversion

**How to use:**

```
Invoice Creation:
1. Click "Currency" dropdown
2. Select: USD, EUR, GBP, JPY, AUD, etc.
3. Price fields auto-convert using live rates
4. Customer sees their local currency
```

**Example:**
```
Product Price: $999.99 USD
When customer selects EUR:
Converted: €920 EUR (at today's rate 0.92)
```

**Setting Default:**
- Settings → Company Info → Default Currency: USD
- All new invoices use this unless changed

### 2. Multi-Language Support

**Available Languages:**
- English (EN)
- Spanish (ES)
- French (FR)
- German (DE)
- Italian (IT)
- Portuguese (PT)
- Russian (RU)
- Chinese - Simplified (ZH-CN)
- Japanese (JA)
- Arabic (AR)

**How to use:**

```
Invoice Creation:
1. Click "Language" dropdown
2. Select: English, Spanish, French, etc.
3. Receipt prints in selected language
4. Customer receives email in their language
```

**Receipt in Spanish Example:**
```
┌─────────────────────────────┐
│  RECIBO                     │
│  Número: REC-2026-001234   │
│                             │
│  CLIENTE                    │
│  Juan García                │
│                             │
│  ARTÍCULOS                  │
│  iPhone 15 Pro    $999.99  │
│                             │
│  TOTAL           $1,368.16 │
│                             │
│  GARANTÍA ACTIVADA ✓       │
│  Válido hasta: 13 mar 2028 │
└─────────────────────────────┘
```

### 3. Regional Tax Rules

**How it works:**

Tax calculated automatically based on customer location

```
Customer: San Francisco, CA
Tax Rate: 8.0%
Amount: $1,000.00
Tax: $80.00

vs.

Customer: Austin, TX
Tax Rate: 8.25%
Amount: $1,000.00
Tax: $82.50
```

**Supported Regions:**

**USA:** 50 states (all have different rates)
**Europe:** VAT (20% standard, 5-10% reduced)
**Others:** Canada, Australia, India, Singapore, etc.

**How configured:**
- During invoice creation, system detects customer location
- Applies correct tax rate automatically
- Can manually override if needed (for special cases)

### 4. Timezone Support

**What it does:** All times show in your local timezone

**Example:**
```
Headquarters: New York (EST)
Invoice created: 13 Mar 2026 20:30:15 EST

Branch in Tokyo (JST):
Same invoice shows: 14 Mar 2026 09:30:15 JST
(9 hours ahead)

Receipt timestamp in Tokyo employee's language:
"発行日: 14 Mar 2026 09:30:15 JST"
```

**Default Timezone:**
- Settings → Company Info → Timezone
- Auto-detects from your location
- Can manually set for each location/user

---

## FAQ & Troubleshooting

### General Questions

**Q: Can I edit an invoice after creating it?**
A: 
- ✓ While in DRAFT status: Yes, edit anything
- ✗ After ISSUED: No changes allowed (prevents fraud)
- To modify: Cancel and create new invoice

**Q: What happens to warranty when invoice is created?**
A: Warranties auto-create for items with warranty info
- iPhone 15 (12mo): 1 warranty created
- AppleCare+ (24mo): Extends first warranty to 24mo
- Serial numbers auto-populated
- Customer immediately has access

**Q: Can customer see their receipt online?**
A: Yes!
- Email receipt includes secure link
- QR code links to warranty page
- Shows invoice & warranty details
- Printable from home

**Q: How long before payment is reflected?**
A: Immediate
- Card: Instant (when terminal approves)
- Cash: Instant (when you record)
- Check: Instant in system (verify bank clearance)
- Bank transfer: When bank processes (1-3 days)

---

### Invoices

**Q: Invoice number already exists - what's wrong?**
A: System should prevent duplicates
- Manual conflict: Contact support
- Auto-numbering may need reset
- Go to Settings → Reset Invoice Sequence

**Q: Can I print invoice before payment?**
A: Yes!
- Invoice prints/emails anytime
- "Invoice" document (business use)
- Receipt only after payment
- Receipt includes warranty info

**Q: How to handle returns/refunds?**
A: Use Refund feature
1. Open original invoice
2. Click "⤴️ Refund"
3. Select payment to refund
4. Enter reason
5. Click "Process"
- Creates credit memo
- Updates warranty status if applicable

---

### Payments

**Q: Customer paid but invoice shows unpaid?**
A: Verify payment was recorded
1. Open invoice
2. Scroll to "Payments" section
3. Check if payment is listed
4. If missing: Click "Record Payment" to add
5. Payment must match invoice amount (or be marked partial)

**Q: Can I accept multiple payment methods?**
A: Yes!
1. Record partial payment (e.g., $500 cash)
2. Click "Still owed: $868.16"
3. Record second payment (e.g., $368.16 card)
4. Invoice auto-marks as PAID when total matches

**Q: What if I charge wrong amount?**
A: Use refund + new payment
1. Refund incorrect payment
2. Record correct amount
3. All tracked in payment history

---

### Receipts

**Q: Receipt didn't print - printer offline!**
A: 
1. Check printer is connected
2. Load thermal paper
3. Click 🖨️ Print again
4. Or email receipt to print later

**Q: Receipt formatting looks wrong**
A: Common fixes:
- Thermal 58mm is narrow format (narrow products)
- Thermal 80mm is standard (recommended)
- PDF format always looks correct
- Try emailing PDF instead

**Q: Customer lost receipt - can they get another copy?**
A: Yes, multiple ways:
1. Check email for original receipt
2. Click invoice → "🖨️ Print Receipt" again
3. Customer portal access (ask for email)
4. Call support for reprint

**Q: How long does receipt stay valid?**
A: Forever in system
- Print reprints anytime
- Warranty QR codes never expire
- Receipt proves purchase for warranty claims

---

### Global Features

**Q: Currency shows wrong conversion rate**
A:
- Rates update daily from API
- Manual rates as fallback
- Wait 1 hour for new rates
- Or check with different currency pair

**Q: Can I charge in customer's currency?**
A: Yes! Two options:
1. Invoice in customer currency (system converts for you)
2. Customer pays online (auto currency detection)
3. Your company receives payment in default currency

**Q: Receipt not in correct language**
A:
1. Open invoice
2. Check "Language" field
3. If wrong, click Edit → Change Language
4. Regenerate receipt

**Q: Tax is wrong for my region**
A:
1. Settings → Tax Rules
2. Check your region is listed
3. If missing: Manually add rate
4. Contact support to add to database

---

### Reporting

**Q: Sales report showing wrong totals**
A:
1. Verify date range
2. Check if invoices have status "Draft" (excluded from reports)
3. Only ISSUED/PAID invoices count
4. Refresh page

**Q: Can't export to Excel**
A:
1. Check browser allows downloads
2. Try PDF export instead
3. Copy/paste table to Excel
4. Contact support for tech issues

**Q: Where are old invoices?**
A:
1. Reports → Customer History → Select customer
2. Or Reports → Date Range → Adjust dates
3. All invoices archived in system
4. Searchable by date/customer/amount

---

## Tips & Best Practices

### ✅ DO

- **Create invoice for EVERY sale** (required for warranty)
- **Add warranty duration** when appropriate
- **Record payment immediately** (prevents "lost payment" issues)
- **Email receipt** for digital paper trail
- **Regular backups** of system (esp. invoices)
- **Review daily report** for trends

### ❌ DON'T

- **Never modify paid invoices** (creates audit trail issues)
- **Don't skip warranty entry** (customer loses coverage)
- **Avoid manual number entry** (use auto-numbering)
- **Never delete invoices** (always cancel instead)
- **Don't mix currencies** without understanding

---

## Keyboard Shortcuts

```
F2          - New Invoice
F3          - Search Product
F4          - Search Customer
F5          - Refresh Report
Ctrl+P      - Print Current
Ctrl+E      - Email Receipt
Ctrl+S      - Save Invoice
Escape      - Close Dialog
Enter       - Confirm / Submit
```

---

## Contact Support

**🆘 Need Help?**

- Email: support@company.com
- Phone: +1-800-WARRANT
- Chat: In-app chat button
- Video Training: https://company.com/training
- Documentation: https://company.com/docs

---

## Version & Updates

**Current Version:** 1.0.0

**Last Updated:** 13 Mar 2026

**Next Update:** Quarterly (automatic)

---

**Happy invoicing! 📊** 🚀
