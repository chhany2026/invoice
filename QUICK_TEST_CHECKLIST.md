# 🧪 QUICK TEST CHECKLIST

## 5-Minute Complete System Test

### Phase 1: Setup (1 min)
```
□ Backend running? (Terminal shows "Running on http://0.0.0.0:5000")
□ Dashboard loads? (Open DASHBOARD.html)
□ API online? (Green ✓ indicator visible)
```

### Phase 2: Settings Changes (1 min)
```
□ Click ⚙️ Settings button
□ Settings panel opens in new window
□ Go to 🏢 Company Info tab
□ Change Company Name → "TEST COMPANY"
□ Click ✓ Save Company Info → ✅ Success!
```

### Phase 3: Template Preview (1 min)
```
□ In Settings, click 👁️ View Template Preview
□ Preview window opens showing sample invoice
□ Look at dark blue box with test settings
□ Scroll down to invoice preview
□ Verify: Company name = "TEST COMPANY" ✅
```

### Phase 4: Create Test Invoice (1.5 min)
```
□ Switch back to Dashboard window
□ Scroll down to "Create New Invoice"
□ Fill form:
  □ Product Name: "TEST"
  □ Quantity: "1"
  □ Unit Price: "100"
  □ Customer Name: "Test"
□ Click "✓ Create Invoice"
□ Wait for success message
```

### Phase 5: Verify Invoice (0.5 min)
```
□ Look at invoice list (should show new invoice)
□ Click on invoice to view/print
□ Check header: "TEST COMPANY" appears ✅
□ Check calculations correct
□ Check currency/tax applied
```

---

## Result
- ✅ **ALL PASS:** Settings → Preview → Invoice working perfectly!
- ❌ **FAIL:** Note which step failed (see troubleshooting below)

---

## 🐛 Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Settings don't save | Reload page (F5), try again |
| Preview old data | Click 🔄 Refresh button |
| Invoice list empty | Reload Dashboard (F5) |
| No backend API | Restart backend: `cd backend; python start_dev.py` |
| Color/tax not applied | Check browser cache: Ctrl+Shift+R |

---

## 📊 Detailed Test Scenarios

### Test 1: Company Name Change
```
Settings → Company Name = "ABC CORP"
       ↓
Save ✅
       ↓
Preview → Shows "ABC CORP" ✓
       ↓
Invoice → Shows "ABC CORP" ✓
```
**Status:** ✅ PASS / ❌ FAIL

---

### Test 2: Color Change
```
Settings → Primary Color = RED (#e74c3c)
       ↓
Save ✅
       ↓
Preview → Header is RED ✓
       ↓
Invoice → Header is RED ✓
```
**Status:** ✅ PASS / ❌ FAIL

---

### Test 3: Tax Rate Change
```
Settings → Tax Rate = 20%
       ↓
Save ✅
       ↓
Preview → Shows 20% calculation ✓
       ↓
Invoice → Math correct (1000 + 20% = 1200) ✓
```
**Status:** ✅ PASS / ❌ FAIL

---

### Test 4: Multi-Language
```
Dashboard → Click language selector
       ↓
Change to Khmer ខ្មែរ
       ↓
Dashboard text changes ✓
       ↓
Settings still work ✓
       ↓
Preview still work ✓
```
**Status:** ✅ PASS / ❌ FAIL

---

## Before / After Comparison

### Before Testing
```
Dashboard     SETTINGS      PREVIEW      INVOICE
=========     ========      =======      =======
✓ Form        ✗ Missing     ✗ Missing    ✓ Works
✓ Created     (NEW)         (NEW)        ✓ Generated
```

### After Testing
```
Dashboard     SETTINGS      PREVIEW      INVOICE
=========     ========      =======      =======
✓ Form        ✓ Saves       ✓ Shows      ✓ Applied
✓ Links       ✓ Updates     ✓ Refreshes  ✓ Matches
```

---

## Data Flow Verification

```
STEP 1: YOU CHANGE SETTINGS
├─ Input: Company Name = "TEST"
├─ Process: Form submission
└─ Output: ✅ Success message

STEP 2: SETTINGS SAVED
├─ Frontend: localStorage updated
├─ Backend: settings.json updated  
└─ Verify: Reload page, value persists

STEP 3: PREVIEW SHOWS CHANGES
├─ Load: localStorage read
├─ Render: Sample invoice with values
└─ Display: "TEST" visible in preview

STEP 4: INVOICE CREATED
├─ Form: Pulls settings
├─ Database: Stores with settings
└─ Generate: Invoice shows "TEST"

RESULT: ✅ Full integration working!
```

---

## Windows Setup

**Recommended Browser Layout:**
```
┌─────────────────────────────────────┐
│ DASHBOARD.html (Main)               │
│ - Invoice form                      │
│ - Click ⚙️ Settings →               │
│                                     │
├─────────────────────────────────────┤
│ SETTINGS.html (New window)          │
│ - Make changes                      │
│ - Click 👁️ Preview →               │
│                                     │
├─────────────────────────────────────┤
│ TEMPLATE_PREVIEW.html (New window)  │
│ - See changes instantly             │
│ - Click 🔄 Refresh to update        │
└─────────────────────────────────────┘
```

**Workflow Tip:** 
Arrange windows so you can see Dashboard and Settings side-by-side. Makes workflow faster!

---

## Success Indicators

### ✅ Settings Working
- [ ] Form loads all fields
- [ ] Can edit without errors
- [ ] Save button works
- [ ] Green success message appears
- [ ] Values persist on reload

### ✅ Preview Working
- [ ] Opens from Settings button
- [ ] Shows sample invoice
- [ ] Shows current settings at top
- [ ] Refresh button updates display
- [ ] All 4 template tabs work

### ✅ Invoice Working
- [ ] Dashboard loads settings
- [ ] Form uses company name/tax/currency
- [ ] Invoice creates successfully
- [ ] Generated invoice has all settings
- [ ] Appears in invoice list

### ✅ Full Integration Working
- [ ] Settings changes → Preview updates
- [ ] Preview shows → Invoice creates with same
- [ ] No errors in browser console
- [ ] No errors in backend terminal
- [ ] Multiple invoices work

---

## Test Results Template

```
Date: _______________
Tester: ______________

🧪 PHASE 1: Setup
□ Backend running    ✓ / ✗
□ Dashboard loads    ✓ / ✗
□ API online         ✓ / ✗

🎨 PHASE 2: Settings
□ Opens              ✓ / ✗
□ Can edit           ✓ / ✗
□ Saves              ✓ / ✗

👁️ PHASE 3: Preview
□ Opens              ✓ / ✗
□ Shows changes      ✓ / ✗
□ Refreshes          ✓ / ✗

📄 PHASE 4: Invoice
□ Creates            ✓ / ✗
□ Shows settings     ✓ / ✗
□ In list            ✓ / ✗

📊 PHASE 5: Integration  
□ Settings → Preview ✓ / ✗
□ Settings → Invoice ✓ / ✗
□ No errors          ✓ / ✗

OVERALL RESULT: 
[ ] ✅ ALL TESTS PASS
[ ] ⚠️ PARTIAL PASS (note issues)
[ ] ❌ CRITICAL FAILURE (see notes)

Notes:
_________________________________
_________________________________
```

---

## 🎯 Testing Goals

✅ **Primary Goal:**
Verify that Settings changes are applied to real invoices

✅ **Secondary Goals:**
- Confirm Template Preview reflects settings
- Ensure data persistence
- Check multi-language support
- Verify calculations (tax, total)

✅ **Success Metrics:**
- 100% of 5 test phases complete
- 0 errors in browser console
- Settings visible in generated invoices
- All buttons/links functional

---

**Version:** 1.0
**Last Updated:** March 14, 2026
**Status:** Ready for Testing
