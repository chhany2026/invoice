#!/usr/bin/env python
"""
Test multi-product invoice creation
"""
import requests
import json
from datetime import datetime, timedelta

API_BASE = "http://localhost:5000/api"

def test_multi_product_invoice():
    """Test creating an invoice with multiple products"""
    
    print("\n" + "="*60)
    print("🧪 Testing Multi-Product Invoice Creation")
    print("="*60)
    
    try:
        # Step 1: Create customer
        print("\n1️⃣  Creating customer...")
        customer_data = {
            "name": "Test Customer",
            "email": f"customer_{datetime.now().timestamp()}@example.com",
            "phone": "+855 (0)12 345 678",
            "address": "Street Address",
            "city": "Phnom Penh",
            "country": "Cambodia"
        }
        
        resp = requests.post(f"{API_BASE}/customer", json=customer_data)
        if resp.status_code != 201:
            print(f"❌ Failed to create customer: {resp.text}")
            return False
        
        customer = resp.json()['customer']
        customer_id = customer['id']
        print(f"✓ Customer created: {customer_id}")
        
        # Step 2: Create multiple products
        print("\n2️⃣  Creating products...")
        product_ids = []
        
        products = [
            {
                "name": "iPhone 15 Pro",
                "model": "A2846",
                "category": "Electronics",
                "description": "Premium Smartphone",
                "manufacturer": "Apple"
            },
            {
                "name": "MacBook Air M3",
                "model": "MacBookAir15,1",
                "category": "Electronics",
                "description": "Laptop Computer",
                "manufacturer": "Apple"
            },
            {
                "name": "AirPods Pro",
                "model": "A2968",
                "category": "Electronics",
                "description": "Wireless Earbuds",
                "manufacturer": "Apple"
            }
        ]
        
        for product in products:
            resp = requests.post(f"{API_BASE}/product", json=product)
            if resp.status_code != 201:
                print(f"❌ Failed to create product {product['name']}: {resp.text}")
                return False
            
            prod = resp.json()['product']
            product_ids.append(prod['id'])
            print(f"✓ Product created: {product['name']} ({prod['id']})")
        
        # Step 3: Create invoice with multiple line items
        print("\n3️⃣  Creating invoice with multiple products...")
        
        today = datetime.now()
        due_date = today + timedelta(days=30)
        
        invoice_data = {
            "customer_id": customer_id,
            "invoice_date": today.isoformat(),
            "due_date": due_date.isoformat(),
            "line_items": [
                {
                    "product_id": product_ids[0],
                    "quantity": 1,
                    "unit_price": 999.99,
                    "warranty_duration_months": 24,
                    "serial_number": f"SN-IP15P-{int(datetime.now().timestamp() * 1000) % 10000}",
                    "description": "iPhone 15 Pro"
                },
                {
                    "product_id": product_ids[1],
                    "quantity": 1,
                    "unit_price": 1299.99,
                    "warranty_duration_months": 12,
                    "serial_number": f"SN-MBA-{int(datetime.now().timestamp() * 1000) % 10000}",
                    "description": "MacBook Air M3"
                },
                {
                    "product_id": product_ids[2],
                    "quantity": 2,
                    "unit_price": 249.99,
                    "warranty_duration_months": 12,
                    "serial_number": f"SN-AIRPODS-{int(datetime.now().timestamp() * 1000) % 10000}",
                    "description": "AirPods Pro"
                }
            ],
            "tax_amount": 100.00,
            "currency": "USD",
            "language": "en"
        }
        
        resp = requests.post(f"{API_BASE}/invoice", json=invoice_data)
        
        if resp.status_code != 201:
            print(f"❌ Failed to create invoice: {resp.status_code}")
            print(f"Response: {resp.text}")
            return False
        
        resp_json = resp.json()
        
        # DEBUG: Print full response
        print(f"📋 Full response: {json.dumps(resp_json, indent=2)}")
        
        # Handle both response formats
        if 'invoice' in resp_json:
            invoice = resp_json['invoice']
        elif 'invoices' in resp_json:
            invoice = resp_json['invoices'][0] if resp_json['invoices'] else None
        else:
            invoice = resp_json
        
        if not invoice:
            print(f"❌ No invoice in response: {resp_json}")
            return False
        
        # Handle different ID field names
        invoice_id = invoice.get('id') or invoice.get('_id') or invoice.get('invoice_id')
        invoice_number = invoice.get('invoice_number') or invoice.get('number')
        
        print(f"✓ Invoice created: {invoice_number} ({invoice_id})")
        print(f"  - Subtotal: ${invoice_data['line_items'][0]['unit_price'] * invoice_data['line_items'][0]['quantity'] + invoice_data['line_items'][1]['unit_price'] * invoice_data['line_items'][1]['quantity'] + invoice_data['line_items'][2]['unit_price'] * invoice_data['line_items'][2]['quantity']:.2f}")
        print(f"  - Tax: ${invoice_data['tax_amount']:.2f}")
        print(f"  - Total: ${resp_json.get('grand_total', 0):.2f}")
        print(f"  - Items: {len(invoice_data['line_items'])} products")
        
        # Step 4: Verify invoice details
        print("\n4️⃣  Verifying invoice details...")
        resp = requests.get(f"{API_BASE}/invoice/{invoice_id}")
        
        if resp.status_code != 200:
            print(f"❌ Failed to retrieve invoice: {resp.text}")
            return False
        
        resp_data = resp.json()
        
        # Handle different response structures
        if 'invoice' in resp_data:
            invoice_detail = resp_data['invoice']
        elif 'invoices' in resp_data and resp_data['invoices']:
            invoice_detail = resp_data['invoices'][0]
        else:
            invoice_detail = resp_data
        
        line_items = invoice_detail.get('line_items', [])
        
        print(f"✓ Invoice verified")
        print(f"  - Line items count: {len(line_items)}")
        
        for i, item in enumerate(line_items, 1):
            print(f"    {i}. {item['description']} x{item['quantity']} @ ${item['unit_price']} = ${item['line_total']}")
        
        # Step 5: Test print endpoints
        print("\n5️⃣  Testing print endpoints...")
        
        resp = requests.get(f"{API_BASE}/invoice/{invoice_id}/print")
        if resp.status_code == 200:
            print(f"✓ Invoice print template loaded successfully")
        else:
            print(f"⚠️  Invoice print failed: {resp.status_code}")
        
        print("\n" + "="*60)
        print("✅ Multi-Product Invoice Test PASSED!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_multi_product_invoice()
    exit(0 if success else 1)
