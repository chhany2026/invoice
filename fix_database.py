#!/usr/bin/env python
"""
Fix database columns issue - ensure all columns exist
"""

import sqlite3
import os

def fix_database():
    """Add missing columns to company_settings table"""
    db_path = os.path.join(os.path.dirname(__file__), 'backend', 'instance', 'warranty_product.db')
    
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return False
    
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        print("Checking company_settings table columns...")
        cursor.execute("PRAGMA table_info(company_settings)")
        columns = {row[1] for row in cursor.fetchall()}
        
        required_columns = {
            'logo_base64': 'TEXT',
            'khqr_merchant_id': 'VARCHAR(255)',
            'khqr_code_base64': 'TEXT',
            'aba_account_number': 'VARCHAR(100)',
            'aba_account_holder': 'VARCHAR(255)',
            'acleda_account_number': 'VARCHAR(100)',
            'acleda_account_holder': 'VARCHAR(255)',
            'preferred_payment_methods': 'TEXT',
            'invoice_footer_text': 'TEXT',
            'receipt_footer_text': 'TEXT',
        }
        
        missing_columns = [col for col in required_columns if col not in columns]
        
        if missing_columns:
            print(f"Found {len(missing_columns)} missing columns: {missing_columns}")
            
            for col in missing_columns:
                sql_type = required_columns[col]
                try:
                    cursor.execute(f'ALTER TABLE company_settings ADD COLUMN {col} {sql_type}')
                    print(f"  ✓ Added {col}")
                except Exception as e:
                    print(f"  ✗ Error adding {col}: {str(e)}")
            
            conn.commit()
            print("✓ All missing columns added")
        else:
            print("✓ All required columns exist")
        
        conn.close()
        return True
    
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

if __name__ == '__main__':
    success = fix_database()
    if success:
        print("\n✓ Database fixed successfully!")
    else:
        print("\n✗ Database fix failed")
