"""
Settings API Routes
Handles configuration and customization settings
"""
from flask import Blueprint, request, jsonify, send_from_directory
import json
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import base64

settings_bp = Blueprint('settings', __name__)

# Upload configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'svg', 'webp'}

def get_upload_folder():
    """Get or create uploads folder"""
    upload_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), UPLOAD_FOLDER)
    os.makedirs(upload_path, exist_ok=True)
    return upload_path

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Settings file path - stored in instance folder for persistence
def get_settings_file():
    instance_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance')
    os.makedirs(instance_path, exist_ok=True)
    return os.path.join(instance_path, 'settings.json')

def load_settings():
    """Load settings from JSON file"""
    settings_file = get_settings_file()
    if os.path.exists(settings_file):
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading settings: {e}")
            return get_default_settings()
    return get_default_settings()

def save_settings(settings):
    """Save settings to JSON file"""
    try:
        settings_file = get_settings_file()
        with open(settings_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving settings: {e}")
        return False

def get_default_settings():
    """Return default settings"""
    return {
        "company": {
            "name": "Your Company Name",
            "email": "info@company.com",
            "phone": "+855-90-000-000",
            "website": "https://www.company.com",
            "street": "123 Business Street",
            "city": "Phnom Penh",
            "state": "Phnom Penh",
            "postal": "00000",
            "country": "Cambodia",
            "taxId": ""
        },
        "branding": {
            "logo": "",
            "primaryColor": "#667eea",
            "secondaryColor": "#764ba2",
            "accentColor": "#4CAF50",
            "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
        },
        "invoice": {
            "prefix": "INV",
            "startNum": "1000",
            "taxRate": "10",
            "paymentTerms": "30",
            "terms": "Thank you for your business! Payment is due within the specified terms.",
            "notes": "",
            "defaultCurrency": "USD",
            "defaultLanguage": "en"
        },
        "payments": {
            "cashKHRDetails": "Direct Cash Payment (KHR)",
            "cashUSDDetails": "Direct Cash Payment (USD)",
            "khqrId": "",
            "abaName": "ABA Bank Account",
            "abaAccount": "Not provided",
            "acledaName": "ACLEDA Bank Account",
            "acledaAccount": "Not provided"
        },
        "currencies": {
            "enabled": ["USD", "KHR"],
            "symbols": {
                "USD": "$",
                "EUR": "€",
                "GBP": "£",
                "JPY": "¥",
                "CAD": "C$",
                "KHR": "៛"
            }
        },
        "advanced": {
            "numberingStyle": "simple",
            "timezone": "Asia/Bangkok",
            "decimalPlaces": "2",
            "dateFormat": "MM/DD/YYYY",
            "enableReminders": "yes",
            "defaultWarranty": "24"
        }
    }

@settings_bp.route('/api/settings', methods=['GET'])
def get_settings():
    """Get all settings"""
    try:
        settings = load_settings()
        return jsonify({
            'success': True,
            'data': settings
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/settings/<section>', methods=['GET'])
def get_settings_section(section):
    """Get specific settings section"""
    try:
        settings = load_settings()
        if section in settings:
            return jsonify({
                'success': True,
                'data': settings[section]
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': f'Section "{section}" not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/settings', methods=['POST'])
def update_settings():
    """Update settings (full or partial)"""
    try:
        data = request.get_json()
        settings = load_settings()
        
        # Update settings with provided data
        for section, values in data.items():
            if section in settings:
                if isinstance(values, dict):
                    settings[section].update(values)
                else:
                    settings[section] = values
        
        if save_settings(settings):
            return jsonify({
                'success': True,
                'message': 'Settings updated successfully',
                'data': settings
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to save settings'
            }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/settings/<section>', methods=['POST'])
def update_settings_section(section):
    """Update specific settings section"""
    try:
        data = request.get_json()
        settings = load_settings()
        
        if section in settings:
            if isinstance(settings[section], dict) and isinstance(data, dict):
                settings[section].update(data)
            else:
                settings[section] = data
            
            if save_settings(settings):
                return jsonify({
                    'success': True,
                    'message': f'Section "{section}" updated successfully',
                    'data': settings[section]
                }), 200
            else:
                return jsonify({
                    'success': False,
                    'error': 'Failed to save settings'
                }), 500
        else:
            return jsonify({
                'success': False,
                'error': f'Section "{section}" not found'
            }), 404
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/settings/reset', methods=['POST'])
def reset_settings():
    """Reset settings to defaults"""
    try:
        default = get_default_settings()
        if save_settings(default):
            return jsonify({
                'success': True,
                'message': 'Settings reset to defaults',
                'data': default
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to reset settings'
            }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/settings/export', methods=['GET'])
def export_settings():
    """Export settings as JSON file"""
    try:
        settings = load_settings()
        return jsonify({
            'success': True,
            'data': settings,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/upload/logo', methods=['POST'])
def upload_logo():
    """Upload company logo file"""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No file part in request'
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'success': False,
                'error': 'No file selected'
            }), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                'success': False,
                'error': 'File type not allowed. Allowed types: PNG, JPG, JPEG, GIF, SVG, WEBP'
            }), 400
        
        # Generate secure filename
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = f'company_logo_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{ext}'
        secure_name = secure_filename(filename)
        
        # Save file
        upload_folder = get_upload_folder()
        filepath = os.path.join(upload_folder, secure_name)
        file.save(filepath)
        
        # Create relative URL path for the logo
        logo_url = f'/api/uploads/logo/{secure_name}'
        
        # Update settings with the logo URL
        settings = load_settings()
        settings['branding']['logo'] = logo_url
        save_settings(settings)
        
        return jsonify({
            'success': True,
            'message': 'Logo uploaded successfully',
            'logo_url': logo_url,
            'filename': secure_name
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@settings_bp.route('/api/uploads/logo/<filename>', methods=['GET'])
def get_logo(filename):
    """Serve uploaded logo file"""
    try:
        upload_folder = get_upload_folder()
        return send_from_directory(upload_folder, secure_filename(filename))
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'Logo not found'
        }), 404
