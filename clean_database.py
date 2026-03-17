#!/usr/bin/env python
"""Clean all data from the database"""

import sqlite3

db_path = 'backend/instance/warranty_product.db'

try:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Get all tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cur.fetchall()]
    
    print('Tables found:', tables)
    print()
    
    # Delete all data from all tables
    for table in tables:
        try:
            cur.execute(f'DELETE FROM {table}')
            print(f'✓ Cleared: {table}')
        except Exception as e:
            print(f'⚠ Error clearing {table}: {e}')
    
    conn.commit()
    print()
    print('═════════════════════════════════')
    print('✓ DATABASE SUCCESSFULLY CLEANED')
    print('═════════════════════════════════')
    
    # Verify all tables are empty
    print()
    for table in tables:
        cur.execute(f'SELECT COUNT(*) FROM {table}')
        count = cur.fetchone()[0]
        print(f'{table}: {count} records')
    
    conn.close()
except Exception as e:
    print(f'Error: {e}')
