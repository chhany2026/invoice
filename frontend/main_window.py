from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QTabWidget, QTableWidget, QTableWidgetItem,
                             QLineEdit, QLabel, QMessageBox, QComboBox, QStatusBar)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QColor
from api_client import APIClient
from qr_scanner import QRScannerDialog
from dialogs import NewWarrantyDialog, NewProductDialog, NewCustomerDialog, NewInvoiceDialog, NewReceiptDialog
from datetime import datetime


class WarrantyProductApp(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Warranty Product Management System')
        self.setGeometry(0, 0, 1200, 700)
        
        # Initialize API client
        self.api_client = APIClient('http://localhost:5000')
        
        # Create UI
        self.init_ui()
        
        # Load initial data
        self.refresh_warranties()
        self.refresh_products()
        self.refresh_customers()
        self.refresh_invoices()
        self.refresh_receipts()
    
    def init_ui(self):
        """Initialize the main UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Top control panel
        control_layout = QHBoxLayout()
        
        # QR Code Scanner Button
        self.scan_button = QPushButton('📱 Scan QR Code')
        self.scan_button.setFont(QFont('Arial', 10, QFont.Weight.Bold))
        self.scan_button.clicked.connect(self.open_qr_scanner)
        control_layout.addWidget(self.scan_button)
        
        # Serial Number Search
        control_layout.addWidget(QLabel('Search Serial:'))
        self.search_serial_input = QLineEdit()
        self.search_serial_input.setPlaceholderText('Enter serial number...')
        self.search_serial_input.returnPressed.connect(self.search_warranty)
        control_layout.addWidget(self.search_serial_input)
        
        search_button = QPushButton('Search')
        search_button.clicked.connect(self.search_warranty)
        control_layout.addWidget(search_button)
        
        control_layout.addStretch()
        
        main_layout.addLayout(control_layout)
        
        # Tab widget for different views
        tabs = QTabWidget()
        
        # Warranties Tab
        warranties_widget = QWidget()
        warranties_layout = QVBoxLayout()
        
        warranty_button_layout = QHBoxLayout()
        new_warranty_btn = QPushButton('Create New Warranty')
        new_warranty_btn.clicked.connect(self.open_new_warranty_dialog)
        warranty_button_layout.addWidget(new_warranty_btn)
        
        refresh_warranty_btn = QPushButton('Refresh')
        refresh_warranty_btn.clicked.connect(self.refresh_warranties)
        warranty_button_layout.addWidget(refresh_warranty_btn)
        warranty_button_layout.addStretch()
        
        warranties_layout.addLayout(warranty_button_layout)
        
        self.warranties_table = QTableWidget()
        self.warranties_table.setColumnCount(8)
        self.warranties_table.setHorizontalHeaderLabels([
            'Serial Number', 'Product', 'Customer', 'Purchase Date', 
            'Warranty End', 'Status', 'Price', 'Actions'
        ])
        self.warranties_table.setColumnWidth(0, 150)
        self.warranties_table.setColumnWidth(1, 120)
        self.warranties_table.setColumnWidth(2, 120)
        self.warranties_table.setColumnWidth(3, 100)
        self.warranties_table.setColumnWidth(4, 100)
        self.warranties_table.setColumnWidth(5, 80)
        self.warranties_table.setColumnWidth(6, 80)
        self.warranties_table.setColumnWidth(7, 100)
        warranties_layout.addWidget(self.warranties_table)
        
        warranties_widget.setLayout(warranties_layout)
        tabs.addTab(warranties_widget, 'Warranties')
        
        # Products Tab
        products_widget = QWidget()
        products_layout = QVBoxLayout()
        
        product_button_layout = QHBoxLayout()
        new_product_btn = QPushButton('Add New Product')
        new_product_btn.clicked.connect(self.open_new_product_dialog)
        product_button_layout.addWidget(new_product_btn)
        
        refresh_product_btn = QPushButton('Refresh')
        refresh_product_btn.clicked.connect(self.refresh_products)
        product_button_layout.addWidget(refresh_product_btn)
        product_button_layout.addStretch()
        
        products_layout.addLayout(product_button_layout)
        
        self.products_table = QTableWidget()
        self.products_table.setColumnCount(5)
        self.products_table.setHorizontalHeaderLabels([
            'Name', 'Model', 'Category', 'Manufacturer', 'Description'
        ])
        self.products_table.setColumnWidth(0, 150)
        self.products_table.setColumnWidth(1, 100)
        self.products_table.setColumnWidth(2, 100)
        self.products_table.setColumnWidth(3, 120)
        self.products_table.setColumnWidth(4, 250)
        products_layout.addWidget(self.products_table)
        
        products_widget.setLayout(products_layout)
        tabs.addTab(products_widget, 'Products')
        
        # Customers Tab
        customers_widget = QWidget()
        customers_layout = QVBoxLayout()
        
        customer_button_layout = QHBoxLayout()
        new_customer_btn = QPushButton('Add New Customer')
        new_customer_btn.clicked.connect(self.open_new_customer_dialog)
        customer_button_layout.addWidget(new_customer_btn)
        
        refresh_customer_btn = QPushButton('Refresh')
        refresh_customer_btn.clicked.connect(self.refresh_customers)
        customer_button_layout.addWidget(refresh_customer_btn)
        customer_button_layout.addStretch()
        
        customers_layout.addLayout(customer_button_layout)
        
        self.customers_table = QTableWidget()
        self.customers_table.setColumnCount(6)
        self.customers_table.setHorizontalHeaderLabels([
            'Name', 'Email', 'Phone', 'City', 'Country', 'Warranties Count'
        ])
        self.customers_table.setColumnWidth(0, 150)
        self.customers_table.setColumnWidth(1, 150)
        self.customers_table.setColumnWidth(2, 100)
        self.customers_table.setColumnWidth(3, 100)
        self.customers_table.setColumnWidth(4, 100)
        self.customers_table.setColumnWidth(5, 120)
        customers_layout.addWidget(self.customers_table)
        
        customers_widget.setLayout(customers_layout)
        tabs.addTab(customers_widget, 'Customers')
        
        # Invoices Tab
        invoices_widget = QWidget()
        invoices_layout = QVBoxLayout()
        
        invoice_button_layout = QHBoxLayout()
        new_invoice_btn = QPushButton('Create New Invoice')
        new_invoice_btn.clicked.connect(self.open_new_invoice_dialog)
        invoice_button_layout.addWidget(new_invoice_btn)
        
        refresh_invoice_btn = QPushButton('Refresh')
        refresh_invoice_btn.clicked.connect(self.refresh_invoices)
        invoice_button_layout.addWidget(refresh_invoice_btn)
        invoice_button_layout.addStretch()
        
        invoices_layout.addLayout(invoice_button_layout)
        
        self.invoices_table = QTableWidget()
        self.invoices_table.setColumnCount(7)
        self.invoices_table.setHorizontalHeaderLabels([
            'Invoice #', 'Customer', 'Date', 'Due Date', 'Total', 'Status', 'Actions'
        ])
        self.invoices_table.setColumnWidth(0, 100)
        self.invoices_table.setColumnWidth(1, 150)
        self.invoices_table.setColumnWidth(2, 100)
        self.invoices_table.setColumnWidth(3, 100)
        self.invoices_table.setColumnWidth(4, 100)
        self.invoices_table.setColumnWidth(5, 80)
        self.invoices_table.setColumnWidth(6, 120)
        invoices_layout.addWidget(self.invoices_table)
        
        invoices_widget.setLayout(invoices_layout)
        tabs.addTab(invoices_widget, 'Invoices')
        
        # Receipts Tab
        receipts_widget = QWidget()
        receipts_layout = QVBoxLayout()
        
        receipt_button_layout = QHBoxLayout()
        new_receipt_btn = QPushButton('Create New Receipt')
        new_receipt_btn.clicked.connect(self.open_new_receipt_dialog)
        receipt_button_layout.addWidget(new_receipt_btn)
        
        refresh_receipt_btn = QPushButton('Refresh')
        refresh_receipt_btn.clicked.connect(self.refresh_receipts)
        receipt_button_layout.addWidget(refresh_receipt_btn)
        receipt_button_layout.addStretch()
        
        receipts_layout.addLayout(receipt_button_layout)
        
        self.receipts_table = QTableWidget()
        self.receipts_table.setColumnCount(6)
        self.receipts_table.setHorizontalHeaderLabels([
            'Receipt #', 'Invoice #', 'Customer', 'Amount', 'Payment Method', 'Date'
        ])
        self.receipts_table.setColumnWidth(0, 100)
        self.receipts_table.setColumnWidth(1, 100)
        self.receipts_table.setColumnWidth(2, 150)
        self.receipts_table.setColumnWidth(3, 100)
        self.receipts_table.setColumnWidth(4, 120)
        self.receipts_table.setColumnWidth(5, 100)
        receipts_layout.addWidget(self.receipts_table)
        
        receipts_widget.setLayout(receipts_layout)
        tabs.addTab(receipts_widget, 'Receipts')
        
        main_layout.addWidget(tabs)
        
        central_widget.setLayout(main_layout)
        
        # Status bar
        self.statusBar().showMessage('Ready')
    
    def open_qr_scanner(self):
        """Open QR code scanner dialog"""
        scanner = QRScannerDialog(self)
        scanner.qr_scanned.connect(self.on_qr_scanned)
        scanner.exec()
    
    def on_qr_scanned(self, qr_data: str):
        """Handle scanned QR code"""
        self.search_serial_input.setText(qr_data)
        self.search_warranty()
    
    def search_warranty(self):
        """Search warranty by serial number"""
        serial = self.search_serial_input.text().strip()
        if not serial:
            QMessageBox.warning(self, 'Error', 'Please enter a serial number')
            return
        
        try:
            warranty = self.api_client.get_warranty_by_serial(serial)
            
            # Display warranty details
            details = f"""
Warranty Details:
═══════════════════════════════════════════
Serial Number: {warranty['serial_number']}
Product: {warranty['product']['name']} ({warranty['product']['model']})
Customer: {warranty['customer']['name']}
Purchase Date: {warranty['purchase_date']}
Warranty End: {warranty['warranty_end_date']}
Status: {warranty['status']}
Price: ${warranty['purchase_price']} {warranty['currency']}
═══════════════════════════════════════════
            """
            
            QMessageBox.information(self, 'Warranty Found', details)
        
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Warranty not found: {str(e)}')
    
    def refresh_warranties(self):
        """Refresh warranties table"""
        try:
            self.statusBar().showMessage('Loading warranties...')
            
            # Get all warranties (in a real app, you'd use pagination)
            self.api_client.list_products()  # Ensure products are loaded
            self.api_client.list_customers()  # Ensure customers are loaded
            
            # For demo, we'll show an empty table since we need to implement list all
            self.warranties_table.setRowCount(0)
            
            self.statusBar().showMessage('Warranties loaded')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load warranties: {str(e)}')
            self.statusBar().showMessage('Error loading warranties')
    
    def refresh_products(self):
        """Refresh products table"""
        try:
            self.statusBar().showMessage('Loading products...')
            
            products = self.api_client.list_products()
            self.products_table.setRowCount(len(products))
            
            for row, product in enumerate(products):
                self.products_table.setItem(row, 0, QTableWidgetItem(product['name']))
                self.products_table.setItem(row, 1, QTableWidgetItem(product['model']))
                self.products_table.setItem(row, 2, QTableWidgetItem(product.get('category', '-')))
                self.products_table.setItem(row, 3, QTableWidgetItem(product.get('manufacturer', '-')))
                self.products_table.setItem(row, 4, QTableWidgetItem(product.get('description', '-')[:50]))
            
            self.statusBar().showMessage(f'Products loaded ({len(products)} items)')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load products: {str(e)}')
            self.statusBar().showMessage('Error loading products')
    
    def refresh_customers(self):
        """Refresh customers table"""
        try:
            self.statusBar().showMessage('Loading customers...')
            
            customers = self.api_client.list_customers()
            self.customers_table.setRowCount(len(customers))
            
            for row, customer in enumerate(customers):
                self.customers_table.setItem(row, 0, QTableWidgetItem(customer['name']))
                self.customers_table.setItem(row, 1, QTableWidgetItem(customer.get('email', '-')))
                self.customers_table.setItem(row, 2, QTableWidgetItem(customer.get('phone', '-')))
                self.customers_table.setItem(row, 3, QTableWidgetItem(customer.get('city', '-')))
                self.customers_table.setItem(row, 4, QTableWidgetItem(customer.get('country', '-')))
                self.customers_table.setItem(row, 5, QTableWidgetItem(str(len(customer.get('warranties', [])))))
            
            self.statusBar().showMessage(f'Customers loaded ({len(customers)} items)')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load customers: {str(e)}')
            self.statusBar().showMessage('Error loading customers')
    
    def refresh_invoices(self):
        """Refresh invoices table"""
        try:
            self.statusBar().showMessage('Loading invoices...')
            
            invoices = self.api_client.list_invoices()
            self.invoices_table.setRowCount(len(invoices))
            
            for row, invoice in enumerate(invoices):
                customer_name = invoice.get('customer', {}).get('name', 'Unknown')
                self.invoices_table.setItem(row, 0, QTableWidgetItem(invoice.get('invoice_number', '-')))
                self.invoices_table.setItem(row, 1, QTableWidgetItem(customer_name))
                self.invoices_table.setItem(row, 2, QTableWidgetItem(invoice.get('invoice_date', '-')[:10]))
                self.invoices_table.setItem(row, 3, QTableWidgetItem(invoice.get('due_date', '-')[:10]))
                self.invoices_table.setItem(row, 4, QTableWidgetItem(f"${invoice.get('total_amount', 0):.2f}"))
                self.invoices_table.setItem(row, 5, QTableWidgetItem(invoice.get('invoice_status', 'draft').title()))
                
                # Actions button
                actions_widget = QWidget()
                actions_layout = QHBoxLayout()
                actions_layout.setContentsMargins(0, 0, 0, 0)
                
                view_btn = QPushButton('View')
                view_btn.setFixedWidth(50)
                view_btn.clicked.connect(lambda checked, iid=invoice['id']: self.view_invoice(iid))
                actions_layout.addWidget(view_btn)
                
                actions_widget.setLayout(actions_layout)
                self.invoices_table.setCellWidget(row, 6, actions_widget)
            
            self.statusBar().showMessage(f'Invoices loaded ({len(invoices)} items)')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load invoices: {str(e)}')
            self.statusBar().showMessage('Error loading invoices')
    
    def refresh_receipts(self):
        """Refresh receipts table"""
        try:
            self.statusBar().showMessage('Loading receipts...')
            
            receipts = self.api_client.list_receipts()
            self.receipts_table.setRowCount(len(receipts))
            
            for row, receipt in enumerate(receipts):
                customer_name = receipt.get('invoice', {}).get('customer', {}).get('name', 'Unknown')
                invoice_number = receipt.get('invoice', {}).get('invoice_number', '-')
                
                self.receipts_table.setItem(row, 0, QTableWidgetItem(receipt.get('receipt_number', '-')))
                self.receipts_table.setItem(row, 1, QTableWidgetItem(invoice_number))
                self.receipts_table.setItem(row, 2, QTableWidgetItem(customer_name))
                self.receipts_table.setItem(row, 3, QTableWidgetItem(f"${receipt.get('payment_amount', 0):.2f}"))
                self.receipts_table.setItem(row, 4, QTableWidgetItem(receipt.get('payment_method', '-')))
                self.receipts_table.setItem(row, 5, QTableWidgetItem(receipt.get('created_at', '-')[:10]))
            
            self.statusBar().showMessage(f'Receipts loaded ({len(receipts)} items)')
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load receipts: {str(e)}')
            self.statusBar().showMessage('Error loading receipts')
    
    def view_invoice(self, invoice_id: str):
        """View invoice details"""
        try:
            invoice = self.api_client.get_invoice(invoice_id)
            
            # Show invoice details in a message box for now
            details = f"""
Invoice Details:
═══════════════════════════════════════════
Invoice #: {invoice.get('invoice_number', 'N/A')}
Customer: {invoice.get('customer', {}).get('name', 'N/A')}
Date: {invoice.get('invoice_date', 'N/A')}
Due Date: {invoice.get('due_date', 'N/A')}
Total: ${invoice.get('total_amount', 0):.2f}
Status: {invoice.get('invoice_status', 'N/A')}

Line Items:
"""
            for item in invoice.get('line_items', []):
                details += f"• {item.get('description', 'Item')}: ${item.get('total', 0):.2f}\n"
            
            QMessageBox.information(self, 'Invoice Details', details)
            
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to load invoice: {str(e)}')
    
    def open_new_warranty_dialog(self):
        """Open new warranty creation dialog"""
        dialog = NewWarrantyDialog(self.api_client, self)
        dialog.warranty_created.connect(self.on_warranty_created)
        dialog.exec()
    
    def on_warranty_created(self, warranty: dict):
        """Handle warranty creation"""
        self.refresh_warranties()
    
    def open_new_product_dialog(self):
        """Open new product creation dialog"""
        dialog = NewProductDialog(self.api_client, self)
        dialog.product_created.connect(self.on_product_created)
        dialog.exec()
    
    def on_product_created(self, product: dict):
        """Handle product creation"""
        self.refresh_products()
    
    def open_new_customer_dialog(self):
        """Open new customer creation dialog"""
        dialog = NewCustomerDialog(self.api_client, self)
        dialog.customer_created.connect(self.on_customer_created)
        dialog.exec()
    
    def on_customer_created(self, customer: dict):
        """Handle customer creation"""
        self.refresh_customers()
    
    def open_new_invoice_dialog(self):
        """Open new invoice creation dialog"""
        dialog = NewInvoiceDialog(self.api_client, self)
        dialog.invoice_created.connect(self.on_invoice_created)
        dialog.exec()
    
    def on_invoice_created(self, invoice: dict):
        """Handle invoice creation"""
        self.refresh_invoices()
    
    def open_new_receipt_dialog(self):
        """Open new receipt creation dialog"""
        dialog = NewReceiptDialog(self.api_client, self)
        dialog.receipt_created.connect(self.on_receipt_created)
        dialog.exec()
    
    def on_receipt_created(self, receipt: dict):
        """Handle receipt creation"""
        self.refresh_receipts()
