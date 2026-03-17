"""
Settings API Routes
Handles configuration and customization settings
"""
from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

settings_bp = Blueprint('settings', __name__)

# Settings file path
SETTINGS_FILE = os.path.join(os.path.dirname(__file__), 'settings.json')

def load_settings():
    """Load settings from JSON file"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading settings: {e}")
            return get_default_settings()
    return get_default_settings()

def save_settings(settings):
    """Save settings to JSON file"""
    try:
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
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
