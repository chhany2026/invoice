import requests
import json
from typing import Dict, List, Optional

class APIClient:
    """Client for communicating with Flask backend API"""
    
    def __init__(self, base_url: str = 'http://localhost:5000'):
        self.base_url = base_url
        self.session = requests.Session()
    
    # ==================== WARRANTY METHODS ====================
    def create_warranty(self, warranty_data: Dict) -> Dict:
        """Create a new warranty record"""
        response = self.session.post(
            f'{self.base_url}/api/warranty',
            json=warranty_data
        )
        response.raise_for_status()
        return response.json()
    
    def get_warranty(self, warranty_id: str) -> Dict:
        """Get warranty by ID"""
        response = self.session.get(
            f'{self.base_url}/api/warranty/{warranty_id}'
        )
        response.raise_for_status()
        return response.json()
    
    def get_warranty_by_serial(self, serial_number: str) -> Dict:
        """Get warranty by serial number"""
        response = self.session.get(
            f'{self.base_url}/api/warranty/serial/{serial_number}'
        )
        response.raise_for_status()
        return response.json()
    
    def update_warranty(self, warranty_id: str, warranty_data: Dict) -> Dict:
        """Update warranty record"""
        response = self.session.put(
            f'{self.base_url}/api/warranty/{warranty_id}',
            json=warranty_data
        )
        response.raise_for_status()
        return response.json()
    
    def search_warranties(self, customer_id: Optional[str] = None, 
                         product_id: Optional[str] = None,
                         status: Optional[str] = None) -> List[Dict]:
        """Search warranties with filters"""
        params = {}
        if customer_id:
            params['customer_id'] = customer_id
        if product_id:
            params['product_id'] = product_id
        if status:
            params['status'] = status
        
        response = self.session.get(
            f'{self.base_url}/api/warranty/search',
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    # ==================== PRODUCT METHODS ====================
    def create_product(self, product_data: Dict) -> Dict:
        """Create a new product"""
        response = self.session.post(
            f'{self.base_url}/api/product',
            json=product_data
        )
        response.raise_for_status()
        return response.json()
    
    def list_products(self) -> List[Dict]:
        """Get all products"""
        response = self.session.get(
            f'{self.base_url}/api/product'
        )
        response.raise_for_status()
        return response.json()
    
    def get_product(self, product_id: str) -> Dict:
        """Get product details"""
        response = self.session.get(
            f'{self.base_url}/api/product/{product_id}'
        )
        response.raise_for_status()
        return response.json()
    
    # ==================== CUSTOMER METHODS ====================
    def create_customer(self, customer_data: Dict) -> Dict:
        """Create a new customer"""
        response = self.session.post(
            f'{self.base_url}/api/customer',
            json=customer_data
        )
        response.raise_for_status()
        return response.json()
    
    def list_customers(self) -> List[Dict]:
        """Get all customers"""
        response = self.session.get(
            f'{self.base_url}/api/customer'
        )
        response.raise_for_status()
        return response.json()
    
    def get_customer(self, customer_id: str) -> Dict:
        """Get customer details with warranties"""
        response = self.session.get(
            f'{self.base_url}/api/customer/{customer_id}'
        )
        response.raise_for_status()
        return response.json()
    
    # ==================== INVOICE METHODS ====================
    def create_invoice(self, invoice_data: Dict) -> Dict:
        """Create a new invoice"""
        response = self.session.post(
            f'{self.base_url}/api/invoice',
            json=invoice_data
        )
        response.raise_for_status()
        return response.json()
    
    def list_invoices(self) -> List[Dict]:
        """Get all invoices"""
        response = self.session.get(
            f'{self.base_url}/api/invoice'
        )
        response.raise_for_status()
        return response.json()
    
    def get_invoice(self, invoice_id: str) -> Dict:
        """Get invoice details"""
        response = self.session.get(
            f'{self.base_url}/api/invoice/{invoice_id}'
        )
        response.raise_for_status()
        return response.json()
    
    def update_invoice(self, invoice_id: str, invoice_data: Dict) -> Dict:
        """Update invoice"""
        response = self.session.put(
            f'{self.base_url}/api/invoice/{invoice_id}',
            json=invoice_data
        )
        response.raise_for_status()
        return response.json()
    
    # ==================== RECEIPT METHODS ====================
    def create_receipt(self, receipt_data: Dict) -> Dict:
        """Create a receipt for an invoice"""
        response = self.session.post(
            f'{self.base_url}/api/receipt',
            json=receipt_data
        )
        response.raise_for_status()
        return response.json()
    
    def list_receipts(self) -> List[Dict]:
        """Get all receipts"""
        response = self.session.get(
            f'{self.base_url}/api/receipt'
        )
        response.raise_for_status()
        return response.json()
    
    def get_receipt(self, receipt_id: str) -> Dict:
        """Get receipt details"""
        response = self.session.get(
            f'{self.base_url}/api/receipt/{receipt_id}'
        )
        response.raise_for_status()
        return response.json()
    
    # ==================== QR CODE METHODS ====================
    def generate_qr_code(self, serial_number: str) -> Dict:
        """Generate QR code for serial number"""
        response = self.session.post(
            f'{self.base_url}/api/qr/generate',
            json={'serial_number': serial_number}
        )
        response.raise_for_status()
        return response.json()
