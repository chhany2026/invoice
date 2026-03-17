#!/usr/bin/env python
"""
Upgrade database schema to add new payment method columns
"""

from backend.app import create_app, db
from backend.app.models_invoice import Payment, CompanySettings
import sys

def upgrade_database():
    """Add missing columns to payments and company_settings tables"""
    app = create_app()
    with app.app_context():
        try:
            # Check if columns exist, if not, add them
            inspector = db.inspect(db.engine)
            payment_columns = [col['name'] for col in inspector.get_columns('payments')]
            company_columns = [col['name'] for col in inspector.get_columns('company_settings')]
            
            print("Current Payment table columns:", payment_columns)
            print("Current Company Settings table columns:", company_columns)
            
            # Add missing columns using raw SQL
            with db.engine.begin() as conn:
                # Add to payments table if missing
                if 'bank_name' not in payment_columns:
                    print("\nAdding bank_name to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN bank_name VARCHAR(255)'))
                
                if 'bank_account_holder' not in payment_columns:
                    print("Adding bank_account_holder to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN bank_account_holder VARCHAR(255)'))
                
                if 'bank_account_number' not in payment_columns:
                    print("Adding bank_account_number to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN bank_account_number VARCHAR(100)'))
                
                if 'bank_routing_number' not in payment_columns:
                    print("Adding bank_routing_number to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN bank_routing_number VARCHAR(100)'))
                
                if 'khqr_code' not in payment_columns:
                    print("Adding khqr_code to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN khqr_code TEXT'))
                
                if 'cash_currency' not in payment_columns:
                    print("Adding cash_currency to payments...")
                    conn.execute(db.text('ALTER TABLE payments ADD COLUMN cash_currency VARCHAR(3)'))
                
                # Add to company_settings table if missing
                if 'logo_base64' not in company_columns:
                    print("\nAdding logo_base64 to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN logo_base64 TEXT'))
                
                if 'khqr_merchant_id' not in company_columns:
                    print("Adding khqr_merchant_id to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN khqr_merchant_id VARCHAR(255)'))
                
                if 'khqr_code_base64' not in company_columns:
                    print("Adding khqr_code_base64 to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN khqr_code_base64 TEXT'))
                
                if 'aba_account_number' not in company_columns:
                    print("Adding aba_account_number to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN aba_account_number VARCHAR(100)'))
                
                if 'aba_account_holder' not in company_columns:
                    print("Adding aba_account_holder to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN aba_account_holder VARCHAR(255)'))
                
                if 'acleda_account_number' not in company_columns:
                    print("Adding acleda_account_number to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN acleda_account_number VARCHAR(100)'))
                
                if 'acleda_account_holder' not in company_columns:
                    print("Adding acleda_account_holder to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN acleda_account_holder VARCHAR(255)'))
                
                if 'preferred_payment_methods' not in company_columns:
                    print("Adding preferred_payment_methods to company_settings...")
                    conn.execute(db.text("ALTER TABLE company_settings ADD COLUMN preferred_payment_methods TEXT DEFAULT 'cash,bank'"))
                
                if 'invoice_footer_text' not in company_columns:
                    print("Adding invoice_footer_text to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN invoice_footer_text TEXT'))
                
                if 'receipt_footer_text' not in company_columns:
                    print("Adding receipt_footer_text to company_settings...")
                    conn.execute(db.text('ALTER TABLE company_settings ADD COLUMN receipt_footer_text TEXT'))
            
            print("\n✓ Database upgrade completed successfully!")
            return True
        except Exception as e:
            print(f"\n✗ Error during upgrade: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == '__main__':
    success = upgrade_database()
    sys.exit(0 if success else 1)
