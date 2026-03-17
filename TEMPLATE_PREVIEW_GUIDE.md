# 👁️ Template Preview Guide

## Overview
The **Template Preview** page allows you to see exactly how your invoices and receipts will look **with your current settings applied**. It's the easiest way to preview changes before they're used in production.

---

## 🚀 How to Access Template Preview

### Method 1: From Dashboard
1. Open **Dashboard.html**
2. Click **👁️ Preview** button (top-right corner)
3. Template Preview opens in new window

### Method 2: From Settings Panel
1. Open **Settings.html** (or click ⚙️ Settings)
2. Click **👁️ View Template Preview** button (top-right)
3. Template Preview opens in new window

### Method 3: Direct Access
- Open **TEMPLATE_PREVIEW.html** in your browser

---

## 📋 Template Preview Features

### What You See
The preview displays a **realistic sample invoice and receipt** with:
- ✅ Your company name, address, and contact info
- ✅ Your brand colors (primary, secondary, accent)
- ✅ Your logo (if URL is configured)
- ✅ Your selected currency and tax rate
- ✅ Your payment methods
- ✅ Your invoice terms & conditions

### Tabs Available
| Tab | Shows |
|-----|-------|
| 📄 Invoice (English) | Full English invoice with all sections |
| 🧾 Receipt (English) | Compact receipt format (point-of-sale style) |
| 📄 Invoice (Khmer) | Invoice in Khmer language |
| 🧾 Receipt (Khmer) | Receipt in Khmer language |

---

## 🔄 Workflow: Edit → Preview → Confirm

### Step-by-Step Example

**You want to change your company color from blue to purple:**

1. **Edit Settings:**
   - Open Settings panel
   - Go to 🎨 Branding tab
   - Change Primary Color to purple (#764ba2)
   - Click "Save Branding"

2. **View Changes:**
   - Open Template Preview (or refresh if already open)
   - See the invoice header now appears in purple
   - Check all color references updated

3. **Confirm Design:**
   - If happy, you're done!
   - If not, go back to Settings and adjust
   - Refresh Preview to see new changes

---

## 📝 Current Settings Display

At the top of the preview, you'll see a **Settings Strip** showing:

```
📌 Current Settings Applied to Preview:

Company: Your Company Name
Primary Color: #667eea 🟦
Tax Rate: 10%
Currency: USD
```

This tells you exactly which settings are being used in the preview.

---

## 🎨 What Each Setting Affects

### Company Information Settings
- **Company Name** → Appears in header
- **Email/Phone** → Shown in contact section
- **Address** → Displayed in "Bill To" section
- **Tax ID** → Can be shown if configured

### Branding Settings
- **Logo URL** → Shows in top-left of invoice
- **Primary Color** → Headers, labels, borders
- **Secondary Color** → Accent elements
- **Font Family** → Overall typography (if supported)

### Invoice Settings
- **Tax Rate** → Auto-calculated in totals
- **Currency** → Symbol shows on all amounts
- **Terms & Conditions** → Appears at bottom
- **Invoice Notes** → Can be added to preview

### Payment Methods
- All enabled payment methods appear at bottom
- Shows bank account info
- Lists KHQR, cash, and other options

---

## 💡 Preview Tips

### Refresh After Changes
```
Settings | Make Changes | Save
   ↓
Open/Refresh Preview | See Live Changes
   ↓
Happy? | Done!
```

### Check Multiple Tabs
- View invoice in English AND Khmer
- Check receipt format for POS printing
- Verify both layouts look good

### Use Browser Zoom
- **Ctrl + Plus** - Zoom in (100% → 125% → 150%)
- **Ctrl + Minus** - Zoom out
- **Ctrl + 0** - Reset to 100%
- Helpful to see how it looks at different sizes

### Print Preview
- Click **🖨️ Print Preview** button
- See how it looks when printed
- Adjust margins if needed

---

## 📐 Sample Data in Preview

The preview uses **realistic sample data:**
- Customer: "John Smith" from "Tech Solutions Inc."
- Products: Laptop Computer ($600), Software License ($300)
- Quantities and amounts: Real calculations
- Dates: Current date and calculated due date

**This helps you see:**
- How totals calculate with your tax rate
- Currency symbol placement
- Table formatting with data
- How your terms text flows

---

## 🆘 Troubleshooting Preview

### Preview Shows Old Settings
- **Issue:** Settings were changed but preview didn't update
- **Solution:** Click **🔄 Refresh Preview** button
- Also close and reopen the window

### Logo Not Showing
- **Issue:** Logo placeholder still shows
- **Cause:** URL might be incorrect or inaccessible
- **Solution:** Check URL in Settings → Branding
- Verify image is publicly accessible

### Colors Look Different
- **Issue:** Colors don't match your settings
- **Cause:** Browser cache
- **Solution:** Hard refresh (Ctrl + Shift + R)
- Check color code in settings

### Text Overlapping
- **Issue:** Company name overlaps with other info
- **Cause:** Company name is very long
- **Solution:** Try shorter company name
- Or check font setting

---

## 🖨️ Printing From Preview

### How to Print
1. Open Template Preview
2. Select the template tab you want
3. Click **🖨️ Print Preview** button
4. Or use **Ctrl + P** in browser
5. Select printer and print!

### Print Tips
- **Layout:** Choose "Landscape" for wider invoices
- **Margins:** Set to "None" or "Minimal"
- **Scale:** Keep at 100%
- **Paper:** Use white 8.5" × 11" or A4

---

## 💻 Live Editing Workflow

### Best Practice for Customization

**Session 1: Design Phase**
```
Settings → Branding → Set colors
         → Company → Add details
Preview  → Check appearance
         → Adjust until happy
```

**Session 2: Test Phase**
```
Dashboard → Create test invoice
         → Generate receipt
Preview   → Compare to template
         → Make final tweaks
```

**Session 3: Production**
```
Settings → Lock in final settings
Dashboard → Start creating real invoices
```

---

## 🎯 Common Preview Scenarios

### Scenario 1: Rebranding
You want to change from blue company to red:

1. Settings → Branding
2. Change Primary Color: #667eea → #e74c3c
3. Change Secondary Color: #764ba2 → #c0392b
4. Click Save Branding
5. Open Preview (or Refresh)
6. See all invoices now in red theme
7. Print test to check on paper

### Scenario 2: Adding Logo
You got a company logo:

1. Settings → Branding
2. Enter Logo URL: https://your-company.com/logo.png
3. Click Save Branding
4. Open Preview
5. See logo in top-left corner
6. Verify it doesn't cover company name
7. Adjust logo URL if needed

### Scenario 3: Adjusting Tax Rate
You're in a different tax jurisdiction:

1. Settings → Invoice Settings
2. Change Tax Rate: 10% → 20%
3. Click Save Invoice Settings
4. Open Preview
5. See totals recalculate automatically
6. Check that tax amount is correct
7. ($1,500 subtotal + 20% = $1,800 total)

### Scenario 4: Multi-Language Check
You serve English and Khmer customers:

1. Open Preview
2. View 📄 Invoice (English) tab
3. Check all text displays correctly
4. Switch to 📄 Invoice (Khmer) tab
5. Verify Khmer text layout
6. Both should look professional

---

## ✅ Pre-Production Checklist

Before using invoices in production, verify in Template Preview:

- [ ] Company name spelled correctly
- [ ] Address is accurate
- [ ] Phone/email display properly
- [ ] Logo URL works and looks good
- [ ] Colors match your brand guidelines
- [ ] Tax rate is correct for your jurisdiction
- [ ] Currency symbol is correct
- [ ] Payment methods are listed
- [ ] Terms & conditions are clear
- [ ] Both English and Khmer look good
- [ ] Receipt format is appropriate
- [ ] All text is readable when printed

---

## 🔐 Data Privacy Note

- **Preview is 100% local** - No data sent to server
- **Only displays sample data** - Not real customer info
- **Settings loaded from browser** - From your localStorage
- **Safe to print/share** - Contains no sensitive data

---

## 🚀 Next Steps After Preview

Once you're happy with the preview:

1. ✅ **Close Preview** - Return to Dashboard
2. ✅ **Create Invoices** - Use the dashboard form
3. ✅ **Generate Receipts** - Check actual output
4. ✅ **Compare** - How does real invoice compare to preview?
5. ✅ **Make Final Adjustments** - If needed
6. ✅ **Go Live** - Start using in production!

---

## 📞 Support

**Common Questions:**

Q: Can I edit preview directly?
A: No, preview is read-only. Edit in Settings panel instead.

Q: Does preview update automatically?
A: No, click "Refresh Preview" to see latest settings.

Q: Can I save preview as PDF?
A: Yes! Use Ctrl+P → "Save as PDF" in print dialog.

Q: How often should I use preview?
A: Use every time you change branding or business info.

---

**Pro Tip:** Keep Template Preview open while editing Settings. When you save settings in one window, switch to Preview window and click Refresh to instantly see the changes!

---

**Last Updated:** March 14, 2026
**Version:** 1.0
