# 🎛️ Settings Panel - User Guide

## Overview
The Settings Panel is your control center for customizing your invoice system without touching any code. Access it by clicking the **⚙️ Settings** button on the Dashboard (top-right corner).

---

## 📋 Settings Sections

### 1. 🏢 Company Information
Configure your business details that appear on invoices and documents.

**Fields:**
- **Company Name** - Your business name (appears on every invoice)
- **Company Email** - Contact email for customers
- **Phone Number** - Business phone
- **Website** - Your company website
- **Street Address** - Physical location
- **City, State, Postal Code, Country** - Complete address
- **Tax ID** - Your tax registration number (optional)

**Auto-Applied To:**
- All invoices
- All receipts
- All reports

---

### 2. 🎨 Branding & Colors
Customize the visual appearance of your invoices.

**Fields:**
- **Company Logo URL** - Link to your logo image (PNG, JPG, SVG)
- **Primary Color** - Used for headers and main elements (default: #667eea)
- **Secondary Color** - Used for accents (default: #764ba2)
- **Accent Color** - Success/positive indicators (default: #4CAF50)
- **Font Family** - Choose typography style

**Options:**
- Arial (Clean & Modern)
- Segoe UI (Professional)
- Georgia (Elegant)
- Times New Roman (Classic)

---

### 3. 📋 Invoice Settings
Control how invoices are generated and formatted.

**Fields:**
- **Invoice Prefix** - Text before invoice number (e.g., "INV" → INV-2025-001)
- **Invoice Start Number** - Starting number for auto-increment (default: 1000)
- **Default Tax Rate** - Tax percentage applied to invoices (default: 10%)
- **Payment Terms** - Days for payment (default: 30 days)
- **Invoice Terms & Conditions** - Legal text shown on invoices
- **Invoice Notes** - Additional messages for customers
- **Default Currency** - Preferred currency (USD, EUR, GBP, JPY, CAD, KHR)
- **Default Language** - Language for new invoices (English or ខ្មែរ Khmer)

**Examples:**
- Prefix "INV" + Start 1000 = Invoice numbers: INV-1000, INV-1001, etc.
- Default tax 10% = Automatically calculated on all line items
- Payment terms 30 days = Due date 30 days after invoice date

---

### 4. 💳 Payment Methods
Enable and configure payment options for customers.

**Available Methods:**
1. **💵 Cash (KHR & USD)**
   - Configure KHR and USD payment details
   - Used for direct cash transactions

2. **🇰🇭 KHQR (Bakong)**
   - Cambodia's nationwide QR payment system
   - Enter Merchant ID/Account

3. **🏛️ ABA Bank**
   - Account holder name
   - Account number

4. **🏛️ ACLEDA Bank**
   - Account holder name
   - Account number

**How Payment Methods Work:**
- Click the toggle switch to enable/disable a method
- Add account details for each enabled method
- Details appear on invoices and receipts
- Customers can see all available payment options

---

### 5. 💰 Currency Settings
Select which currencies customers can invoice in.

**Available Currencies:**
- 💵 USD - United States Dollar
- 💶 EUR - Euro
- 💷 GBP - British Pound
- 💴 JPY - Japanese Yen
- 🍁 CAD - Canadian Dollar
- 🇰🇭 KHR - Cambodian Riel *(selected by default)*

**How It Works:**
- Click currency boxes to select/deselect
- Selected currencies appear in invoice dropdown
- Customers choose currency when creating invoice
- Symbols automatically applied ($ for USD, ៛ for KHR, etc.)

---

### 6. ⚡ Advanced Settings
Fine-tune system behavior and data handling.

**Fields:**
- **Invoice Numbering Style**
  - Simple: 1, 2, 3, 4...
  - Yearly: 2026-0001, 2026-0002...
  - Monthly: 202603-001, 202603-002...

- **Timezone** - For date/time stamps
  - UTC (default)
  - Asia/Bangkok (Cambodia)
  - America/New_York
  - Europe/London
  - Asia/Tokyo

- **Decimal Places**
  - 0 - Whole numbers ($100)
  - 2 - Standard ($100.25) *(default)*
  - 3 - High precision ($100.250)

- **Date Format**
  - MM/DD/YYYY (US style)
  - DD/MM/YYYY (Europe style)
  - YYYY-MM-DD (ISO standard)

- **Enable Invoice Reminders**
  - Yes - System sends payment reminders
  - No - Reminders disabled

- **Default Warranty Duration**
  - Default months for warranty (default: 24 months)

---

## 💾 Saving Settings

### Step-by-Step:
1. Open Settings panel (⚙️ button on Dashboard)
2. Navigate to the section you want to customize
3. Make your changes in the fields
4. Click **✓ Save [Section Name]** button
5. See green success message confirming save

### Storage:
- Settings saved in browser **localStorage**
- Also backed up in **instance/settings.json** (server-side)
- Settings persist across browser sessions
- Settings apply immediately to new invoices

---

## 🔄 Resetting Settings

To restore defaults:
1. Open Settings panel
2. Go to any section
3. Click **↻ Reset** button
4. Confirm the popup
5. All settings return to defaults

⚠️ **Note:** This affects all sections, not just the current tab.

---

## 🚀 Using Your Settings

### On Dashboard:
1. Create an invoice
2. Your company name, address, and settings auto-populate
3. Tax rate auto-calculates
4. Currency dropdown shows your selected currencies
5. Payment methods appear in receipt

### On Invoices:
1. Company branding applies automatically
2. Colors match your primary/secondary colors
3. Logo displays if URL is valid
4. Terms & conditions appear at bottom
5. Payment methods listed with your account info

### On Receipts:
1. Same branding as invoices
2. Payment methods displayed
3. Company contact info included
4. Language based on your default selection

---

## 📱 Mobile Responsiveness

Settings page works on:
- Desktop computers ✅
- Tablets ✅
- Mobile phones ✅

The interface adapts to your screen size.

---

## 🔒 Data Security

- Settings stored locally in your browser AND server
- No data sent to external servers
- All payment details stay secure
- Use HTTPS for production (if deployed to web)

---

## ✅ Common Tasks

### Change Company Name
1. Settings → Company Info tab
2. Update "Company Name" field
3. Click "Save Company Info"
4. New invoices use new name

### Add Company Logo
1. Settings → Branding tab
2. Paste logo image URL in "Company Logo URL"
3. Click "Save Branding"
4. Logo appears on invoices

### Add Bank Account
1. Settings → Payment Methods tab
2. Toggle "ABA Bank" to on
3. Enter account details
4. Click "Save Payment Methods"
5. Customers see option on receipts

### Change Currency
1. Settings → Currencies tab
2. Click currency box to select
3. Click "Save Currencies"
4. Currency appears in invoice dropdown

### Update Invoice Terms
1. Settings → Invoice Settings tab
2. Edit "Invoice Terms & Conditions" box
3. Click "Save Invoice Settings"
4. Terms appear on new invoices

---

## 🆘 Troubleshooting

### Settings Not Saving
- Check internet connection
- Make sure browser allows localStorage
- Try a different browser
- Clear browser cache and try again

### Logo Not Showing
- Verify URL is correct (http:// or https://)
- Check image format (PNG, JPG, SVG)
- Try another image URL
- Image must be publicly accessible

### Settings Disappeared
- Check if using a different browser
- Check if in private/incognito mode
- Clear browser history and reload
- Click "Reset" to restore defaults

### Colors Look Different
- Colors may look different on different devices/monitors
- Try adjusting the color picker
- All hex colors (#667eea) are standard across browsers
- Save and reload page to confirm

---

## 🎯 Best Practices

✅ **Do:**
- Keep company name accurate
- Use professional colors (avoid extreme colors)
- Update payment details regularly
- Use real logo URL
- Keep terms clear and concise
- Backup your settings regularly

❌ **Don't:**
- Use fake company information
- Change settings frequently during month (causes confusion)
- Use external websites' logos
- Share payment account details with customers in system
- Set unrealistic tax rates

---

## 📞 Support

**For Issues:**
1. Check this guide for answers
2. Make sure all required fields are filled (marked with *)
3. Try resetting to defaults and reconfigure
4. Check browser console for error messages (F12)

**Keyboard Shortcuts:**
- None defined (use mouse/touchscreen)
- Save buttons: Click or press Enter on focused button

---

## 📊 Settings Structure

```
Settings
├── Company Information
│   ├── Name, Email, Phone
│   ├── Website
│   ├── Address (Street, City, State, Postal, Country)
│   └── Tax ID
├── Branding
│   ├── Logo URL
│   ├── Colors (Primary, Secondary, Accent)
│   └── Font Family
├── Invoice Settings
│   ├── Numbering (Prefix, Start Number)
│   ├── Tax Rate
│   ├── Payment Terms
│   ├── Terms & Conditions
│   ├── Notes
│   ├── Default Currency
│   └── Default Language
├── Payment Methods
│   ├── Cash
│   ├── KHQR
│   ├── ABA Bank
│   └── ACLEDA Bank
├── Currencies
│   └── USD, EUR, GBP, JPY, CAD, KHR
└── Advanced
    ├── Numbering Style
    ├── Timezone
    ├── Decimal Places
    ├── Date Format
    ├── Reminders
    └── Warranty Duration
```

---

**Last Updated:** March 14, 2026
**Version:** 1.0
