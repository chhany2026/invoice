@echo off
REM Quick Setup Script for Warranty Product Management System (Windows)

echo ================================
echo Warranty Product Setup Script
echo ================================
echo.

REM Check Python version
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+
    exit /b 1
)
python --version
echo ✅ Python found
echo.

REM Setup Backend
echo [2/5] Setting up backend environment...
cd backend
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
echo ✅ Backend environment ready
echo.

REM Setup Frontend
echo [3/5] Setting up frontend environment...
cd ..\frontend
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
echo ✅ Frontend environment ready
cd ..
echo.

REM Create database structure
echo [4/5] Initializing database...
cd backend
call venv\Scripts\activate.bat
python -c "from app import create_app; app = create_app('development'); ctx = app.app_context(); ctx.push(); from app import db; db.create_all(); print('✅ Database tables created')"
cd ..
echo.

REM Display instructions
echo [5/5] Setup Complete!
echo.
echo ================================
echo 📋 Next Steps
echo ================================
echo.
echo To start the application:
echo.
echo Terminal 1 (Backend):
echo   cd backend
echo   venv\Scripts\activate.bat
echo   python run.py
echo.
echo Terminal 2 (Frontend):
echo   cd frontend
echo   venv\Scripts\activate.bat
echo   python main.py
echo.
echo API will be available at: http://localhost:5000
echo.
echo Documentation:
echo   - README.md - Project overview
echo   - DEPLOYMENT.md - Deployment guide
echo   - API_DOCUMENTATION.md - API reference
echo.
