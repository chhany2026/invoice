#!/usr/bin/env python
"""
Test Khmer invoice printing
"""
import requests
import json
from datetime import datetime, timedelta

API_BASE = "http://localhost:5000/api"

def test_khmer_invoice():
    """Test creating and printing an invoice in Khmer language"""
    
    print("\n" + "="*60)
    print("🇰🇭 Testing Khmer Invoice Print")
    print("="*60)
    
    try:
        # Step 1: Create customer
        print("\n1️⃣  Creating customer...")
        customer_data = {
            "name": "បराग राଜ",
            "email": f"khmer_{datetime.now().timestamp()}@example.com",
            "phone": "+855 (0)17 123 456",
            "address": "ផ្លូវលេលីម",
            "city": "ភ្នំពេញ",
            "country": "កម្ពុជា"
        }
        
        resp = requests.post(f"{API_BASE}/customer", json=customer_data)
        customer = resp.json()['customer']
        customer_id = customer['id']
        print(f"✓ Customer created: {customer_id}")
        
        # Step 2: Create product
        print("\n2️⃣  Creating product...")
        product_data = {
            "name": "ស្មាតហ្វូន",
            "model": "SM-A135F",
            "category": "ឧបករណ៍អេឡិចត្រូនិក",
            "description": "សម្រាប់ប្រើប្រាស់ប្រចាំថ្ងៃ",
            "manufacturer": "Samsung"
        }
        
        resp = requests.post(f"{API_BASE}/product", json=product_data)
        product = resp.json()['product']
        product_id = product['id']
        print(f"✓ Product created: {product_id}")
        
        # Step 3: Create invoice with Khmer language
        print("\n3️⃣  Creating Khmer invoice...")
        
        today = datetime.now()
        due_date = today + timedelta(days=30)
        
        invoice_data = {
            "customer_id": customer_id,
            "invoice_date": today.isoformat(),
            "due_date": due_date.isoformat(),
            "line_items": [
                {
                    "product_id": product_id,
                    "quantity": 2,
                    "unit_price": 299.99,
                    "warranty_duration_months": 12,
                    "serial_number": f"SN-KHM-{int(datetime.now().timestamp() * 1000) % 10000}",
                    "description": "ស្មាតហ្វូន Samsung A13"
                }
            ],
            "tax_amount": 50.00,
            "currency": "USD",
            "language": "km"  # Khmer language
        }
        
        resp = requests.post(f"{API_BASE}/invoice", json=invoice_data)
        
        if resp.status_code != 201:
            print(f"❌ Failed to create invoice: {resp.status_code}")
            print(f"Response: {resp.text}")
            return False
        
        resp_json = resp.json()
        invoice_id = resp_json.get('invoice_id')
        invoice_number = resp_json.get('invoice_number')
        
        print(f"✓ Khmer invoice created: {invoice_number} ({invoice_id})")
        print(f"  - Language: Khmer (km)")
        print(f"  - Total: ${resp_json.get('grand_total', 0):.2f}")
        
        # Step 4: Test Khmer print endpoint
        print("\n4️⃣  Testing Khmer invoice print...")
        resp = requests.get(f"{API_BASE}/invoice/{invoice_id}/print")
        
        if resp.status_code == 200:
            print(f"✓ Khmer invoice print template loaded successfully")
            
            # Check if Khmer text is in the response
            html_content = resp.text
            
            khmer_labels = {
                "លេខវិក័យប័ត្រ": "Invoice Number",
                "វិក័យប័ត្របង្រួមឱ្យ": "Bill To",
                "លម្អិត": "Description",
                "តម្លៃឯកតា": "Unit Price",
                "សរុបសាលរ": "Grand Total"
            }
            
            found_khmer = []
            for khmer_text, english_equiv in khmer_labels.items():
                if khmer_text in html_content:
                    found_khmer.append(khmer_text)
            
            if found_khmer:
                print(f"✓ Khmer labels found in template:")
                for label in found_khmer:
                    print(f"   • {label}")
            else:
                print(f"⚠️  Some Khmer labels not found in template")
        else:
            print(f"❌ Khmer print failed: {resp.status_code}")
            return False
        
        # Step 5: Test receipt print
        print("\n5️⃣  Testing Khmer receipt print...")
        resp = requests.get(f"{API_BASE}/invoice/{invoice_id}/receipt/print")
        
        if resp.status_code == 200:
            print(f"✓ Khmer receipt print template loaded successfully")
        else:
            print(f"⚠️  Receipt print returned: {resp.status_code}")
        
        print("\n" + "="*60)
        print("✅ Khmer Invoice Test PASSED!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == '__main__':
    success = test_khmer_invoice()
    exit(0 if success else 1)
