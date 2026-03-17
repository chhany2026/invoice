# Quick Start: Khmer Language in Invoice Dashboard

## 📍 Where is the Language Selector?

**Top-right corner of the page** - Look for the flag emoji selector:
```
┌─────────────────────────────────┐
│                                 │  [🇬🇧 English]
│  Invoice Dashboard              │  [🇰🇭 Khmer]  ← HERE
│                                 │
```

---

## 🔄 How to Switch Languages

### Step 1: Click the Dropdown (top-right)
![Position: Fixed at top-right]

### Step 2: Select Your Language
- 🇬🇧 **English** - Default interface language
- 🇰🇭 **ខ្មែរ** - Khmer interface language

### Step 3: Done! ✅
- Entire interface translates instantly
- Your choice is saved automatically
- Next time you visit → remembers your choice

---

## 🌍 What Gets Translated?

### ✅ Translated Elements
- Form labels: "Customer Name" → "ឈ្មោះអតិថិជន"
- All buttons: "Create Invoice" → "បង្កើតវិក័យប័ត្រ"
- Section headers: "Dashboard" → "ផ្ទាំងគ្រប់គ្រង"
- Tab names: "Payments" → "ការបង់ប្រាក់"
- Status indicators: "Backend API" → "API ខាងក្រោយ"
- Everything in the interface!

### ✅ Preserved Elements
- Product/Company names (you enter)
- Numbers and amounts (universal)
- Email addresses (universal)
- Date formats (still work correctly)
- Currency symbols (remain as-is)

---

## 📱 Language Preference Storage

Your language choice is saved in your browser:

```
Browser Memory (localStorage)
├─ Key: "uiLanguage"
├─ Values: "en" or "km"
└─ Cleared: Only if you clear browser cache
```

**This means:**
- ✅ Works offline
- ✅ No account needed
- ✅ Persistent across sessions
- ✅ Syncs with your device

---

## 🎯 Use Cases

### Scenario 1: Khmer-Speaking User
1. Open dashboard
2. Select "ខ្មែរ" from top-right selector
3. All form labels appear in Khmer
4. Fill in invoice details
5. Click "បង្កើតវិក័យប័ត្របង់រួច" to create invoice
6. Language choice saved for next visit

### Scenario 2: English User Visiting Khmer Employee
1. User opens dashboard (defaults to English)
2. Passes device to Khmer employee
3. Employee clicks selector → chooses "ខ្មែរ"
4. Interface switches to Khmer
5. Khmer employee creates invoices
6. Both can work independently

### Scenario 3: Creating Invoices in Khmer
1. Language selector: Choose "ខ្មែរ"
2. Fill customer details (names, emails in any language)
3. All form labels in Khmer
4. Add products with Khmer labels
5. All payment options in Khmer
6. Create and print invoice
7. Printed invoice language depends on invoice settings (not UI language)

---

## 🖨️ Printing Notes

**Important:** The **invoice print language** is different from **UI language**

```
┌──────────────────────────────────────┐
│ Invoice Dashboard (Web Form)          │
│ Language: Selector at top-right       │
│ Controls: Form labels & buttons       │
├──────────────────────────────────────┤
│ When you click "Print"                │
│ ↓                                     │
│ Invoice Document (Print Template)     │
│ Language: Set in "Language" dropdown  │
│ in the form itself                    │
│                                       │
│ Languages available:                 │
│ - English (auto-prints in English)   │
│ - Khmer (auto-prints in Khmer)       │
│ - Spanish, French, German, etc.      │
└──────────────────────────────────────┘
```

**So:**
- UI Language (selector): Controls web interface only
- Invoice Language (dropdown): Controls print template

You can:
- Use Khmer interface + print English invoices ✅
- Use English interface + print Khmer invoices ✅
- Use Khmer for both ✅
- Use English for both ✅

---

## 💡 Tips & Tricks

### Tip 1: Keyboard Input
Your Khmer keyboard will work perfectly:
1. Select "ខ្មែរ" language
2. Switch your OS keyboard to Khmer (Windows/Mac)
3. Type in Khmer directly into form fields
4. Everything works seamlessly

### Tip 2: Copy-Paste Khmer Text
```
1. Have Khmer text elsewhere? Copy it
2. Paste into any form field
3. Works perfectly - no encoding issues
```

### Tip 3: Language Switch in Middle of Work
Don't worry!
- Fill form in English
- Switch to Khmer to see Khmer labels
- All your entered data stays intact
- Form still works perfectly

### Tip 4: Reset Language
1. Click selector (top-right)
2. Choose "🇬🇧 English"
3. Page updates instantly
4. Your preference is saved

---

## ❓ Frequently Asked Questions

### Q: Why is the language selector in the top-right?
**A:** Fixed position so it's always visible while you scroll and work in the form.

### Q: Does my language choice sync across devices?
**A:** No, because we store it locally in your browser to avoid needing an account. Each device saves its own preference.

### Q: Can I switch languages while filling an invoice?
**A:** Yes! Any time. Your form data is preserved. Just click the selector and choose a language.

### Q: Does the printed invoice language match the UI language?
**A:** No. You choose the invoice print language in the "Language" dropdown inside the form. This is separate from the UI language selector.

### Q: What if I want to see both English and Khmer?
**A:** Use two browser tabs:
1. Tab 1: Set to English
2. Tab 2: Set to Khmer
3. Compare translations instantly!

### Q: Can I change the Khmer translations?
**A:** Yes, if you can edit the HTML. Look for `data-km="..."` attributes and change the Khmer text.

### Q: Will this work on my phone?
**A:** Yes! Works perfectly on mobile. The language selector adapts to small screens.

### Q: Is Khmer text properly encoded?
**A:** Yes, all Khmer text uses UTF-8 Unicode. Every modern browser supports it.

---

## 🔧 Technical Details

### How Translation Works
```html
<!-- Element has both language options -->
<label data-en="Customer Name" data-km="ឈ្មោះអតិថិជន"></label>

<!-- When you select language -->
language = "km"

<!-- JavaScript updates the text -->
element.textContent = element.dataset['km']
// Result: Shows "ឈ្មោះអតិថិជន"
```

### Storage
```javascript
// Browser sets this when you choose Khmer
localStorage.setItem('uiLanguage', 'km')

// Next visit, it loads automatically
const savedLang = localStorage.getItem('uiLanguage')
```

---

## 📝 Form Translations Reference

| English | ខ្មែរ |
|---------|------|
| Customer Name | ឈ្មោះអតិថិជន |
| Email | អ៉ីមែល |
| Phone | ទូរស័ព្ទ |
| City | ក្រុង |
| Country | ប្រទេស |
| Product Name | ឈ្មោះផលិតផល |
| Unit Price | តម្លៃឯកតា |
| Quantity | បរិមាណ |
| Warranty | ការធានា |
| Currency | រូបិយប័ណ្ណ |
| Tax | ពន្ធ |
| Total | សរុប |
| Create Invoice | បង្កើតវិក័យប័ត្របង់រួច |
| Payments | ការបង់ប្រាក់ |
| Receipts | ឯកសារទទួល |
| Dashboard | ផ្ទាំងគ្រប់គ្រង |

[Full translation list in KHMER_LANGUAGE_IMPLEMENTATION.md]

---

## ✨ Summary

**Khmer language support means:**
- ✅ Full interface in Khmer
- ✅ Works offline
- ✅ Remembers your choice
- ✅ No account needed
- ✅ One-click switching
- ✅ Data always preserved

**Get started:**
1. Look at top-right corner
2. Click language selector
3. Choose "ខ្មែរ"
4. Enjoy fully translated interface!

---

*For detailed technical information, see KHMER_LANGUAGE_IMPLEMENTATION.md*
