#!/usr/bin/env python
"""
Fix missing columns in payments table
"""
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), 'backend', 'instance', 'warranty_product.db')

# Try alternate path if not found
if not os.path.exists(db_path):
    db_path = os.path.join(os.path.dirname(__file__), 'backend', 'warranty_product.db')

if not os.path.exists(db_path):
    print(f"❌ Database not found at {db_path}")
    exit(1)

print(f"📦 Connecting to database: {db_path}")

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get existing columns in payments table
    cursor.execute("PRAGMA table_info(payments)")
    existing_columns = {row[1] for row in cursor.fetchall()}
    print(f"\n📋 Existing columns in payments table: {existing_columns}")
    
    # Define columns to add
    columns_to_add = {
        'bank_name': 'VARCHAR(255)',
        'bank_account_holder': 'VARCHAR(255)',
        'bank_account_number': 'VARCHAR(100)',
        'bank_routing_number': 'VARCHAR(100)',
        'khqr_code': 'TEXT',
        'cash_currency': 'VARCHAR(3)',
        'refund_amount': 'DECIMAL(12, 2)',
        'refund_reason': 'TEXT',
        'refund_date': 'DATETIME'
    }
    
    missing_columns = {col: dtype for col, dtype in columns_to_add.items() if col not in existing_columns}
    
    if not missing_columns:
        print("✓ All columns already exist in payments table!")
    else:
        print(f"\n⚠️  Missing columns found: {list(missing_columns.keys())}")
        
        for column_name, column_type in missing_columns.items():
            try:
                alter_sql = f"ALTER TABLE payments ADD COLUMN {column_name} {column_type}"
                cursor.execute(alter_sql)
                print(f"✓ Added {column_name}")
            except sqlite3.OperationalError as e:
                print(f"✗ Error adding {column_name}: {e}")
        
        conn.commit()
        print("✓ All missing columns added successfully!")
    
    conn.close()
    print("\n✓ Database fix complete!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    exit(1)
