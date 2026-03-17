from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Load configuration
    if config_name == 'production':
        from .config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from .config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Initialize extensions
    db.init_app(app)
    CORS(app)
    jwt.init_app(app)
    
    # Import models (required for create_all)
    from .models import Customer, Product, Warranty
    from .models_invoice import Invoice, InvoiceLineItem, Receipt, Payment, CompanySettings
    
    # Register blueprints
    from .routes import warranty_bp, product_bp, customer_bp, qr_bp
    from .routes_invoice import invoice_bp
    from .routes_settings import settings_bp
    
    app.register_blueprint(warranty_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(qr_bp)
    app.register_blueprint(invoice_bp)
    app.register_blueprint(settings_bp)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    # Serve Dashboard
    import os
    @app.route('/')
    @app.route('/dashboard')
    @app.route('/DASHBOARD.html')
    def serve_dashboard():
        from flask import send_file
        dashboard_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'DASHBOARD.html')
        if os.path.exists(dashboard_path):
            return send_file(dashboard_path)
        return '<h1>Invoice & Warranty Management System</h1><p>API is running on /api endpoints</p>'
    
    @app.route('/settings')
    @app.route('/SETTINGS.html')
    def serve_settings():
        from flask import send_file
        settings_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'SETTINGS.html')
        if os.path.exists(settings_path):
            return send_file(settings_path)
        return '<h1>Settings Not Found</h1>'
    
    @app.route('/preview')
    @app.route('/TEMPLATE_PREVIEW.html')
    def serve_preview():
        from flask import send_file
        preview_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'TEMPLATE_PREVIEW.html')
        if os.path.exists(preview_path):
            return send_file(preview_path)
        return '<h1>Preview Not Found</h1>'
    
    return app
