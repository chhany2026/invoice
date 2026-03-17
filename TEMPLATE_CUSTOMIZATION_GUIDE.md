# 📋 Invoice & Receipt Template Customization Guide

## Overview

Two **clean, editable templates** have been created for you to customize:

1. **INVOICE_TEMPLATE_EDITABLE.html** - Professional invoice for formal sales billing
2. **RECEIPT_TEMPLATE_EDITABLE.html** - Thermal printer receipt for point-of-sale

Both templates include detailed comments and are ready to be personalized with your company branding.

---

## 🎨 Quick Customization Checklist

- [ ] Change primary color (#667eea → your brand color)
- [ ] Add company logo
- [ ] Update company name and details
- [ ] Customize footer text
- [ ] Adjust font if needed
- [ ] Configure payment methods display
- [ ] Set up warranty information display

---

## 📝 WHERE TO CUSTOMIZE

### 1️⃣ **PRIMARY COLOR** (Easy ⭐)

**What it affects:** Headers, borders, labels, buttons

**Location:** Find & Replace `#667eea` with your brand color

**Files:**
- `INVOICE_TEMPLATE_EDITABLE.html` - Line 20-21 (comment), then throughout
- `RECEIPT_TEMPLATE_EDITABLE.html` - Line 19-20 (comment), then throughout

**Example:**
```css
/* Change from: */
border-bottom: 3px solid #667eea;

/* To: */
border-bottom: 3px solid #e74c3c;  /* Your brand color */
```

---

### 2️⃣ **COMPANY LOGO** (Medium ⭐⭐)

**What it affects:** Company branding in header

**Three Ways to Add Logo:**

#### Option A: Base64 Image (Recommended - No External URLs)
1. Upload your logo image through the dashboard
2. The system will convert it to Base64 automatically
3. The template will display: `{{ company_logo }}`

#### Option B: Direct URL (For Cloud Images)
Find this section in template:
```html
<div class="company-logo">
    {% if company_logo %}
        <img src="data:image/png;base64,{{ company_logo }}" alt="Company Logo">
    {% else %}
        <span>🏢</span>
    {% endif %}
</div>
```

Replace with:
```html
<div class="company-logo">
    <img src="https://your-domain.com/logo.png" alt="Company Logo" style="max-width: 100%; max-height: 100%;">
</div>
```

#### Option C: Emoji Only (Simple)
Replace `<span>🏢</span>` with any emoji:
```html
<span>🏪</span>  <!-- Store -->
<span>📱</span>  <!-- Tech -->
<span>💼</span>  <!-- Business -->
<span>🎁</span>  <!-- Products -->
```

---

### 3️⃣ **COMPANY DETAILS** (Easy ⭐)

These are auto-filled from database, but you can also hardcode them.

**Location:** Look for these variables in template:
- `{{ company_name }}`
- `{{ company_address }}`
- `{{ company_city }}`
- `{{ company_phone }}`
- `{{ company_email }}`
- `{{ company_website }}`

**To hardcode (if database not available):**
```html
<h1>{{ company_name | default('Your Company Name') }}</h1>
<p>📍 121 Street, your address</p>
<p>☎ +855 (0)17 123 456</p>
<p>📧 info@yourcompany.com</p>
<p>🌐 www.yourcompany.com</p>
```

---

### 4️⃣ **FOOTER TEXT** (Very Easy ⭐)

**Location:** Bottom of template

**Invoice Footer (INVOICE_TEMPLATE_EDITABLE.html):**
```html
<div class="footer">
    {% if footer_text %}
        <p class="footer-company-text">{{ footer_text }}</p>
    {% else %}
        <p class="footer-company-text">Thank you for your business!</p>
    {% endif %}
    <p style="font-size: 11px; color: #999;">
        Invoice #{{ invoice_number }} | Generated on {{ generation_date }}
    </p>
</div>
```

**Change to:**
```html
<div class="footer">
    <p class="footer-company-text">🙏 Thank you for choosing us!</p>
    <p style="font-size: 11px; color: #999;">
        We appreciate your business | Questions? Email us anytime
    </p>
    <p style="font-size: 10px; color: #bbb;">
        © 2026 Your Company. All rights reserved.
    </p>
</div>
```

**Receipt Footer (RECEIPT_TEMPLATE_EDITABLE.html):**
```html
<div class="thank-you">Thank You!</div>

{% if footer_text %}
    <div class="footer-text">
        {{ footer_text }}
    </div>
{% else %}
    <div class="footer-text">
        <p>Please visit us again!</p>
        <p>Questions? Contact us anytime</p>
    </div>
{% endif %}

<div class="footer-meta">
    <p>Generated: {{ generation_date }}</p>
    <p>© 2026 {{ company_name }}</p>
</div>
```

**Customize to:**
```html
<div class="thank-you">សូមរំរឹង!</div>

<div class="footer-text">
    <p>ឯកសារនេះមានសុពលភាព ៣០ ថ្ងៃ</p>
    <p>សូមចូលមកវិញ!</p>
</div>

<div class="footer-meta">
    <p>ផ្តល់ឱ្យលើ: {{ generation_date }}</p>
    <p>© ២ ០ ២ ៦ Your Company Ltd.</p>
</div>
```

---

### 5️⃣ **COLORS & STYLING** (Medium ⭐⭐)

**Key Colors to Customize:**

```css
/* Main brand color */
#667eea → #your-color

/* Success (Warranty/Paid) */
#4caf50 → #your-green

/* Warning (Draft/Pending) */
#ffc107 → #your-yellow

/* Info (Issued) */
#667eea → #your-blue

/* Error (if needed) */
#f44336 → #your-red
```

**Background Colors:**
- `#f8f9fa` - Light gray backgrounds
- `#e8f5e9` - Light green (warranty)
- `#fff8e1` - Light yellow (notes)

**Text Colors:**
- `#333` - Dark text
- `#666` - Medium gray
- `#999` - Light gray

---

### 6️⃣ **FONTS** (Medium ⭐⭐)

**Current Font:**
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;  /* Invoice - clean */
font-family: 'Courier New', 'Lucida Console', monospace;        /* Receipt - fixed-width */
```

**To Change Font:**

Replace the entire font-family line with options like:
```css
/* Modern & Clean */
font-family: 'Inter', 'Roboto', 'Open Sans', sans-serif;

/* Professional & Formal */
font-family: 'Georgia', 'Garamond', serif;

/* Monospace (for receipts) */
font-family: 'Courier New', 'Courier', monospace;

/* System Default (fastest) */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

---

### 7️⃣ **PAYMENT METHODS** (Medium ⭐⭐)

**Location:** "Payment Methods" section in template

Currently displays:
- KHQR (Khmer QR Code)
- ABA (Bank Account)
- ACLEDA (Bank Account)
- Cash (with currency)

**To Customize (add/remove payment methods):**

```html
<div class="payment-methods">
    <h3>💳 Payment Methods</h3>
    <div class="payment-method-grid">
        <!-- Method 1: KHQR -->
        <div class="payment-method-item">
            <h4>🇰🇭 KHQR (Recommended)</h4>
            <p><strong>Scan with Mobile Banking:</strong> Use any KHQR-enabled app</p>
            <p><strong>QR Code:</strong> See below</p>
        </div>

        <!-- Method 2: Bank Transfer -->
        <div class="payment-method-item">
            <h4>🏦 Bank Transfer</h4>
            <p><strong>Bank:</strong> {{ bank_name }}</p>
            <p><strong>Account:</strong> {{ bank_account_number }}</p>
            <p><strong>Holder:</strong> {{ bank_account_holder }}</p>
        </div>

        <!-- Method 3: Cash -->
        <div class="payment-method-item">
            <h4>💵 Cash Payment</h4>
            <p><strong>Currency:</strong> USD / {{ cash_currency }}</p>
            <p><strong>Accepted:</strong> USD or KHR at exchange rate</p>
        </div>
    </div>

    {% if khqr_code %}
        <div class="qr-code-container">
            <p style="font-size: 12px; color: #666; margin-bottom: 10px;">KHQR Payment Code - Scan to Pay</p>
            <img src="data:image/png;base64,{{ khqr_code }}" alt="KHQR Code">
        </div>
    {% endif %}
</div>
```

---

### 8️⃣ **WARRANTY SECTION** (Easy ⭐)

**Location:** Warranty Information box

**Current Display:**
```html
<div class="warranty-section">
    <h4>✅ Warranty Information</h4>
    {% for item in warranty_items %}
        <p>• <strong>{{ item.description }}</strong><br>
           {{ item.warranty_duration }} months (until {{ item.warranty_end_date }})</p>
    {% endfor %}
</div>
```

**Customize Title & Icons:**
```html
<div class="warranty-section">
    <h4>🛡️ Product Warranty Coverage</h4>
    {% for item in warranty_items %}
        <p>📦 <strong>{{ item.description }}</strong><br>
           ⏰ Duration: {{ item.warranty_duration }} months<br>
           📅 Valid until: {{ item.warranty_end_date }}<br>
           ✨ Full replacement coverage included</p>
    {% endfor %}
</div>
```

---

### 9️⃣ **NOTES SECTION** (Easy ⭐)

**Before:**
```html
{% if notes %}
    <div class="notes-section">
        <h4>📝 Notes</h4>
        <p>{{ notes }}</p>
    </div>
{% endif %}
```

**After:**
```html
{% if notes %}
    <div class="notes-section">
        <h4>⚠️ Important Information</h4>
        <p>{{ notes }}</p>
        <p style="margin-top: 8px; font-size: 11px;">
            Please review the above information carefully before payment.
        </p>
    </div>
{% endif %}
```

---

## 🖼️ LAYOUT ADJUSTMENTS

### Receipt Width (for different paper sizes)

**Current:** 400px (standard 58-80mm thermal printer)

**For A4 Paper:** Change to 900px
```css
.receipt-container {
    max-width: 900px;  /* Changed from 400px */
}
```

**For wide receipt (100mm):** Change to 600px
```css
.receipt-container {
    max-width: 600px;
}
```

### Invoice Column Layout

**Current:** 2-column (logo + details, invoice #)

**To Change to 1-column:**
```css
.invoice-header {
    grid-template-columns: 1fr;  /* Changed from 1fr 1fr */
    gap: 20px;
}

.invoice-meta {
    text-align: left;  /* Changed from right */
}
```

---

## 🔄 SPECIAL VARIABLES (Auto-Filled)

These are automatically populated from the database:

**Invoices:**
- `{{ invoice_number }}` - INV-2026-000001
- `{{ invoice_date }}` - March 14, 2026
- `{{ due_date }}` - April 13, 2026
- `{{ customer_name }}` - Customer's name
- `{{ company_name }}` - Your company name
- `{{ currency }}` - USD, EUR, KHR, etc.
- `{{ subtotal }}` - Calculated total before tax
- `{{ tax_amount }}` - Tax amount
- `{{ grand_total }}` - Final total
- `{{ status }}` - draft, issued, paid

**Receipts:**
- `{{ receipt_number }}` - RCP-2026-000001
- `{{ receipt_date }}` - March 14, 2026
- `{{ receipt_time }}` - 14:30:45
- `{{ payment_method }}` - khqr, bank, cash
- `{{ payment_status }}` - completed, pending

---

## 💾 SAVING YOUR CUSTOMIZED TEMPLATES

### Option 1: Overwrite Originals (Simple)
```bash
# Backup originals
Copy INVOICE_PRINT_TEMPLATE.html → INVOICE_PRINT_TEMPLATE_BACKUP.html
Copy RECEIPT_PRINT_TEMPLATE.html → RECEIPT_PRINT_TEMPLATE_BACKUP.html

# Replace with customized versions
Copy INVOICE_TEMPLATE_EDITABLE.html → INVOICE_PRINT_TEMPLATE.html
Copy RECEIPT_TEMPLATE_EDITABLE.html → RECEIPT_PRINT_TEMPLATE.html
```

### Option 2: Keep Multiple Versions (Professional)
```bash
INVOICE_PRINT_TEMPLATE_DEFAULT.html      (Original)
INVOICE_PRINT_TEMPLATE_CUSTOM.html       (Your custom)
INVOICE_PRINT_TEMPLATE_KHMER.html        (Khmer version)

RECEIPT_PRINT_TEMPLATE_DEFAULT.html      (Original)
RECEIPT_PRINT_TEMPLATE_CUSTOM.html       (Your custom)
RECEIPT_PRINT_TEMPLATE_THERMAL.html      (For thermal printer)
```

---

## 🧪 TESTING YOUR CUSTOMIZATIONS

1. **Edit Template** → Save changes
2. **Create Test Invoice** in dashboard with language "en"
3. **Click Print** button
4. **Review** in browser before printing
5. **Adjust** CSS if needed
6. **Print to PDF** to verify formatting

---

## 🎯 COMMON CUSTOMIZATIONS

### Example 1: Restaurant Receipt
```html
<!-- Change header -->
<h1>🍽️ NOODLE HOUSE KHMER</h1>

<!-- Add menu items -->
<div class="receipt-section-title">Order Details</div>

<!-- Add special instructions -->
<p style="font-size: 10px; color: #666; margin-top: 10px;">
    ☎ Delivery: +855 (0)17 987 654 | Open: 10am-11pm
</p>
```

### Example 2: Electronics Store Invoice
```html
<!-- Professional branding -->
<h1 style="color: #1a73e8;">⚡ TECH SOLUTIONS CAMBODIA</h1>

<!-- Add warranty promotion -->
<div class="warranty-section">
    <h4>🛡️ Extended Warranty Available</h4>
    <p>Protect your investment with our 3-year coverage plan!<br>
       Contact us for details: service@techcam.com</p>
</div>
```

### Example 3: Khmer Language Customization
```html
<!-- Change all text to Khmer -->
<h1>ក្រុមហ៊ុន ឈឺន សូលឩン</h1>

<!-- Khmer footer -->
<p style="color: #667eea;">សូមរំរឹងដែលបានផ្តល់ឱ្យ!</p>
<p>ប្រសិនបើមានសំណួរ សូមទាក់ទងយើងម្ដងទៀត</p>

<!-- Khmer currency label -->
<p>រូបិយប័ណ្ណ: ៛ (KHR) ឬ $ (USD)</p>
```

---

## 📧 NEED HELP?

If something doesn't display correctly:

1. **Check browser console** (F12 → Console tab) for JavaScript errors
2. **Verify template variables** exist in your database
3. **Test with sample data** to ensure formatting works
4. **Use "Print to PDF"** first before printing to paper
5. **Check file encoding** is UTF-8 for special characters

---

## ✅ TEMPLATE CHECKLIST BEFORE PRODUCTION

- [ ] Logo displays correctly
- [ ] Company name and contact info accurate
- [ ] Footer text appropriate
- [ ] Colors match brand guidelines
- [ ] Font readable in print
- [ ] Payment methods correct
- [ ] Warranty section displays properly
- [ ] Works on both A4 and thermal printer
- [ ] Print preview looks good (Ctrl+P)
- [ ] Special characters (Khmer) display correctly

---

**Last Updated:** March 14, 2026  
**Template Version:** 2.0 (Customizable)  
**Status:** Ready for customization ✅
