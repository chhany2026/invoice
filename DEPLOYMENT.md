# Deployment Guide

## Local Development Deployment

### Using SQLite (Recommended for Development)

1. **Set environment to development:**
```bash
set FLASK_ENV=development
```

2. **Create .env file in backend:**
```env
FLASK_ENV=development
DEBUG=True
DATABASE_URL=sqlite:///warranty_product.db
JWT_SECRET_KEY=dev-secret-key
```

3. **Run backend:**
```bash
cd backend
python run.py
```

4. **Run frontend:**
```bash
cd frontend
python main.py
```

The application runs on `http://localhost:5000` (API) and desktop app launches independently.

---

## Cloud Deployment (Production)

### Option 1: Docker Deployment

#### Create Docker Compose Setup

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: warranty_user
      POSTGRES_PASSWORD: your_secure_password
      POSTGRES_DB: warranty_product
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    environment:
      DATABASE_URL: postgresql://warranty_user:your_secure_password@postgres:5432/warranty_product
      FLASK_ENV: production
      JWT_SECRET_KEY: your_production_secret_key
    ports:
      - "5000:5000"
    depends_on:
      - postgres

volumes:
  postgres_data:
```

**backend/Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV FLASK_ENV=production
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "run:app"]
```

#### Deploy with Docker:
```bash
docker-compose up -d
```

---

### Option 2: Cloud Platform Deployment

#### A. Heroku Deployment

1. **Create Heroku app:**
```bash
heroku create your-warranty-app
```

2. **Add PostgreSQL addon:**
```bash
heroku addons:create heroku-postgresql:standard-0
```

3. **Set environment variables:**
```bash
heroku config:set FLASK_ENV=production
heroku config:set JWT_SECRET_KEY=your_production_key
```

4. **Deploy:**
```bash
git push heroku main
```

#### B. AWS Deployment (Elastic Beanstalk)

1. **Initialize EB CLI:**
```bash
eb init -p python-3.11 warranty-product
```

2. **Create environment:**
```bash
eb create warranty-prod --instance-type t3.small
```

3. **Set environment variables:**
```bash
eb setenv FLASK_ENV=production JWT_SECRET_KEY=your_key DATABASE_URL=aws_rds_url
```

4. **Deploy:**
```bash
eb deploy
```

#### C. Google Cloud Run Deployment

1. **Create Cloud Run service:**
```bash
gcloud run deploy warranty-backend \
  --source . \
  --platform managed \
  --region us-central1 \
  --set-env-vars FLASK_ENV=production
```

---

### Option 3: Traditional Server Deployment (VPS/EC2)

#### 1. Setup Linux Server (Ubuntu 22.04)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3.11 python3.11-venv postgres postgresql-contrib nginx git

# Create app directory
mkdir -p /var/www/warranty-product
cd /var/www/warranty-product

# Clone repository
git clone <your-repo> .
```

#### 2. Setup Python Environment

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

#### 3. Setup PostgreSQL

```bash
sudo -i -u postgres
createdb warranty_product
createuser warranty_user
psql << EOF
ALTER USER warranty_user WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE warranty_product TO warranty_user;
\q
EOF
```

#### 4. Create Systemd Service

**File: /etc/systemd/system/warranty-backend.service**
```ini
[Unit]
Description=Warranty Product Backend
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/var/www/warranty-product
Environment="PATH=/var/www/warranty-product/venv/bin"
Environment="DATABASE_URL=postgresql://warranty_user:password@localhost/warranty_product"
ExecStart=/var/www/warranty-product/venv/bin/gunicorn --bind 0.0.0.0:5000 run:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start service:
```bash
sudo systemctl enable warranty-backend
sudo systemctl start warranty-backend
sudo systemctl status warranty-backend
```

#### 5. Setup Nginx Reverse Proxy

**File: /etc/nginx/sites-available/warranty**
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/warranty /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 6. Setup SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

## Frontend Deployment Options

### Option 1: Standalone Desktop Executable

Use PyInstaller to create executable:

```bash
pip install pyinstaller
cd frontend
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

Distribute `dist/main.exe` to users.

### Option 2: Web-Based Frontend (Optional)

Convert PyQt6 UI to web interface with Flask + React:
- Requires rewriting frontend
- Better for multiple users
- Can be hosted on same server

---

## Database Backups

### PostgreSQL Backup Script

**backup.sh:**
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/warranty"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
DB_NAME="warranty_product"

mkdir -p $BACKUP_DIR
pg_dump $DB_NAME | gzip > $BACKUP_DIR/warranty_$TIMESTAMP.sql.gz

# Keep only last 30 days
find $BACKUP_DIR -mtime +30 -delete
```

Run daily with cron:
```bash
0 2 * * * /path/to/backup.sh
```

---

## Monitoring & Logging

### Application Logging

Add to backend config:
```python
import logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
```

### Server Monitoring

- **CPU/Memory**: Use `top`, `htop`, or cloud provider dashboard
- **Disk Space**: Monitor with `df`
- **Application Status**: Use `systemctl status warranty-backend`
- **Port Open**: `netstat -tlnp | grep 5000`

---

## Performance Optimization

### 1. Database Optimization
```sql
-- Create indexes
CREATE INDEX idx_warranty_serial ON warranties(serial_number);
CREATE INDEX idx_warranty_customer ON warranties(customer_id);
CREATE INDEX idx_warranty_status ON warranties(status);
```

### 2. Caching
Add Redis for session caching:
```python
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'redis'})
```

### 3. Load Balancing
Deploy multiple instances behind Nginx:
```nginx
upstream warranty_backend {
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
    server 127.0.0.1:5003;
}
```

---

## Security Checklist

- [ ] Change JWT_SECRET_KEY to a strong random value
- [ ] Use HTTPS (SSL/TLS) in production
- [ ] Set DEBUG=False in production
- [ ] Enable CORS only for trusted domains
- [ ] Use strong database passwords
- [ ] Implement rate limiting
- [ ] Regular security updates
- [ ] Database backup strategy in place
- [ ] Monitor logs for suspicious activity
- [ ] Use environment variables for secrets

---

## Troubleshooting Deployment

**Issue: Connection refused**
- Check if backend is running: `systemctl status warranty-backend`
- Check port: `netstat -tlnp | grep 5000`
- Check firewall: `sudo ufw allow 5000`

**Issue: Database connection failed**
- Verify PostgreSQL is running: `sudo systemctl status postgresql`
- Check connection string in .env
- Verify database and user exist

**Issue: Nginx 502 Bad Gateway**
- Ensure backend is responding: `curl http://127.0.0.1:5000`
- Check Nginx logs: `tail -f /var/log/nginx/error.log`
- Verify Nginx config: `sudo nginx -t`

---

## Support

For deployment issues, check logs:
```bash
# Backend logs
tail -f /var/log/syslog | grep warranty

# Nginx logs
tail -f /var/log/nginx/error.log

# Application logs
tail -f app.log
```
