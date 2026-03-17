#!/usr/bin/env python
import os

# Set DATABASE_URL explicitly to SQLite for development
os.environ['DATABASE_URL'] = 'sqlite:///warranty_product.db'
os.environ['FLASK_ENV'] = 'development'

from app import create_app

app = create_app('development')
print(f"Using database: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
