#!/usr/bin/env python3
"""
Warranty Product System - API Test Script
Tests all major endpoints and demonstrates the system workflow
"""

import requests
import json
from datetime import datetime, timedelta
import time

BASE_URL = "http://localhost:5000"

class Colors:
    """Terminal colors for output"""
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text):
    """Print formatted header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")

def print_json(data):
    """Pretty print JSON"""
    print(json.dumps(data, indent=2))

def test_products():
    """Test product endpoints"""
    print_header("TESTING PRODUCT ENDPOINTS")
    
    products_data = [
        {
            "name": "iPhone 15 Pro",
            "model": "A2846",
            "category": "Mobile Phone",
            "manufacturer": "Apple Inc.",
            "description": "Premium flagship smartphone with advanced camera capabilities"
        },
        {
            "name": "Samsung Galaxy S24 Ultra",
            "model": "SM-S918U",
            "category": "Mobile Phone",
            "manufacturer": "Samsung Electronics",
            "description": "Ultra-premium Android smartphone"
        },
        {
            "name": "MacBook Pro 14 inch",
            "model": "M3 Max",
            "category": "Laptop",
            "manufacturer": "Apple Inc.",
            "description": "Professional grade laptop with M3 Max chip"
        },
        {
            "name": "iPad Air",
            "model": "A2585",
            "category": "Tablet",
            "manufacturer": "Apple Inc.",
            "description": "Mid-range tablet with M1 chip"
        }
    ]
    
    product_ids = []
    
    print_info("Creating 4 products...")
    for product in products_data:
        try:
            response = requests.post(
                f"{BASE_URL}/api/product",
                json=product,
                timeout=5
            )
            if response.status_code == 201:
                data = response.json()
                product_id = data['product']['id']
                product_ids.append(product_id)
                print_success(f"Created: {product['name']} (ID: {product_id[:8]}...)")
            else:
                print_error(f"Failed to create {product['name']}: {response.status_code}")
        except Exception as e:
            print_error(f"Error creating product: {str(e)}")
    
    # List products
    print_info("\nFetching all products...")
    try:
        response = requests.get(f"{BASE_URL}/api/product", timeout=5)
        if response.status_code == 200:
            products = response.json()
            print_success(f"Retrieved {len(products)} products")
        else:
            print_error(f"Failed to list products: {response.status_code}")
    except Exception as e:
        print_error(f"Error listing products: {str(e)}")
    
    return product_ids

def test_customers():
    """Test customer endpoints"""
    print_header("TESTING CUSTOMER ENDPOINTS")
    
    customers_data = [
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1-555-0123",
            "address": "123 Main Street",
            "city": "New York",
            "country": "USA"
        },
        {
            "name": "Jane Smith",
            "email": "jane.smith@example.com",
            "phone": "+1-555-0124",
            "address": "456 Oak Avenue",
            "city": "Los Angeles",
            "country": "USA"
        },
        {
            "name": "Bob Johnson",
            "email": "bob.johnson@example.com",
            "phone": "+1-555-0125",
            "address": "789 Pine Road",
            "city": "Chicago",
            "country": "USA"
        },
        {
            "name": "Alice White",
            "email": "alice.white@example.com",
            "phone": "+1-555-0126",
            "address": "321 Elm Street",
            "city": "Houston",
            "country": "USA"
        }
    ]
    
    customer_ids = []
    
    print_info("Creating 4 customers...")
    for customer in customers_data:
        try:
            response = requests.post(
                f"{BASE_URL}/api/customer",
                json=customer,
                timeout=5
            )
            if response.status_code == 201:
                data = response.json()
                customer_id = data['customer']['id']
                customer_ids.append(customer_id)
                print_success(f"Created: {customer['name']} (ID: {customer_id[:8]}...)")
            else:
                print_error(f"Failed to create {customer['name']}: {response.status_code}")
        except Exception as e:
            print_error(f"Error creating customer: {str(e)}")
    
    # List customers
    print_info("\nFetching all customers...")
    try:
        response = requests.get(f"{BASE_URL}/api/customer", timeout=5)
        if response.status_code == 200:
            customers = response.json()
            print_success(f"Retrieved {len(customers)} customers")
        else:
            print_error(f"Failed to list customers: {response.status_code}")
    except Exception as e:
        print_error(f"Error listing customers: {str(e)}")
    
    return customer_ids

def test_warranties(product_ids, customer_ids):
    """Test warranty endpoints"""
    print_header("TESTING WARRANTY ENDPOINTS")
    
    if not product_ids or not customer_ids:
        print_error("No products or customers available for warranty creation")
        return []
    
    warranties_data = [
        {
            "serial_number": "SN-2024-001234",
            "product_id": product_ids[0],
            "customer_id": customer_ids[0],
            "purchase_date": "2024-01-15T00:00:00",
            "warranty_duration_months": 24,
            "purchase_location": "Best Buy - New York",
            "purchase_price": 999.99,
            "currency": "USD",
            "notes": "AppleCare+ Extended coverage included"
        },
        {
            "serial_number": "SN-2024-001235",
            "product_id": product_ids[1],
            "customer_id": customer_ids[1],
            "purchase_date": "2024-02-01T00:00:00",
            "warranty_duration_months": 24,
            "purchase_location": "Best Buy - Los Angeles",
            "purchase_price": 899.99,
            "currency": "USD",
            "notes": "Standard Samsung warranty"
        },
        {
            "serial_number": "SN-2024-001236",
            "product_id": product_ids[2],
            "customer_id": customer_ids[2],
            "purchase_date": "2024-01-20T00:00:00",
            "warranty_duration_months": 36,
            "purchase_location": "Apple Store - Chicago",
            "purchase_price": 1999.99,
            "currency": "USD",
            "notes": "Extended AppleCare Pro included"
        },
        {
            "serial_number": "SN-2024-001237",
            "product_id": product_ids[3],
            "customer_id": customer_ids[3],
            "purchase_date": "2024-03-10T00:00:00",
            "warranty_duration_months": 12,
            "purchase_location": "Apple Store - Houston",
            "purchase_price": 599.99,
            "currency": "USD",
            "notes": "Standard iPad warranty"
        }
    ]
    
    warranty_ids = []
    
    print_info("Creating 4 warranties...")
    for i, warranty in enumerate(warranties_data):
        try:
            response = requests.post(
                f"{BASE_URL}/api/warranty",
                json=warranty,
                timeout=5
            )
            if response.status_code == 201:
                data = response.json()
                warranty_id = data['warranty']['id']
                warranty_ids.append(warranty_id)
                serial = warranty['serial_number']
                print_success(f"Created warranty {i+1}: {serial} (ID: {warranty_id[:8]}...)")
            else:
                print_error(f"Failed to create warranty {i+1}: {response.status_code}")
                print_info(f"Response: {response.text}")
        except Exception as e:
            print_error(f"Error creating warranty: {str(e)}")
    
    # Test warranty lookup by serial
    if warranty_ids:
        print_info("\nTesting warranty lookup by serial number...")
        serial = warranties_data[0]['serial_number']
        try:
            response = requests.get(
                f"{BASE_URL}/api/warranty/serial/{serial}",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                print_success(f"Found warranty: {serial}")
                print_info(f"  Product: {data.get('product', {}).get('name', 'N/A')}")
                print_info(f"  Customer: {data.get('customer', {}).get('name', 'N/A')}")
                print_info(f"  Status: {data.get('status', 'N/A')}")
                print_info(f"  Expires: {data.get('warranty_end_date', 'N/A')}")
            else:
                print_error(f"Failed to lookup warranty: {response.status_code}")
        except Exception as e:
            print_error(f"Error looking up warranty: {str(e)}")
    
    # Test warranty by ID
    if warranty_ids:
        print_info("\nTesting warranty lookup by ID...")
        try:
            response = requests.get(
                f"{BASE_URL}/api/warranty/{warranty_ids[0]}",
                timeout=5
            )
            if response.status_code == 200:
                data = response.json()
                print_success(f"Retrieved warranty details")
                print_info(f"  Serial: {data.get('serial_number', 'N/A')}")
                print_info(f"  Price: ${data.get('purchase_price', 'N/A')} {data.get('currency', 'USD')}")
            else:
                print_error(f"Failed to get warranty: {response.status_code}")
        except Exception as e:
            print_error(f"Error getting warranty: {str(e)}")
    
    return warranty_ids

def test_search():
    """Test search functionality"""
    print_header("TESTING SEARCH FUNCTIONALITY")
    
    print_info("Searching warranties by status...")
    try:
        response = requests.get(
            f"{BASE_URL}/api/warranty/search?status=active",
            timeout=5
        )
        if response.status_code == 200:
            warranties = response.json()
            print_success(f"Found {len(warranties)} active warranties")
            if warranties:
                print_info(f"  First warranty: {warranties[0].get('serial_number', 'N/A')}")
        else:
            print_error(f"Search failed: {response.status_code}")
    except Exception as e:
        print_error(f"Error searching: {str(e)}")

def test_update_warranty(warranty_id):
    """Test warranty update"""
    print_header("TESTING WARRANTY UPDATE")
    
    update_data = {
        "status": "active",
        "notes": "Updated notes at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    print_info(f"Updating warranty: {warranty_id[:8]}...")
    try:
        response = requests.put(
            f"{BASE_URL}/api/warranty/{warranty_id}",
            json=update_data,
            timeout=5
        )
        if response.status_code == 200:
            print_success("Warranty updated successfully")
        else:
            print_error(f"Update failed: {response.status_code}")
    except Exception as e:
        print_error(f"Error updating warranty: {str(e)}")

def test_qr_generation():
    """Test QR code generation"""
    print_header("TESTING QR CODE GENERATION")
    
    serial = "SN-2024-001234"
    print_info(f"Generating QR code for: {serial}...")
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/qr/generate",
            json={"serial_number": serial},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            qr_hex = data.get('qr_code', '')
            print_success(f"QR code generated ({len(qr_hex)//2} bytes)")
        else:
            print_error(f"QR generation failed: {response.status_code}")
    except Exception as e:
        print_error(f"Error generating QR: {str(e)}")

def main():
    """Run all tests"""
    print_header("WARRANTY PRODUCT SYSTEM - COMPREHENSIVE API TEST")
    
    print_info("Testing API at: " + BASE_URL)
    print_info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check if API is running
    try:
        response = requests.get(f"{BASE_URL}/api/product", timeout=2)
        print_success("✓ Backend API is running and responding")
    except Exception as e:
        print_error(f"✗ Cannot connect to API: {str(e)}")
        print_error("Make sure backend is running: python run.py")
        return
    
    time.sleep(1)
    
    # Run tests in sequence
    product_ids = test_products()
    time.sleep(1)
    
    customer_ids = test_customers()
    time.sleep(1)
    
    warranty_ids = test_warranties(product_ids, customer_ids)
    time.sleep(1)
    
    test_search()
    time.sleep(0.5)
    
    test_qr_generation()
    time.sleep(0.5)
    
    if warranty_ids:
        test_update_warranty(warranty_ids[0])
    
    # Summary
    print_header("TEST SUMMARY")
    print_success(f"Created {len(product_ids)} products")
    print_success(f"Created {len(customer_ids)} customers")
    print_success(f"Created {len(warranty_ids)} warranties")
    print_success("All tests completed!")
    
    print_info("\nNext steps:")
    print_info("1. View the interactive UI mockup: UI_PREVIEW.html")
    print_info("2. Read design documentation: UX_UI_DESIGN.md")
    print_info("3. Review API docs: API_DOCUMENTATION.md")
    print_info("4. Try the desktop app (requires display): python frontend/main.py")

if __name__ == "__main__":
    main()
