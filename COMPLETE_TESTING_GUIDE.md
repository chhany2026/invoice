# 🧪 Complete System Testing Guide

## Overview
This guide walks you through the **entire workflow** to verify all updates work correctly:
1. Make Settings changes
2. Preview the changes
3. Create an actual invoice
4. Verify settings are applied

---

## 📋 Full Workflow Test

### Step 1: Open Dashboard
**Goal:** Start the application
1. Open `DASHBOARD.html` in your browser
2. You should see the invoice creation form
3. Check the backend is running (look for green ✓ indicator)

**Expected:**
- Dashboard loads without errors
- Status bar shows API online ✓
- Invoice list loads successfully

---

### Step 2: Open Settings Panel

**Action:**
1. Click **⚙️ Settings** button (top-right)
2. Settings panel opens in new window

**Expected:**
- Settings form loads with all tabs visible
- 6 tabs appear: Company Info, Branding, Invoices, Payments, Currencies, Advanced
- All fields show either defaults or previously saved values

---

### Step 3: Make Test Changes in Settings

**Change #1: Company Name**

Location: Settings → 🏢 Company Info tab

```
Field: Company Name
Current: "Your Company Name" (or previous value)
Change to: "SOLA TECHNOLOGY CO., LTD"
```

Action:
1. Click Company Info tab
2. Edit "Company Name" field
3. Enter your actual company name
4. Click **✓ Save Company Info**
5. See green success message

**Expected:** ✅ "Settings saved successfully!"

---

**Change #2: Brand Color**

Location: Settings → 🎨 Branding tab

```
Field: Primary Color
Current: #667eea (Blue)
Change to: #e74c3c (Red)
```

Action:
1. Click Branding tab
2. Click color picker for "Primary Color"
3. Change from blue to red
4. Click **✓ Save Branding**
5. See green success message

**Expected:** ✅ "Settings saved successfully!"

---

**Change #3: Tax Rate**

Location: Settings → 📋 Invoice Settings tab

```
Field: Default Tax Rate
Current: 10%
Change to: 20%
```

Action:
1. Click Invoice Settings tab
2. Edit "Default Tax Rate" field
3. Change value to 20
4. Click **✓ Save Invoice Settings**
5. See green success message

**Expected:** ✅ "Settings saved successfully!"

---

### Step 4: View Template Preview

**Goal:** See how changes appear in invoice template

Action:
1. From Settings window, click **👁️ View Template Preview** (top-right)
2. Template Preview opens in new window
3. You should see a sample invoice

**Verify in Preview:**

Check Company Info:
- ✅ Company name shows your updated name
- ✅ Address fields populated
- ✅ Contact info displayed

Check Branding:
- ✅ Invoice header color changed to RED (#e74c3c)
- ✅ All headers, borders use new color
- ✅ Labels and highlights show red

Check Tax Rate:
- ✅ Scroll to "Totals" section
- ✅ Tax rate shows as 20%
- ✅ Tax calculation correct:
  - Subtotal: $1,500
  - Tax (20%): $300 ✓
  - Total: $1,800 ✓

**Expected:** All three changes visible and correct ✅

---

### Step 5: Refresh Preview Multiple Times

**Why:** Ensure preview consistently shows latest settings

Action:
1. In preview window, click **🔄 Refresh Preview**
2. Wait for preview to update
3. Verify same changes still showing
4. Click refresh again
5. Same result?

**Expected:** ✅ Consistent results each refresh

---

### Step 6: Switch Template Tabs

**Why:** Ensure all template types show settings

Action:
1. In preview, click **📄 Invoice (English)**
2. See company name and red color
3. Click **🧾 Receipt (English)**
4. See same company and color in receipt
5. Click **📄 Invoice (Khmer)**
6. See Khmer version with same settings

**Expected:** ✅ All tabs show your updates

---

### Step 7: Create Actual Test Invoice

**Goal:** Verify settings transfer to real invoice

Action:
1. Return to **DASHBOARD.html**
2. Scroll to "Create New Invoice"
3. Fill in form:
   - **Product Name:** "Test Product"
   - **Quantity:** 2
   - **Unit Price:** $500
   - **Customer Name:** "Test Customer"
   - **Customer Email:** your@email.com
   - **Invoice Type:** International (for wider settings)

4. Click **"+ Add Product"** to add the test product
5. Scroll down and review the form
6. Click **"✓ Create Invoice"**

**Expected:** ✅ Invoice created successfully (see confirmation)

---

### Step 8: View Generated Invoice

**Goal:** Check if settings actually applied to invoice

Action:
1. After creating invoice, look for **print button** or **download link**
2. Click to view the invoice
3. Check PDF or new window opens

**Verify in Generated Invoice:**

✅ Company Information:
```
Look for your company name:
"SOLA TECHNOLOGY CO., LTD"
Address, phone, email shown
```

✅ Branding Colors:
```
Header section should be RED (#e74c3c)
Invoice number label in red
Amount colors in red
```

✅ Product Line Items:
```
Your test products shown
Quantities match what you entered
Prices calculated correctly
```

✅ Tax Calculation:
```
Subtotal: $1,000 (2 × $500)
Tax (20%): $200 ✓
Total: $1,200 ✓
Tax rate correct!
```

✅ Currency:
```
All amounts show $ symbol
Or your selected currency
```

**Expected:** ✅ All settings visible in actual invoice!

---

### Step 9: Check Invoice in Database

**Goal:** Verify data persisted correctly

What to look for in the invoice list on Dashboard:
- New invoice appears in the list
- Correct product info shown
- Status shows correctly
- Date is today's date

**Expected:** ✅ Invoice saved and visible in list

---

### Step 10: Test Edit Flow

**Goal:** Verify you can adjust settings and see new invoices use updates

Action:
1. Go back to Settings
2. Change another setting:
   - Company Phone number
   - Or Payment Method details
   - Or Currency

3. Save the change
4. Return to Dashboard
5. Create a SECOND test invoice
6. View this new invoice

**Expected:** ✅ New invoice has updated settings, old invoice unchanged

---

## 🔄 Complete Flow Summary

```
DASHBOARD
   ↓
Click ⚙️ Settings
   ↓
SETTINGS PANEL
   ↓
Make Changes (Company, Color, Tax)
   ↓
Click ✓ Save Settings
   ↓ (Success message shows)
   ↓
Click 👁️ Preview
   ↓
TEMPLATE PREVIEW
   ↓
Click 🔄 Refresh Preview
   ↓
Verify Changes Visible (Company name, RED color, 20% tax)
   ↓
Back to DASHBOARD
   ↓
Create Invoice with Test Data
   ↓
View Generated Invoice
   ↓
Verify All Settings Applied! ✅
```

---

## ✅ Full Verification Checklist

### Settings Panel
- [ ] Opens without errors
- [ ] All 6 tabs visible and clickable
- [ ] Can edit all fields
- [ ] Save buttons work
- [ ] Success messages appear

### Template Preview
- [ ] Opens from Settings button
- [ ] Shows sample invoice
- [ ] Shows current settings in strip
- [ ] All 4 template tabs work
- [ ] 🔄 Refresh works
- [ ] Company name shows updates
- [ ] Colors show updates
- [ ] Tax calculation accurate

### Dashboard & Invoice Creation
- [ ] Form loads without errors
- [ ] Can fill in all fields
- [ ] Can add multiple products
- [ ] Create button works
- [ ] Invoice created successfully
- [ ] Appears in invoice list

### Generated Invoice
- [ ] Company name matches settings
- [ ] Colors match branding settings
- [ ] Tax rate applied correctly
- [ ] Currency symbol correct
- [ ] All product info shown
- [ ] Calculations accurate

### Settings Integration
- [ ] Settings saved to localStorage
- [ ] Settings persisted on page reload
- [ ] Multiple invoices use same settings
- [ ] Settings can be changed for new invoices

---

## 🐛 Common Issues & Fixes

### Issue: Settings saved but preview not updating
**Solution:**
1. Click 🔄 Refresh Preview button
2. Or close and reopen preview window
3. Check browser cache (Ctrl+Shift+R to clear)

### Issue: Invoice shows old company name
**Solution:**
1. Check settings were actually saved
2. Look for green success message
3. Reload dashboard page
4. Create new invoice (old invoices won't update)

### Issue: Color not changing in preview
**Solution:**
1. Verify color was saved in settings
2. Check Settings → Branding tab shows new color
3. Click Refresh Preview
4. Try different color code
5. Check browser cache

### Issue: Tax calculation wrong
**Solution:**
1. Go to Settings → Invoice Settings
2. Check "Default Tax Rate" value
3. Look at math: Subtotal × (1 + Tax%) = Total
4. Example: $1,000 × 1.20 = $1,200 ✓

### Issue: Invoice not generating
**Solution:**
1. Check backend is running (green API status)
2. Check all required fields filled (marked with *)
3. Check browser console (F12) for errors
4. Try creating simpler invoice (1 product only)

---

## 📊 What Gets Saved Where

### Browser localStorage (Client-Side)
- All Settings values
- UI Language selection
- User preferences

**Location in Code:** SETTINGS.html, DASHBOARD.html

**Persistence:** Survives page refresh, lost if clear browser data

### Server Database (Server-Side)
- Invoice data
- Receipt data  
- Customer information
- Created dates, payment status

**Location:** backend/warranty_product.db (SQLite)

**Persistence:** Permanent until deleted

### Settings File (Server-Side)
- Company information
- Branding settings
- Invoice defaults
- Payment options

**Location:** backend/instance/settings.json

**Persistence:** Saved on Settings page, persists until changed

---

## 🎯 Key Verification Points

### Point 1: Settings → Storage
```
You change: Company Name to "ABC Corp"
System does: 
  1. Save to localStorage
  2. Save to server (settings.json)
  3. Return success message ✓
```

### Point 2: Storage → Preview
```
Preview loads settings from localStorage
Shows in "Current Settings Applied" strip
Renders in sample invoice with your values ✓
```

### Point 3: Preview → Invoice
```
When you create invoice in Dashboard:
  1. Dashboard form loads your settings
  2. Company name auto-fills
  3. Tax rate auto-applies
  4. Currency defaults to your setting
  5. Generated invoice has all settings ✓
```

### Point 4: Invoice → Database
```
Invoice created with all settings:
  1. Saved to database
  2. Appears in invoice list
  3. Can be viewed, printed, downloaded
  4. Data persists permanently ✓
```

---

## 🚀 Success Criteria

✅ **PASS if:**
- All 3 test settings changes save successfully
- Template preview shows all changes
- Generated invoice has all settings applied
- No errors appear in console
- Invoices are visible in list
- Can create multiple invoices

❌ **FAIL if:**
- Settings don't save (check browser console: F12)
- Preview doesn't update
- Invoice shows old settings
- Errors appear in console
- Invoices not created
- Tax calculation wrong

---

## 🧑‍💻 For Technical Users: What's Working

**Frontend (SETTINGS.html):**
```
✅ Form rendering
✅ Input validation
✅ localStorage save/load
✅ Success messages
✅ Tab switching
```

**Frontend (TEMPLATE_PREVIEW.html):**
```
✅ Settings loading from localStorage
✅ Sample invoice rendering
✅ Color application
✅ Tax calculation
✅ Refresh functionality
```

**Frontend (DASHBOARD.html):**
```
✅ Form loading
✅ Settings integration
✅ Invoice creation
✅ List rendering
✅ Preview button
```

**Backend (routes_settings.py):**
```
✅ Settings API endpoints
✅ File saving (instance/settings.json)
✅ CORS enabled
✅ Error handling
```

**Backend (routes_invoice.py):**
```
✅ Invoice creation with date fix
✅ Company details integration
✅ Tax calculation
✅ PDF generation
```

---

## 📞 Testing Support

**If something doesn't work:**

1. **Check Backend:**
   - Make sure terminal shows "Running on http://0.0.0.0:5000"
   - If not running, backend won't save data

2. **Check Console:**
   - Press F12 in browser
   - Look for red errors
   - Check Network tab for failed requests

3. **Check Files:**
   - SETTINGS.html exists
   - TEMPLATE_PREVIEW.html exists
   - DASHBOARD.html has preview button

4. **Test Incrementally:**
   - Test settings save alone
   - Test preview refresh alone
   - Test invoice creation alone
   - Then test together

---

**Last Updated:** March 14, 2026
**Test Date:** [Your test date]
**Tester:** [Your name]
**Result:** [PASS/FAIL]

