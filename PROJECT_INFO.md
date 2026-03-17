# Warranty Product Application

## Development

### Architecture Overview

```
┌─────────────────────────────────────────────────────┐
│              Desktop Application (PyQt6)             │
│  ┌─────────────────────────────────────────────────┐ │
│  │  QR Code Scanner | Warranty Management | Reports │ │
│  └─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
                      ↓ HTTP/REST API
┌─────────────────────────────────────────────────────┐
│           Flask Backend (Python)                    │
│  ┌─────────────────────────────────────────────────┐ │
│  │  /api/warranty  /api/product  /api/customer     │ │
│  │             /api/qr                             │ │
│  └─────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────┘
                      ↓ SQL
┌─────────────────────────────────────────────────────┐
│  PostgreSQL Database (Production)                   │
│  SQLite Database (Development)                      │
└─────────────────────────────────────────────────────┘
```

### Technology Stack

**Backend:**
- Flask (Web framework)
- SQLAlchemy (ORM)
- PostgreSQL/SQLite (Database)
- Python-QRCode (QR generation)

**Frontend:**
- PyQt6 (Desktop GUI)
- OpenCV (Camera/QR scanning)
- pyzbar (QR decoding)
- Requests (API client)

### Development Workflow

1. Create feature branch
2. Implement changes
3. Test thoroughly
4. Create pull request
5. Code review
6. Merge to main

## Features

### Current (v1.0)
- ✅ Warranty registration via serial number/QR code
- ✅ Product catalog management
- ✅ Customer information management
- ✅ Real-time QR scanning with camera
- ✅ RESTful API
- ✅ Local/Cloud deployment options

### Planned (v1.1+)
- Warranty claim management
- Warranty transfer functionality
- Email notifications
- Bulk import/export (CSV)
- Advanced reporting
- Multi-language support
- Mobile app
- 2FA authentication

## Project Statistics

- **Total Files**: 15+
- **Total Lines of Code**: ~3000+
- **API Endpoints**: 12+
- **Database Size**: Scalable (SQLite for dev, PostgreSQL for prod)

## Team & Contribution

### Code Style
- PEP 8 for Python
- Type hints for functions
- Docstrings for classes and functions
- Comments for complex logic

### Testing
Run tests with:
```bash
# Backend tests (coming soon)
cd backend
pytest

# Frontend tests (coming soon)
cd frontend
pytest
```

### Documentation
- Inline code comments
- README.md for overview
- DEPLOYMENT.md for setup
- API_DOCUMENTATION.md for endpoints

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-01-15 | Initial release - Warranty registration and QR scanning |
| 0.1 | 2024-01-01 | Project setup and architecture design |

## Legal & License

© 2026 Warranty Product Management System

All rights reserved. This software is provided as-is for managing warranty products globally through QR codes and serial numbers.
