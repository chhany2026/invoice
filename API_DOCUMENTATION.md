# API Documentation

## Base URL
```
http://localhost:5000
```

## Authentication
Currently, the API doesn't require authentication. In production, JWT tokens should be implemented.

---

## Warranty Endpoints

### Create Warranty
**POST** `/api/warranty`

Creates a new warranty record for a product.

**Request Body:**
```json
{
  "serial_number": "SN123456789",
  "product_id": "uuid-product-id",
  "customer_id": "uuid-customer-id",
  "purchase_date": "2024-01-15T00:00:00",
  "warranty_duration_months": 24,
  "purchase_location": "Best Buy - New York",
  "purchase_price": 999.99,
  "currency": "USD",
  "notes": "Extended warranty purchased"
}
```

**Required Fields:**
- `serial_number` (string, unique) - Product serial number
- `product_id` (string) - Valid product UUID
- `customer_id` (string) - Valid customer UUID
- `purchase_date` (ISO datetime) - Purchase date
- `warranty_duration_months` (integer) - Warranty period in months

**Optional Fields:**
- `purchase_location` (string) - Where product was purchased
- `purchase_price` (float) - Purchase amount
- `currency` (string, default="USD") - Currency code
- `notes` (string) - Additional notes

**Response (201 Created):**
```json
{
  "message": "Warranty created successfully",
  "warranty": {
    "id": "uuid",
    "serial_number": "SN123456789",
    "qr_code": "uuid-qr-code",
    "product_id": "uuid",
    "customer_id": "uuid",
    "product": { ... },
    "customer": { ... },
    "purchase_date": "2024-01-15T00:00:00",
    "warranty_start_date": "2024-01-15T00:00:00",
    "warranty_end_date": "2026-01-15T00:00:00",
    "warranty_duration_months": 24,
    "purchase_location": "Best Buy - New York",
    "purchase_price": 999.99,
    "currency": "USD",
    "status": "active",
    "notes": "Extended warranty purchased",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T10:30:00"
  }
}
```

---

### Get Warranty by ID
**GET** `/api/warranty/<warranty_id>`

Retrieve warranty details by its UUID.

**Parameters:**
- `warranty_id` (path, required) - Warranty UUID

**Response (200 OK):**
```json
{
  "id": "uuid",
  "serial_number": "SN123456789",
  "product": { ... },
  "customer": { ... },
  "warranty_end_date": "2026-01-15T00:00:00",
  "status": "active",
  ...
}
```

**Response (404 Not Found):**
```json
{
  "error": "Warranty not found"
}
```

---

### Get Warranty by Serial Number
**GET** `/api/warranty/serial/<serial_number>`

Retrieve warranty by product serial number.

**Parameters:**
- `serial_number` (path, required) - Product serial number

**Response (200 OK):**
```json
{
  "id": "uuid",
  "serial_number": "SN123456789",
  "product": { ... },
  "customer": { ... },
  ...
}
```

---

### Update Warranty
**PUT** `/api/warranty/<warranty_id>`

Update warranty record (partial update supported).

**Request Body:**
```json
{
  "status": "expired",
  "notes": "Updated warranty status",
  "purchase_location": "Updated location",
  "purchase_price": 1099.99
}
```

**Updatable Fields:**
- `purchase_location` (string)
- `purchase_price` (float)
- `status` (string) - active | expired | claimed | transferred
- `notes` (string)

**Response (200 OK):**
```json
{
  "message": "Warranty updated successfully",
  "warranty": { ... }
}
```

---

### Search Warranties
**GET** `/api/warranty/search`

Search warranties with filters.

**Query Parameters:**
- `customer_id` (optional) - Filter by customer
- `product_id` (optional) - Filter by product
- `status` (optional) - Filter by status (active, expired, claimed, transferred)

**Example:**
```
GET /api/warranty/search?customer_id=uuid&status=active
```

**Response (200 OK):**
```json
[
  { warranty1 },
  { warranty2 },
  { warranty3 }
]
```

---

## Product Endpoints

### Create Product
**POST** `/api/product`

Add a new product to the database.

**Request Body:**
```json
{
  "name": "iPhone 15 Pro",
  "model": "A2846",
  "category": "Electronics",
  "manufacturer": "Apple",
  "description": "Premium smartphone with advanced camera system"
}
```

**Required Fields:**
- `name` (string) - Product name
- `model` (string) - Model/SKU number

**Optional Fields:**
- `category` (string) - Product category
- `manufacturer` (string) - Manufacturer name
- `description` (string) - Detailed description

**Response (201 Created):**
```json
{
  "message": "Product created successfully",
  "product": {
    "id": "uuid",
    "name": "iPhone 15 Pro",
    "model": "A2846",
    "category": "Electronics",
    "manufacturer": "Apple",
    "description": "...",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T10:30:00"
  }
}
```

---

### List All Products
**GET** `/api/product`

Retrieve all products in the database.

**Response (200 OK):**
```json
[
  {
    "id": "uuid",
    "name": "iPhone 15 Pro",
    "model": "A2846",
    ...
  },
  {
    "id": "uuid",
    "name": "Samsung Galaxy S24",
    "model": "SM-S921B",
    ...
  }
]
```

---

### Get Product Details
**GET** `/api/product/<product_id>`

Get details of a specific product.

**Parameters:**
- `product_id` (path, required) - Product UUID

**Response (200 OK):**
```json
{
  "id": "uuid",
  "name": "iPhone 15 Pro",
  "model": "A2846",
  "category": "Electronics",
  "manufacturer": "Apple",
  "description": "Premium smartphone...",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

---

## Customer Endpoints

### Create Customer
**POST** `/api/customer`

Add a new customer to the database.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1-555-0123",
  "address": "123 Main Street",
  "city": "New York",
  "country": "United States"
}
```

**Required Fields:**
- `name` (string) - Customer's full name

**Optional Fields:**
- `email` (string, unique) - Email address
- `phone` (string) - Phone number
- `address` (string) - Street address
- `city` (string) - City
- `country` (string) - Country

**Response (201 Created):**
```json
{
  "message": "Customer created successfully",
  "customer": {
    "id": "uuid",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-0123",
    "address": "123 Main Street",
    "city": "New York",
    "country": "United States",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T10:30:00"
  }
}
```

---

### List All Customers
**GET** `/api/customer`

Retrieve all customers in the database.

**Response (200 OK):**
```json
[
  {
    "id": "uuid",
    "name": "John Doe",
    "email": "john.doe@example.com",
    ...
  },
  {
    "id": "uuid",
    "name": "Jane Smith",
    ...
  }
]
```

---

### Get Customer with Warranties
**GET** `/api/customer/<customer_id>`

Get customer details including all their warranties.

**Parameters:**
- `customer_id` (path, required) - Customer UUID

**Response (200 OK):**
```json
{
  "id": "uuid",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1-555-0123",
  "address": "123 Main Street",
  "city": "New York",
  "country": "United States",
  "warranties": [
    {
      "id": "warranty-uuid-1",
      "serial_number": "SN123456789",
      "product": { ... },
      "status": "active",
      "warranty_end_date": "2026-01-15T00:00:00",
      ...
    },
    {
      "id": "warranty-uuid-2",
      ...
    }
  ],
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-15T10:30:00"
}
```

---

## QR Code Endpoints

### Generate QR Code
**POST** `/api/qr/generate`

Generate a QR code image for a serial number.

**Request Body:**
```json
{
  "serial_number": "SN123456789"
}
```

**Required Fields:**
- `serial_number` (string) - Serial number to encode

**Response (200 OK):**
```json
{
  "qr_code": "89504e470d0a1a0a...",  // Hex-encoded PNG image
  "serial_number": "SN123456789"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "Missing required fields"
}
```

### 404 Not Found
```json
{
  "error": "Warranty not found"
}
```

### 409 Conflict
```json
{
  "error": "Serial number already registered"
}
```

### 500 Internal Server Error
```json
{
  "error": "Database connection error"
}
```

---

## Response Codes

| Code | Description |
|------|-------------|
| 200 | Success - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Resource not found |
| 409 | Conflict - Resource already exists |
| 500 | Internal Server Error |

---

## Examples using cURL

### Create a Product
```bash
curl -X POST http://localhost:5000/api/product \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 15",
    "model": "A2846",
    "manufacturer": "Apple"
  }'
```

### Create a Customer
```bash
curl -X POST http://localhost:5000/api/customer \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "country": "USA"
  }'
```

### Create a Warranty
```bash
curl -X POST http://localhost:5000/api/warranty \
  -H "Content-Type: application/json" \
  -d '{
    "serial_number": "SN123456",
    "product_id": "<product-uuid>",
    "customer_id": "<customer-uuid>",
    "purchase_date": "2024-01-15",
    "warranty_duration_months": 24
  }'
```

### Search Warranty by Serial
```bash
curl http://localhost:5000/api/warranty/serial/SN123456
```

### Get Customer with Warranties
```bash
curl http://localhost:5000/api/customer/<customer-uuid>
```

---

## Rate Limiting (Future Feature)

Rate limiting will be implemented to prevent abuse:
- **Default**: 100 requests per minute per IP
- **Authentication**: 1000 requests per minute for authenticated users

---

## Pagination (Future Feature)

List endpoints will support pagination:
```
GET /api/warranty?page=1&per_page=20
```

---

## Documentation Generated
Generated with OpenAPI 3.0 (Swagger docs coming soon)
