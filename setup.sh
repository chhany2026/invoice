#!/bin/bash
# Quick Setup Script for Warranty Product Management System

set -e

echo "================================"
echo "Warranty Product Setup Script"
echo "================================"
echo ""

# Check Python version
echo "[1/5] Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+"
    exit 1
fi
python3 --version
echo "✅ Python found"
echo ""

# Setup Backend
echo "[2/5] Setting up backend environment..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
echo "✅ Backend environment ready"
echo ""

# Setup Frontend
echo "[3/5] Setting up frontend environment..."
cd ../frontend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
echo "✅ Frontend environment ready"
cd ..
echo ""

# Create database structure
echo "[4/5] Initializing database..."
cd backend
source venv/bin/activate
python3 << 'EOF'
from app import create_app
app = create_app('development')
with app.app_context():
    from app import db
    db.create_all()
    print("✅ Database tables created")
EOF
cd ..
echo ""

# Display instructions
echo "[5/5] Setup Complete!"
echo ""
echo "================================"
echo "📋 Next Steps"
echo "================================"
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python run.py"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd frontend"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "API will be available at: http://localhost:5000"
echo ""
echo "Documentation:"
echo "  - README.md - Project overview"
echo "  - DEPLOYMENT.md - Deployment guide"
echo "  - API_DOCUMENTATION.md - API reference"
echo ""
