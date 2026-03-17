# Warranty Product Management System

A global warranty recording system that allows users to register and manage warranty products from **QR codes or serial numbers**. Built with Flask backend and PyQt6 desktop application.

## Features

✅ **QR Code Scanning** - Camera-based QR code scanning and manual serial number input
✅ **Global Warranty Database** - Centralized warranty product records with full customer info
✅ **Multi-Platform** - Works on Windows, macOS, and Linux
✅ **Hybrid Deployment** - Deploy locally (SQLite) or on cloud (PostgreSQL)
✅ **RESTful API** - Complete REST API for integration with other systems
✅ **Product Management** - Track products, models, categories, and manufacturers
✅ **Customer Management** - Store comprehensive customer information
✅ **Extended Data** - Record purchase details, warranty duration, location, and pricing

## Project Structure

```
Warranty Product/
├── backend/
│   ├── app/
│   │   ├── __init__.py          # Flask app factory
│   │   ├── models.py            # Database models (Warranty, Product, Customer)
│   │   ├── routes.py            # API endpoints
│   │   └── config.py            # Configuration management
│   ├── requirements.txt          # Python dependencies
│   ├── run.py                    # Backend entry point
│   └── .env.example              # Environment template
│
├── frontend/
│   ├── main.py                   # Application entry point
│   ├── main_window.py            # Main UI window
│   ├── qr_scanner.py             # QR code scanning module
│   ├── dialogs.py                # Dialog windows for CRUD operations
│   ├── api_client.py             # API client
│   ├── requirements.txt          # Frontend dependencies
│   └── .env.example              # Environment template
│
├── README.md                      # This file
├── DEPLOYMENT.md                  # Deployment guide
└── API_DOCUMENTATION.md           # API reference
```

## Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL (for production) or SQLite (for development)
- Camera (for QR code scanning)

### Backend Setup

1. **Install dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env file with your database credentials
```

3. **Run the backend server:**
```bash
python run.py
```

The API will be available at `http://localhost:5000`

### Frontend Setup

1. **Install dependencies:**
```bash
cd frontend
pip install -r requirements.txt
```

2. **Configure environment:**
```bash
cp .env.example .env
# Edit .env file if needed (API_BASE_URL defaults to localhost:5000)
```

3. **Run the application:**
```bash
python main.py
```

## Database Schema

### Customers Table
- `id` (UUID) - Primary key
- `name` - Customer's full name
- `email` - Email address (unique)
- `phone` - Phone number
- `address` - Street address
- `city` - City
- `country` - Country
- `created_at`, `updated_at` - Timestamps

### Products Table
- `id` (UUID) - Primary key
- `name` - Product name
- `model` - Product model number
- `category` - Product category
- `description` - Product description
- `manufacturer` - Manufacturer name
- `created_at`, `updated_at` - Timestamps

### Warranties Table
- `id` (UUID) - Primary key
- `serial_number` - Product serial (unique)
- `qr_code` - QR code data (unique)
- `product_id` - Foreign key to Product
- `customer_id` - Foreign key to Customer
- `purchase_date` - Date of purchase
- `warranty_start_date` - Warranty start date
- `warranty_end_date` - Warranty expiration date
- `warranty_duration_months` - Duration in months
- `purchase_location` - Where product was purchased
- `purchase_price` - Purchase amount
- `currency` - Currency code (default: USD)
- `status` - active | expired | claimed | transferred
- `notes` - Additional notes
- `created_at`, `updated_at` - Timestamps

## API Endpoints

### Warranties
- `POST /api/warranty` - Create warranty
- `GET /api/warranty/<id>` - Get warranty by ID
- `GET /api/warranty/serial/<serial>` - Get warranty by serial number
- `PUT /api/warranty/<id>` - Update warranty
- `GET /api/warranty/search` - Search warranties (filters: customer_id, product_id, status)

### Products
- `POST /api/product` - Create product
- `GET /api/product` - List all products
- `GET /api/product/<id>` - Get product details

### Customers
- `POST /api/customer` - Create customer
- `GET /api/customer` - List all customers
- `GET /api/customer/<id>` - Get customer with warranties

### QR Codes
- `POST /api/qr/generate` - Generate QR code for serial number

## Configuration

### Development
Uses SQLite database for easy local development:
```
DATABASE_URL=sqlite:///warranty_product.db
```

### Production
Uses PostgreSQL for scalability:
```
DATABASE_URL=postgresql://user:password@host:5432/warranty_product
```

## Features in Detail

### QR Code Scanner
- **Camera Input**: Real-time camera feed with QR detection
- **Manual Input**: Type serial numbers directly
- **Visual Feedback**: Detected QR codes highlighted in green
- **Auto-Lookup**: Scanned codes instantly searched in database

### Warranty Management
Create and track warranty records with:
- Product information
- Customer details
- Purchase information (date, location, price)
- Warranty duration and expiry dates
- Status tracking (active, expired, claimed, transferred)
- Custom notes and comments

### Product Database
- Store product specifications
- Track product models
- Categorize products
- Link to warranties

### Customer Management
- Store full customer information
- Email validation (unique)
- Track all warranties per customer
- Export customer data

## Advanced Features (Coming Soon)

- Claim management system
- Warranty transfer functionality
- Email notifications for expiring warranties
- Bulk import/export (CSV)
- Mobile app extension
- Barcode code scanning
- Warranty PDF generation
- Integration with payment systems
- Multi-language support
- Two-factor authentication
- Advanced reporting and analytics

## Troubleshooting

**Issue: "Unable to open camera"**
- Check camera permissions
- Try a different camera index (0, 1, 2...)
- Ensure no other app is using the camera

**Issue: "Database connection failed"**
- Verify database is running
- Check credentials in .env file
- For PostgreSQL, ensure database exists

**Issue: "API connection refused"**
- Ensure backend server is running on port 5000
- Check firewall settings
- Verify API_BASE_URL in frontend .env

## Support

For issues and feature requests, contact support or file an issue in the repository.

## License

© 2026 Warranty Product Management System. All rights reserved.
