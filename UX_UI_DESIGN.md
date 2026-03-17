# Warranty Product System - UX/UI Design

## Design Philosophy

- **User-Centric**: Minimal clicks to access warranty information
- **QR-First**: Scanning QR codes is the primary interaction
- **Clear Information**: Essential warranty details at a glance
- **Professional**: Corporate appearance with blue/white theme
- **Accessible**: Large buttons, clear text, high contrast

---

## Color Palette

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | #0066CC | Headers, buttons, links |
| Dark Blue | #003366 | Text, borders |
| Light Blue | #E6F2FF | Backgrounds, hover states |
| Success Green | #00AA00 | Active status, confirmations |
| Warning Orange | #FF9900 | Expiring warranties |
| Danger Red | #CC0000 | Expired, critical alerts |
| Neutral Gray | #F5F5F5 | Secondary backgrounds |
| Text Black | #1A1A1A | Main text |
| Text Gray | #666666 | Secondary text |

---

## Typography

- **Header**: Segoe UI / Arial, Bold, 24px
- **Section Title**: Segoe UI / Arial, Bold, 18px
- **Label**: Segoe UI / Arial, Regular, 12px
- **Body Text**: Segoe UI / Arial, Regular, 11px
- **Monospace**: Courier New, Regular, 10px (Serial numbers, IDs)

---

## Main Application Window

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Warranty Product Management System                              [_◻⊠] [×]    │
╠══════════════════════════════════════════════════════════════════════════════╣
│  📱 Scan QR Code  │  🔍 Serial #: [________________]  [Search]  [|➤]       │
├──────────────────────────────────────────────────────────────────────────────┤
│  ║ Warranties  ║ Products  ║ Customers  ║  [≡ Menu]                         │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─ WARRANTY RECORDS ─────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  [+ Create Warranty] [Refresh]                                    │    │
│  │                                                                     │    │
│  │  ┌─────────────────────────────────────────────────────────────┐  │    │
│  │  │ Serial # │ Product │ Customer │ Expiry │ Status │ Price │  │  │    │
│  │  ├─────────────────────────────────────────────────────────────┤  │    │
│  │  │ SN12345  │ iPhone  │ John Doe │ Jan 25│Active │ $999  │  │  │    │
│  │  │ SN12346  │ Galaxy  │ Jane Sm. │ Jun 24│Active │ $899  │  │  │    │
│  │  │ SN12347  │ MacBook │ Bob J.   │ Feb 26│  ⚠️   │$1999 │  │  │    │
│  │  │ SN12348  │ iPad    │ Alice W. │ Dec 23│ ❌    │ $599  │  │  │    │
│  │  └─────────────────────────────────────────────────────────────┘  │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Tab 1: Warranties Management

### Main Warranty View
```
┌─────────────────────────────────────────────────────────────────────┐
│ WARRANTI ES                                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Search & Filter:                                                   │
│  ┌────────────────────────────────────────────────────────────┐    │
│  │ 🔍 Search Serial/QR: [_________________________________]    │    │
│  │                                                             │    │
│  │ Filter: ☑ Active  ☐ Expired  ☐ Claimed  ☐ Transferred    │    │
│  │         Sort: [↨ Expiry Date ▼]                           │    │
│  └────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  Quick Actions:  [+ New Warranty] [Bulk Import] [Export CSV]       │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │ Serial Number         │ Status     │ Customer │ Expiry   │      │
│  ├──────────────────────────────────────────────────────────┤      │
│  │ SN-2024-001234       │✓ ACTIVE   │ John Doe │ 25 Jan 26 │      │
│  │ SN-2024-001235       │✓ ACTIVE   │ Jane Sm. │ 15 Mar 26 │      │
│  │ SN-2024-001236       │⚠ EXP SOON │ Bob J.   │ 05 Apr 26 │      │
│  │ SN-2024-001237       │✗ EXPIRED  │ Alice W. │ 10 Dec 25 │      │
│  │ SN-2024-001238       │✓ ACTIVE   │ Charlie B│ 30 Jun 26 │      │
│  └──────────────────────────────────────────────────────────┘      │
│                                                                      │
│  [< Prev] Page 1 of 5 [Next >]                                     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Warranty Detail View
```
┌────────────────────────────────────────────────────────────┐
│ WARRANTY DETAILS - SN-2024-001234                           │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  Status: ✓ ACTIVE (Valid until 25 Jan 2026)              │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ PRODUCT INFORMATION                                  │  │
│  ├──────────────────────────────────────────────────────┤  │
│  │ Name:          iPhone 15 Pro                         │  │
│  │ Model:         A2846                                 │  │
│  │ Category:      Electronics / Mobile                 │  │
│  │ Manufacturer:  Apple Inc.                            │  │
│  │ Serial Number: SN-2024-001234                        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ CUSTOMER INFORMATION                                 │  │
│  ├──────────────────────────────────────────────────────┤  │
│  │ Name:    John Doe                                    │  │
│  │ Email:   john.doe@example.com                        │  │
│  │ Phone:   +1-555-0123                                 │  │
│  │ Address: 123 Main Street, New York, NY 10001        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ WARRANTY TERMS                                       │  │
│  ├──────────────────────────────────────────────────────┤  │
│  │ Purchase Date:    15 Jan 2024                        │  │
│  │ Start Date:       15 Jan 2024                        │  │
│  │ End Date:         15 Jan 2026                        │  │
│  │ Duration:         24 Months                          │  │
│  │ Status:           Active                             │  │
│  │ Days Remaining:   73 days                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ PURCHASE DETAILS                                     │  │
│  ├──────────────────────────────────────────────────────┤  │
│  │ Location:   Best Buy - New York, NY                 │  │
│  │ Price:      $999.99 USD                              │  │
│  │ Notes:      AppleCare+ Extended Plan Included        │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  [Edit] [Print] [Generate QR] [Transfer] [Claim]  [Close]  │
│                                                             │
└────────────────────────────────────────────────────────────┘
```

---

## QR Code Scanner Interface

```
┌────────────────────────────────────────────────────────┐
│ QR CODE SCANNER                              [×]       │
├────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │                                                   │  │
│  │          ╱──────────────────────╲                │  │
│  │         ╱  🎥 CAMERA FEED ✓      ╲               │  │
│  │        │                           │              │  │
│  │        │   ┌─────────────────┐     │              │  │
│  │        │   │ .  .  .  .  .  │     │              │  │
│  │        │   │ .  .  .  .  .  │     │              │  │
│  │        │   │ QR CODE HERE   │     │              │  │
│  │        │   │ .  .  .  .  .  │     │              │  │
│  │        │   │ .  .  .  .  .  │     │              │  │
│  │        │   └─────────────────┘     │              │  │
│  │        │                           │              │  │
│  │         ╲  Loading...               ╱               │  │
│  │          ╲──────────────────────╱                │  │
│  │                                                   │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  Scanned Data: ✓ SN-2024-001234                       │
│                 (Detected automatically)                │
│                                                         │
│  [🔄 Rescan] [✓ Use This Code] [🔌 Manual Input]      │
│                                                         │
└────────────────────────────────────────────────────────┘
```

### Manual Serial Entry
```
┌────────────────────────────────────────────────┐
│ ENTER SERIAL NUMBER                            │
├────────────────────────────────────────────────┤
│                                                 │
│  Serial Number:                                 │
│  ┌──────────────────────────────────────────┐ │
│  │ SN-2024-001234                           │ │
│  └──────────────────────────────────────────┘ │
│                                                 │
│  Format: SN-YYYY-XXXXXX                        │
│                                                 │
│  [Search] [Cancel]                             │
│                                                 │
└────────────────────────────────────────────────┘
```

---

## Tab 2: Products Management

```
┌─────────────────────────────────────────────────────────────────────┐
│ PRODUCTS                                                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [+ Add New Product]  [Import CSV]                                 │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ Product Name     │ Model    │ Category    │ Manufacturer    │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │ iPhone 15 Pro    │ A2846    │ Mobile      │ Apple           │  │
│  │ Galaxy S24 Ultra │ SM-S918U │ Mobile      │ Samsung         │  │
│  │ MacBook Pro 14"  │ M3 Max   │ Laptop      │ Apple           │  │
│  │ Dell XPS 15      │ XPS-9530 │ Laptop      │ Dell            │  │
│  │ iPad Air         │ A2585    │ Tablet      │ Apple           │  │
│  │ Surface Pro 11   │ 1928     │ Tablet+     │ Microsoft       │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  [Edit] [Delete] [View Details]  [< Prev] Page 1 of 3 [Next >]   │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Add/Edit Product Dialog
```
┌────────────────────────────────────────────────────┐
│ ADD NEW PRODUCT                                    │
├────────────────────────────────────────────────────┤
│                                                     │
│  Product Name *    [________________________]       │
│                                                     │
│  Model/SKU *       [________________________]       │
│                                                     │
│  Category          [Electronics      ▼]            │
│                                                     │
│  Manufacturer      [Apple             ▼]           │
│                                                     │
│  Description       ┌──────────────────────┐        │
│                    │                       │        │
│                    │                       │        │
│                    └──────────────────────┘        │
│                                                     │
│  ☑ Active         ☐ Discontinued                   │
│                                                     │
│  [Save] [Cancel]                                   │
│                                                     │
└────────────────────────────────────────────────────┘
```

---

## Tab 3: Customers Management

```
┌─────────────────────────────────────────────────────────────────────┐
│ CUSTOMERS                                                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  [+ Add New Customer] [Import CSV]                                 │
│                                                                      │
│  Search: [_____________________]  Status: [All ▼]                  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────┐      │
│  │ Name          │ Email             │ Phone      │ Country│      │
│  ├──────────────────────────────────────────────────────────┤      │
│  │ John Doe      │ john@example.com   │ +1-555-0123│ USA   │      │
│  │ Jane Smith    │ jane@example.com   │ +1-555-0124│ USA   │      │
│  │ Bob Johnson   │ bob@example.com    │ +1-555-0125│ USA   │      │
│  │ Alice White   │ alice@example.com  │ +1-555-0126│ USA   │      │
│  │ Charlie Brown │ charlie@example.com│ +1-555-0127│ USA   │      │
│  └──────────────────────────────────────────────────────────┘      │
│                                                                      │
│  [View Details] [Edit] [Delete]                                    │
│  [< Prev] Page 1 of 12 [Next >]                                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Customer Detail View
```
┌────────────────────────────────────────────────────────┐
│ CUSTOMER PROFILE - John Doe                            │
├────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │ PERSONAL INFORMATION                             │  │
│  ├──────────────────────────────────────────────────┤  │
│  │ Name:      John Doe                              │  │
│  │ Email:     john.doe@example.com                  │  │
│  │ Phone:     +1-555-0123                           │  │
│  │ City:      New York                              │  │
│  │ Country:   United States                         │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │ WARRANTY HISTORY (3 Active, 1 Expired)           │  │
│  ├──────────────────────────────────────────────────┤  │
│  │                                                   │  │
│  │ SN-2024-001234  │ iPhone 15     │ Active   ✓     │  │
│  │ SN-2024-001235  │ MacBook Pro   │ Active   ✓     │  │
│  │ SN-2024-001236  │ iPad Air      │ Active   ✓     │  │
│  │ SN-2024-001237  │ Apple Watch   │ Expired  ✗     │  │
│  │                                                   │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  [Edit] [Delete] [Export Data] [Close]                │
│                                                         │
└────────────────────────────────────────────────────────┘
```

### Add/Edit Customer Dialog
```
┌────────────────────────────────────────────────────┐
│ ADD NEW CUSTOMER                                   │
├────────────────────────────────────────────────────┤
│                                                     │
│  Full Name *       [________________________]       │
│                                                     │
│  Email             [________________________]       │
│                    (Unique - for notifications)    │
│                                                     │
│  Phone             [________________________]       │
│                                                     │
│  Address           [________________________]       │
│                                                     │
│  City              [________________________]       │
│                                                     │
│  Country           [Select Country    ▼]          │
│                                                     │
│  ☑ Subscribe to notifications                       │
│                                                     │
│  [Save] [Cancel]                                   │
│                                                     │
└────────────────────────────────────────────────────┘
```

---

## Create Warranty Dialog

```
┌─────────────────────────────────────────────────────────┐
│ CREATE NEW WARRANTY                                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ STEP 1 OF 3: PRODUCT INFORMATION                        │
│                                                          │
│  Serial Number *   [_____________________________]        │
│  (or scan QR code)  [📱 SCAN QR]                        │
│                                                          │
│  Product *         [Select Product    ▼]               │
│  [+ New Product]                                         │
│                                                          │
│  Customer *        [Select Customer   ▼]               │
│  [+ New Customer]                                        │
│                                                          │
│  ─────────────────────────────────────────────────────  │
│                                                          │
│ STEP 2 OF 3: WARRANTY DETAILS                           │
│                                                          │
│  Purchase Date *   [15/01/2024    ]  📅                 │
│                                                          │
│  Warranty Duration [24   ] months                        │
│  (months)                                                │
│                                                          │
│  Start Date        [15/01/2024    ]  (Auto-calculated)  │
│  End Date          [15/01/2026    ]  (Auto-calculated)  │
│                                                          │
│  ─────────────────────────────────────────────────────  │
│                                                          │
│ STEP 3 OF 3: PURCHASE DETAILS                           │
│                                                          │
│  Purchase Location [Best Buy New York]                  │
│                                                          │
│  Purchase Price    [999.99   ]  USD                     │
│                                                          │
│  Notes             ┌──────────────────┐                │
│                    │ Extended coverage│                │
│                    └──────────────────┘                │
│                                                          │
│  [< Back] [Next >] [Save] [Cancel]                      │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## User Flow Diagrams

### Primary User Flow: Scan & Lookup
```
START
  │
  ├─→ [Click Scan QR]
  │   │
  │   ├─→ [Camera Opens]
  │   │   │
  │   │   ├─→ [QR Detected] ✓
  │   │   │   │
  │   │   │   └─→ [Auto-Search & Display]
  │   │   │
  │   │   └─→ [Manual Entry]
  │   │       │
  │   │       └─→ [Click Search]
  │   │
  │   └─→ [Warranty Details Displayed]
  │       │
  │       ├─→ [View Details]
  │       ├─→ [Edit]
  │       ├─→ [Print]
  │       └─→ [Transfer/Claim]
  │
  └─→ END
```

### Warranty Registration Flow
```
START
  │
  ├─→ [Click + Create Warranty]
  │   │
  │   ├─→ [Enter Serial Number]
  │   │   ├─→ [Manual Entry]
  │   │   └─→ [Scan QR] 📱
  │   │
  │   ├─→ [Select Product]
  │   │   ├─→ [Existing Product]
  │   │   └─→ [+ New Product]
  │   │
  │   ├─→ [Select Customer]
  │   │   ├─→ [Existing Customer]
  │   │   └─→ [+ New Customer]
  │   │
  │   ├─→ [Enter Purchase Date]
  │   │
  │   ├─→ [Set Warranty Duration]
  │   │
  │   ├─→ [Enter Location & Price]
  │   │
  │   ├─→ [Add Notes]
  │   │
  │   ├─→ [Preview]
  │   │
  │   ├─→ [Click Save]
  │   │
  │   └─→ [Success Message] ✓
  │       [QR Code Generated]
  │
  └─→ END
```

---

## Notification & Alert Styles

### Success Alert
```
┌─────────────────────────────────────────┐
│ ✓ SUCCESS                      [×]       │
├─────────────────────────────────────────┤
│ Warranty created successfully!           │
│ Serial: SN-2024-001234                   │
│                                          │
│ QR Code: [Generated]  [Download] [Print]│
│                          [Close]         │
└─────────────────────────────────────────┘
```

### Warning Alert
```
┌─────────────────────────────────────────┐
│ ⚠ WARNING                       [×]      │
├─────────────────────────────────────────┤
│ This warranty expires in 30 days!        │
│ Customer may be eligible for renewal.    │
│                                          │
│ Serial: SN-2024-001234                   │
│                    [Dismiss] [Take Action]
└─────────────────────────────────────────┘
```

### Error Alert
```
┌─────────────────────────────────────────┐
│ ✗ ERROR                        [×]       │
├─────────────────────────────────────────┤
│ Serial number already registered!        │
│ This serial is associated with:          │
│                                          │
│ Product: iPhone 15 Pro                   │
│ Customer: John Doe                       │
│ Status: Active                           │
│                                          │
│        [View Existing] [Close]           │
└─────────────────────────────────────────┘
```

---

## Mobile-Responsive Design (Future)

### Mobile Main View
```
┌──────────────────────────┐
│ Warranty Manager      ☰   │
├──────────────────────────┤
│                          │
│  [📱 SCAN QR CODE]      │
│                          │
│  Search Serial:          │
│  [_______________]       │
│  [Search]                │
│                          │
│  Quick Stats:            │
│  • Active: 12            │
│  • Expiring: 2           │
│  • Expired: 1            │
│                          │
│  Recent Warranties:      │
│  ─────────────────       │
│  SN-2024-001234 ✓        │
│  John Doe                │
│  Expires: 25 Jan 26      │
│                          │
│  SN-2024-001235 ✓        │
│  Jane Smith              │
│  Expires: 15 Mar 26      │
│                          │
│  [Warranties][Products]  │
│  [Customers]             │
│                          │
└──────────────────────────┘
```

---

## Accessibility Guidelines

### Keyboard Navigation
- **Tab**: Navigate through fields and buttons
- **Enter**: Confirm/Submit
- **Esc**: Cancel/Close dialogs
- **Alt+S**: Scan QR code
- **Alt+N**: New warranty
- **Alt+F**: Search/Filter

### Screen Reader Support
- All buttons labeled clearly
- Form fields have descriptive labels
- Status indicators use text + icons
- Error messages clearly describe issues
- Data tables have headers and descriptions

### Color Contrast
- Primary text: Dark gray on white (WCAG AAA)
- Links: Blue (#0066CC) on white (WCAG AA)
- Status colors supplemented with icons/text
- Focus indicators: Visible blue outlines (3px)

### Font Sizes
- **Minimum**: 11px for secondary text
- **Default**: 12px for body text
- **Labels**: 12px bold for clarity
- **Headers**: 18px+ for sections

---

## Loading States & Animations

### Loading Spinner
```
Processing...   ⟳ (Rotating)

or

Processing...

    ◐
```

### Empty State
```
┌────────────────────────────┐
│                            │
│         📦 Empty           │
│                            │
│   No warranties found.     │
│                            │
│   [Create Your First One]  │
│                            │
└────────────────────────────┘
```

### Data Grid Loading
```
┌──────────────────────────────────────────┐
│ ▯▯▯▯▯▯  │  ▯▯▯▯▯▯  │  ▯▯▯▯▯▯  │        │
│ ▯▯▯▯▯▯  │  ▯▯▯▯▯▯  │  ▯▯▯▯▯▯  │        │
├──────────────────────────────────────────┤
│ ▯▯▯▯▯   │  ▯▯▯▯   │  ▯▯▯▯▯▯▯  │ ...   │
│ ▯▯▯▯▯   │  ▯▯▯▯   │  ▯▯▯▯▯▯▯  │        │
│ ▯▯▯▯▯   │  ▯▯▯▯   │  ▯▯▯▯▯▯▯  │        │
└──────────────────────────────────────────┘
(Skeleton loading)
```

---

## Desktop Application Toolbar

```
┌─────────────────────────────────────────────────────────┐
│ File  Edit  View  Tools  Help                           │
├─────────────────────────────────────────────────────────┤
│ [📱] [🏠] [🔄] [⚙️] [ℹ️]  |  [🔍] [🔐] [👤] [⋯]       │
│ Scan  Home Refresh Settings Help   Search Settings About │
└─────────────────────────────────────────────────────────┘
```

---

## Status Indicators

| Status | Icon | Color | Description |
|--------|------|-------|-------------|
| Active | ✓ | Green | Warranty is valid |
| Expiring Soon | ⚠ | Orange | Expires in 30 days or less |
| Expired | ✗ | Red | Warranty has ended |
| Claimed | 🎯 | Blue | Claim has been filed |
| Transferred | 🔄 | Purple | Ownership transferred |
| Pending | ⏳ | Gray | Waiting for confirmation |

---

## Button Styles

### Primary Action
```
┌─────────────────┐
│ ✓ Save Warranty │  (Blue background, white text)
└─────────────────┘
```

### Secondary Action
```
┌─────────────────┐
│   Close Dialog  │  (Gray background, dark text)
└─────────────────┘
```

### Danger Action
```
┌─────────────────┐
│ ✕ Delete Record │  (Red background, white text)
└─────────────────┘
```

### Disabled State
```
┌─────────────────┐
│ ⊗ Save Warranty │  (Light gray, faded text)
└─────────────────┘
```

---

## Input Field States

### Normal
```
Label Text
[_________________________________]
```

### Focused
```
Label Text (blue border)
[═════════════════════════════════]
  ┌─ Active, blue outline (2px)
```

### Filled
```
Label Text
[Value entered_____________________]
  └─ Text visible, normal border
```

### Error
```
Label Text  ⚠ Required field
[VALUE___________________________] ← Red border
  └─ Light red background
```

### Disabled
```
Label Text (gray text)
[═════════════════════════════════]  (Grayed out)
```

---

## Print View

```
╔════════════════════════════════════════════════════════════╗
║         WARRANTY CERTIFICATE OF COVERAGE                   ║
║                                                             ║
║  Product: iPhone 15 Pro                                    ║
║  Serial:  SN-2024-001234                                   ║
║  Model:   A2846                                             ║
║                                                             ║
║  Customer Information:                                      ║
║  Name:    John Doe                                         ║
║  Phone:   +1-555-0123                                      ║
║  Email:   john.doe@example.com                             ║
║                                                             ║
║  Coverage Period:                                           ║
║  Valid From:   15 January 2024                             ║
║  Valid Until:  15 January 2026                             ║
║  Duration:     24 Months                                   ║
║                                                             ║
║  Purchase Information:                                      ║
║  Purchase Date:    15 January 2024                         ║
║  Purchase Price:   $999.99 USD                             ║
║  Purchase Location: Best Buy - New York, NY                ║
║                                                             ║
║  [QR CODE HERE]                                            ║
║   ▀▀▀▀▀▀▀▀▀▀▀                                              ║
║                                                             ║
║  Authorized by: Warranty Management System                 ║
║  Document #: WAR-2024-001234                               ║
║  Date Generated: 13 March 2026                             ║
║                                                             ║
╚════════════════════════════════════════════════════════════╝
```

---

## Design Principles Applied

1. **Clarity**: Critical information is immediately visible
2. **Efficiency**: Common tasks completed in 2-3 steps
3. **Consistency**: Uniform styling across all screens
4. **Feedback**: Every action provides clear visual feedback
5. **Accessibility**: WCAG 2.1 AA compliance
6. **Responsive**: Works on desktop and tablet (mobile planned)
7. **Professional**: Corporate appearance, trustworthy design
8. **Forgiving**: Easy to undo actions, clear error messages
