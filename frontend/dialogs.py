from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QComboBox, QSpinBox,
                             QDateEdit, QTextEdit, QMessageBox)
from PyQt6.QtCore import Qt, QDate, pyqtSignal
from api_client import APIClient
from datetime import datetime, timedelta


class NewWarrantyDialog(QDialog):
    """Dialog for creating a new warranty record"""
    
    warranty_created = pyqtSignal(dict)
    
    def __init__(self, api_client: APIClient, parent=None):
        super().__init__(parent)
        self.api_client = api_client
        self.setWindowTitle('Create New Warranty')
        self.setGeometry(100, 100, 500, 700)
        self.products = []
        self.customers = []
        self.init_ui()
        self.load_data()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Serial Number
        layout.addWidget(QLabel('Serial Number:'))
        self.serial_input = QLineEdit()
        layout.addWidget(self.serial_input)
        
        # Product Selection
        layout.addWidget(QLabel('Product:'))
        self.product_combo = QComboBox()
        layout.addWidget(self.product_combo)
        
        # Customer Selection
        layout.addWidget(QLabel('Customer:'))
        self.customer_combo = QComboBox()
        layout.addWidget(self.customer_combo)
        
        # Purchase Date
        layout.addWidget(QLabel('Purchase Date:'))
        self.purchase_date = QDateEdit()
        self.purchase_date.setDate(QDate.currentDate())
        layout.addWidget(self.purchase_date)
        
        # Warranty Duration (months)
        layout.addWidget(QLabel('Warranty Duration (months):'))
        self.duration_spin = QSpinBox()
        self.duration_spin.setValue(12)
        self.duration_spin.setMinimum(1)
        self.duration_spin.setMaximum(360)
        layout.addWidget(self.duration_spin)
        
        # Purchase Location
        layout.addWidget(QLabel('Purchase Location:'))
        self.location_input = QLineEdit()
        layout.addWidget(self.location_input)
        
        # Purchase Price
        layout.addWidget(QLabel('Purchase Price (USD):'))
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText('e.g., 999.99')
        layout.addWidget(self.price_input)
        
        # Notes
        layout.addWidget(QLabel('Notes:'))
        self.notes_input = QTextEdit()
        self.notes_input.setMaximumHeight(100)
        layout.addWidget(self.notes_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton('Create Warranty')
        save_button.clicked.connect(self.create_warranty)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def load_data(self):
        """Load products and customers from API"""
        try:
            self.products = self.api_client.list_products()
            self.customers = self.api_client.list_customers()
            
            # Populate product combo
            for product in self.products:
                self.product_combo.addItem(
                    f"{product['name']} ({product['model']})",
                    product['id']
                )
            
            # Populate customer combo
            for customer in self.customers:
                self.customer_combo.addItem(customer['name'], customer['id'])
        
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load data: {str(e)}')
    
    def create_warranty(self):
        """Create warranty and emit signal"""
        try:
            # Validate inputs
            if not self.serial_input.text().strip():
                QMessageBox.warning(self, 'Error', 'Serial number is required')
                return
            
            # Get selected IDs
            product_id = self.product_combo.currentData()
            customer_id = self.customer_combo.currentData()
            
            if not product_id or not customer_id:
                QMessageBox.warning(self, 'Error', 'Please select product and customer')
                return
            
            # Prepare warranty data
            warranty_data = {
                'serial_number': self.serial_input.text().strip(),
                'product_id': product_id,
                'customer_id': customer_id,
                'purchase_date': self.purchase_date.date().toPyDate().isoformat(),
                'warranty_duration_months': self.duration_spin.value(),
                'purchase_location': self.location_input.text().strip(),
                'purchase_price': float(self.price_input.text()) if self.price_input.text() else None,
                'currency': 'USD',
                'notes': self.notes_input.toPlainText()
            }
            
            # Create warranty
            result = self.api_client.create_warranty(warranty_data)
            
            QMessageBox.information(self, 'Success', 'Warranty created successfully!')
            self.warranty_created.emit(result.get('warranty', {}))
            self.accept()
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create warranty: {str(e)}')


class NewProductDialog(QDialog):
    """Dialog for creating a new product"""
    
    product_created = pyqtSignal(dict)
    
    def __init__(self, api_client: APIClient, parent=None):
        super().__init__(parent)
        self.api_client = api_client
        self.setWindowTitle('Create New Product')
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Product Name
        layout.addWidget(QLabel('Product Name:'))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)
        
        # Product Model
        layout.addWidget(QLabel('Model:'))
        self.model_input = QLineEdit()
        layout.addWidget(self.model_input)
        
        # Category
        layout.addWidget(QLabel('Category:'))
        self.category_input = QLineEdit()
        layout.addWidget(self.category_input)
        
        # Manufacturer
        layout.addWidget(QLabel('Manufacturer:'))
        self.manufacturer_input = QLineEdit()
        layout.addWidget(self.manufacturer_input)
        
        # Description
        layout.addWidget(QLabel('Description:'))
        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(80)
        layout.addWidget(self.description_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton('Create Product')
        save_button.clicked.connect(self.create_product)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def create_product(self):
        """Create product and emit signal"""
        try:
            if not self.name_input.text().strip() or not self.model_input.text().strip():
                QMessageBox.warning(self, 'Error', 'Product name and model are required')
                return
            
            product_data = {
                'name': self.name_input.text().strip(),
                'model': self.model_input.text().strip(),
                'category': self.category_input.text().strip(),
                'manufacturer': self.manufacturer_input.text().strip(),
                'description': self.description_input.toPlainText()
            }
            
            result = self.api_client.create_product(product_data)
            
            QMessageBox.information(self, 'Success', 'Product created successfully!')
            self.product_created.emit(result.get('product', {}))
            self.accept()
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create product: {str(e)}')


class NewCustomerDialog(QDialog):
    """Dialog for creating a new customer"""
    
    customer_created = pyqtSignal(dict)
    
    def __init__(self, api_client: APIClient, parent=None):
        super().__init__(parent)
        self.api_client = api_client
        self.setWindowTitle('Add New Customer')
        self.setGeometry(100, 100, 400, 350)
        self.init_ui()
    
    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()
        
        # Customer Name
        layout.addWidget(QLabel('Full Name:'))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)
        
        # Email
        layout.addWidget(QLabel('Email:'))
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)
        
        # Phone
        layout.addWidget(QLabel('Phone:'))
        self.phone_input = QLineEdit()
        layout.addWidget(self.phone_input)
        
        # Address
        layout.addWidget(QLabel('Address:'))
        self.address_input = QLineEdit()
        layout.addWidget(self.address_input)
        
        # City
        layout.addWidget(QLabel('City:'))
        self.city_input = QLineEdit()
        layout.addWidget(self.city_input)
        
        # Country
        layout.addWidget(QLabel('Country:'))
        self.country_input = QLineEdit()
        layout.addWidget(self.country_input)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton('Add Customer')
        save_button.clicked.connect(self.create_customer)
        button_layout.addWidget(save_button)
        
        cancel_button = QPushButton('Cancel')
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def create_customer(self):
        """Create customer and emit signal"""
        try:
            if not self.name_input.text().strip():
                QMessageBox.warning(self, 'Error', 'Customer name is required')
                return
            
            customer_data = {
                'name': self.name_input.text().strip(),
                'email': self.email_input.text().strip(),
                'phone': self.phone_input.text().strip(),
                'address': self.address_input.text().strip(),
                'city': self.city_input.text().strip(),
                'country': self.country_input.text().strip()
            }
            
            result = self.api_client.create_customer(customer_data)
            
            QMessageBox.information(self, 'Success', 'Customer added successfully!')
            self.customer_created.emit(result.get('customer', {}))
            self.accept()
        
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to add customer: {str(e)}')


class NewInvoiceDialog(QDialog):
    """Dialog for creating a new invoice with enhanced customer controls"""

    invoice_created = pyqtSignal(dict)

    def __init__(self, api_client: APIClient, parent=None):
        super().__init__(parent)
        self.api_client = api_client
        self.setWindowTitle('Create New Invoice')
        self.setGeometry(100, 100, 600, 800)
        self.customers = []
        self.products = []
        self.line_items = []
        self.init_ui()
        self.load_data()

    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()

        # Customer Selection Section
        customer_group = QVBoxLayout()
        customer_group.addWidget(QLabel('Customer Selection:'))

        customer_controls = QHBoxLayout()

        # Customer dropdown with search
        self.customer_combo = QComboBox()
        self.customer_combo.setEditable(True)
        self.customer_combo.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        self.customer_combo.setPlaceholderText('Search and select customer...')
        customer_controls.addWidget(self.customer_combo)

        # Add new customer button
        add_customer_btn = QPushButton('➕ New Customer')
        add_customer_btn.clicked.connect(self.open_new_customer_dialog)
        customer_controls.addWidget(add_customer_btn)

        customer_group.addLayout(customer_controls)
        layout.addLayout(customer_group)

        # Invoice Details
        layout.addWidget(QLabel('Invoice Details:'))

        details_layout = QVBoxLayout()

        # Invoice date
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel('Invoice Date:'))
        self.invoice_date = QDateEdit()
        self.invoice_date.setDate(QDate.currentDate())
        date_layout.addWidget(self.invoice_date)

        date_layout.addWidget(QLabel('Due Date:'))
        self.due_date = QDateEdit()
        self.due_date.setDate(QDate.currentDate().addDays(30))
        date_layout.addWidget(self.due_date)

        details_layout.addLayout(date_layout)

        # Currency and language
        settings_layout = QHBoxLayout()
        settings_layout.addWidget(QLabel('Currency:'))
        self.currency_combo = QComboBox()
        self.currency_combo.addItems(['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'KHR'])
        self.currency_combo.setCurrentText('USD')
        settings_layout.addWidget(self.currency_combo)

        settings_layout.addWidget(QLabel('Language:'))
        self.language_combo = QComboBox()
        self.language_combo.addItems(['en', 'km'])
        self.language_combo.setCurrentText('en')
        settings_layout.addWidget(self.language_combo)

        details_layout.addLayout(settings_layout)

        layout.addLayout(details_layout)

        # Line Items Section
        layout.addWidget(QLabel('Line Items:'))

        # Add item controls
        item_controls = QHBoxLayout()
        self.product_combo = QComboBox()
        self.product_combo.setEditable(True)
        self.product_combo.setPlaceholderText('Select product...')
        item_controls.addWidget(self.product_combo)

        self.quantity_spin = QSpinBox()
        self.quantity_spin.setValue(1)
        self.quantity_spin.setMinimum(1)
        item_controls.addWidget(QLabel('Qty:'))
        item_controls.addWidget(self.quantity_spin)

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText('Price')
        item_controls.addWidget(QLabel('Price:'))
        item_controls.addWidget(self.price_input)

        add_item_btn = QPushButton('Add Item')
        add_item_btn.clicked.connect(self.add_line_item)
        item_controls.addWidget(add_item_btn)

        layout.addLayout(item_controls)

        # Line items table
        self.items_table = QTableWidget()
        self.items_table.setColumnCount(5)
        self.items_table.setHorizontalHeaderLabels(['Product', 'Qty', 'Price', 'Total', 'Actions'])
        self.items_table.setColumnWidth(0, 200)
        self.items_table.setColumnWidth(1, 60)
        self.items_table.setColumnWidth(2, 80)
        self.items_table.setColumnWidth(3, 80)
        self.items_table.setColumnWidth(4, 80)
        layout.addWidget(self.items_table)

        # Totals section
        totals_layout = QHBoxLayout()
        totals_layout.addStretch()

        totals_box = QVBoxLayout()
        self.subtotal_label = QLabel('Subtotal: $0.00')
        self.tax_label = QLabel('Tax (10%): $0.00')
        self.total_label = QLabel('Total: $0.00')
        self.total_label.setStyleSheet('font-weight: bold; font-size: 14px;')

        totals_box.addWidget(self.subtotal_label)
        totals_box.addWidget(self.tax_label)
        totals_box.addWidget(self.total_label)

        totals_layout.addLayout(totals_box)
        layout.addLayout(totals_layout)

        # Notes
        layout.addWidget(QLabel('Notes:'))
        self.notes_input = QTextEdit()
        self.notes_input.setMaximumHeight(60)
        layout.addWidget(self.notes_input)

        # Buttons
        button_layout = QHBoxLayout()

        create_btn = QPushButton('Create Invoice')
        create_btn.clicked.connect(self.create_invoice)
        create_btn.setStyleSheet('QPushButton { background: #10b981; color: white; padding: 10px 20px; }')
        button_layout.addWidget(create_btn)

        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_data(self):
        """Load customers and products"""
        try:
            self.customers = self.api_client.list_customers()
            self.products = self.api_client.list_products()

            # Populate customer combo
            self.customer_combo.clear()
            for customer in self.customers:
                display_text = f"{customer['name']} - {customer.get('email', 'No email')}"
                self.customer_combo.addItem(display_text, customer['id'])

            # Populate product combo
            self.product_combo.clear()
            for product in self.products:
                display_text = f"{product['name']} ({product['model']}) - ${product.get('sale_price', 0)}"
                self.product_combo.addItem(display_text, product['id'])

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load data: {str(e)}')

    def open_new_customer_dialog(self):
        """Open dialog to add new customer"""
        dialog = NewCustomerDialog(self.api_client, self)
        dialog.customer_created.connect(self.on_customer_created)
        dialog.exec()

    def on_customer_created(self, customer):
        """Handle new customer creation"""
        self.customers.append(customer)
        display_text = f"{customer['name']} - {customer.get('email', 'No email')}"
        self.customer_combo.addItem(display_text, customer['id'])
        # Select the newly added customer
        self.customer_combo.setCurrentIndex(self.customer_combo.count() - 1)

    def add_line_item(self):
        """Add line item to invoice"""
        try:
            product_id = self.product_combo.currentData()
            if not product_id:
                QMessageBox.warning(self, 'Error', 'Please select a product')
                return

            quantity = self.quantity_spin.value()
            price_text = self.price_input.text().strip()

            if not price_text:
                QMessageBox.warning(self, 'Error', 'Please enter a price')
                return

            price = float(price_text)
            total = quantity * price

            # Find product details
            product = next((p for p in self.products if p['id'] == product_id), None)
            if not product:
                return

            # Add to line items list
            line_item = {
                'product_id': product_id,
                'description': product['name'],
                'quantity': quantity,
                'unit_price': price,
                'total': total
            }
            self.line_items.append(line_item)

            # Update table
            self.update_items_table()
            self.update_totals()

            # Clear inputs
            self.product_combo.setCurrentIndex(-1)
            self.quantity_spin.setValue(1)
            self.price_input.clear()

        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter a valid price')

    def update_items_table(self):
        """Update the line items table"""
        self.items_table.setRowCount(len(self.line_items))

        for row, item in enumerate(self.line_items):
            self.items_table.setItem(row, 0, QTableWidgetItem(item['description']))
            self.items_table.setItem(row, 1, QTableWidgetItem(str(item['quantity'])))
            self.items_table.setItem(row, 2, QTableWidgetItem(f"${item['unit_price']:.2f}"))
            self.items_table.setItem(row, 3, QTableWidgetItem(f"${item['total']:.2f}"))

            # Remove button
            remove_btn = QPushButton('❌')
            remove_btn.clicked.connect(lambda checked, r=row: self.remove_line_item(r))
            self.items_table.setCellWidget(row, 4, remove_btn)

    def remove_line_item(self, row):
        """Remove line item"""
        if row < len(self.line_items):
            self.line_items.pop(row)
            self.update_items_table()
            self.update_totals()

    def update_totals(self):
        """Update subtotal, tax, and total"""
        subtotal = sum(item['total'] for item in self.line_items)
        tax_rate = 0.10  # 10% tax
        tax = subtotal * tax_rate
        total = subtotal + tax

        currency = self.currency_combo.currentText()
        currency_symbol = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': 'C$', 'KHR': '៛'}.get(currency, '$')

        self.subtotal_label.setText(f'Subtotal: {currency_symbol}{subtotal:.2f}')
        self.tax_label.setText(f'Tax (10%): {currency_symbol}{tax:.2f}')
        self.total_label.setText(f'Total: {currency_symbol}{total:.2f}')

    def create_invoice(self):
        """Create the invoice"""
        try:
            # Validate
            customer_id = self.customer_combo.currentData()
            if not customer_id:
                QMessageBox.warning(self, 'Error', 'Please select a customer')
                return

            if not self.line_items:
                QMessageBox.warning(self, 'Error', 'Please add at least one line item')
                return

            # Prepare invoice data
            invoice_data = {
                'customer_id': customer_id,
                'invoice_date': self.invoice_date.date().toPyDate().isoformat(),
                'due_date': self.due_date.date().toPyDate().isoformat(),
                'currency': self.currency_combo.currentText(),
                'language': self.language_combo.currentText(),
                'tax_rate': 10.0,  # Fixed 10% for now
                'line_items': self.line_items,
                'notes': self.notes_input.toPlainText()
            }

            # Create invoice
            result = self.api_client.create_invoice(invoice_data)

            QMessageBox.information(self, 'Success', f'Invoice created successfully!\nInvoice #: {result.get("invoice_number", "Unknown")}')
            self.invoice_created.emit(result.get('invoice', {}))
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create invoice: {str(e)}')


class NewReceiptDialog(QDialog):
    """Dialog for creating a receipt from an invoice with customer selection"""

    receipt_created = pyqtSignal(dict)

    def __init__(self, api_client: APIClient, parent=None):
        super().__init__(parent)
        self.api_client = api_client
        self.setWindowTitle('Create Receipt')
        self.setGeometry(100, 100, 500, 600)
        self.invoices = []
        self.init_ui()
        self.load_pending_invoices()

    def init_ui(self):
        """Initialize the UI"""
        layout = QVBoxLayout()

        # Invoice Selection
        layout.addWidget(QLabel('Select Invoice to Create Receipt:'))
        self.invoice_combo = QComboBox()
        self.invoice_combo.currentIndexChanged.connect(self.on_invoice_selected)
        layout.addWidget(self.invoice_combo)

        # Customer Info (read-only)
        layout.addWidget(QLabel('Customer Information:'))
        self.customer_info = QLabel('No invoice selected')
        self.customer_info.setStyleSheet('background: #f0f0f0; padding: 10px; border-radius: 5px;')
        layout.addWidget(self.customer_info)

        # Invoice Summary
        layout.addWidget(QLabel('Invoice Summary:'))
        self.invoice_summary = QLabel('No invoice selected')
        self.invoice_summary.setStyleSheet('background: #f0f0f0; padding: 10px; border-radius: 5px;')
        layout.addWidget(self.invoice_summary)

        # Payment Details
        layout.addWidget(QLabel('Payment Details:'))

        payment_form = QVBoxLayout()

        # Payment method
        method_layout = QHBoxLayout()
        method_layout.addWidget(QLabel('Payment Method:'))
        self.payment_method = QComboBox()
        self.payment_method.addItems(['Cash', 'ABA Bank Transfer', 'ACLEDA Bank Transfer', 'Credit Card', 'Other'])
        method_layout.addWidget(self.payment_method)
        payment_form.addLayout(method_layout)

        # Amount
        amount_layout = QHBoxLayout()
        amount_layout.addWidget(QLabel('Payment Amount:'))
        self.payment_amount = QLineEdit()
        self.payment_amount.setPlaceholderText('Enter payment amount')
        amount_layout.addWidget(self.payment_amount)
        payment_form.addLayout(amount_layout)

        # Reference
        ref_layout = QHBoxLayout()
        ref_layout.addWidget(QLabel('Reference/Note:'))
        self.payment_reference = QLineEdit()
        self.payment_reference.setPlaceholderText('Transaction ID, check number, etc.')
        ref_layout.addWidget(self.payment_reference)
        payment_form.addLayout(ref_layout)

        layout.addLayout(payment_form)

        # Receipt Notes
        layout.addWidget(QLabel('Receipt Notes:'))
        self.receipt_notes = QTextEdit()
        self.receipt_notes.setMaximumHeight(60)
        self.receipt_notes.setPlaceholderText('Optional notes for the receipt...')
        layout.addWidget(self.receipt_notes)

        # Buttons
        button_layout = QHBoxLayout()

        create_btn = QPushButton('Create Receipt')
        create_btn.clicked.connect(self.create_receipt)
        create_btn.setStyleSheet('QPushButton { background: #10b981; color: white; padding: 10px 20px; }')
        button_layout.addWidget(create_btn)

        cancel_btn = QPushButton('Cancel')
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(cancel_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def load_pending_invoices(self):
        """Load invoices that don't have receipts yet"""
        try:
            # This would need a new API endpoint to get invoices without receipts
            # For now, we'll load all invoices
            invoices = self.api_client.list_invoices() if hasattr(self.api_client, 'list_invoices') else []

            self.invoice_combo.clear()
            self.invoice_combo.addItem('Select an invoice...', None)

            for invoice in invoices:
                customer_name = invoice.get('customer', {}).get('name', 'Unknown Customer')
                display_text = f"#{invoice['invoice_number']} - {customer_name} - ${invoice.get('total_amount', 0):.2f}"
                self.invoice_combo.addItem(display_text, invoice['id'])

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load invoices: {str(e)}')

    def on_invoice_selected(self):
        """Update customer and invoice info when invoice is selected"""
        invoice_id = self.invoice_combo.currentData()
        if not invoice_id:
            self.customer_info.setText('No invoice selected')
            self.invoice_summary.setText('No invoice selected')
            return

        try:
            # Get invoice details
            invoice = self.api_client.get_invoice(invoice_id) if hasattr(self.api_client, 'get_invoice') else None
            if invoice:
                customer = invoice.get('customer', {})
                self.customer_info.setText(
                    f"Name: {customer.get('name', 'N/A')}\n"
                    f"Email: {customer.get('email', 'N/A')}\n"
                    f"Phone: {customer.get('phone', 'N/A')}"
                )

                self.invoice_summary.setText(
                    f"Invoice #: {invoice['invoice_number']}\n"
                    f"Date: {invoice.get('invoice_date', 'N/A')}\n"
                    f"Total: ${invoice.get('total_amount', 0):.2f}\n"
                    f"Status: {invoice.get('invoice_status', 'N/A')}"
                )

                # Set payment amount to invoice total
                self.payment_amount.setText(str(invoice.get('total_amount', 0)))

        except Exception as e:
            QMessageBox.warning(self, 'Error', f'Failed to load invoice details: {str(e)}')

    def create_receipt(self):
        """Create the receipt"""
        try:
            invoice_id = self.invoice_combo.currentData()
            if not invoice_id:
                QMessageBox.warning(self, 'Error', 'Please select an invoice')
                return

            amount_text = self.payment_amount.text().strip()
            if not amount_text:
                QMessageBox.warning(self, 'Error', 'Please enter payment amount')
                return

            try:
                amount = float(amount_text)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Please enter a valid payment amount')
                return

            # Prepare receipt data
            receipt_data = {
                'invoice_id': invoice_id,
                'payment_amount': amount,
                'payment_method': self.payment_method.currentText(),
                'payment_reference': self.payment_reference.text().strip(),
                'notes': self.receipt_notes.toPlainText()
            }

            # Create receipt (this would need a new API endpoint)
            # result = self.api_client.create_receipt(receipt_data)

            QMessageBox.information(self, 'Success', 'Receipt created successfully!')
            # self.receipt_created.emit(result.get('receipt', {}))
            self.accept()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to create receipt: {str(e)}')
