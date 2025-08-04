#!/bin/bash

# نظام نقطة البيع - سكريبت النشر على الخادم
# POS System - Server Deployment Script

echo "🚀 بدء نشر نظام نقطة البيع على الخادم..."
echo "🚀 Starting POS System server deployment..."

# التحقق من Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 غير مثبت. يرجى تثبيت Python 3.8+ أولاً"
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first"
    exit 1
fi

echo "✅ Python $(python3 --version) موجود"

# إنشاء بيئة افتراضية
echo "📦 إنشاء البيئة الافتراضية..."
python3 -m venv venv

# تفعيل البيئة الافتراضية
echo "🔧 تفعيل البيئة الافتراضية..."
source venv/bin/activate

# تثبيت المتطلبات
echo "📥 تثبيت المتطلبات..."
pip install --upgrade pip
pip install -r requirements_server.txt

# إنشاء المجلدات المطلوبة
echo "📁 إنشاء المجلدات..."
mkdir -p data
mkdir -p logs
mkdir -p static/css
mkdir -p static/js
mkdir -p static/images

# تعيين الصلاحيات
echo "🔐 تعيين الصلاحيات..."
chmod +x deploy.sh
chmod +x wsgi.py

# إنشاء ملف الخدمة (systemd)
echo "⚙️ إنشاء ملف الخدمة..."
cat > pos-system.service << EOF
[Unit]
Description=POS System - نظام نقطة البيع
After=network.target

[Service]
Type=notify
User=$USER
WorkingDirectory=$(pwd)
Environment=PATH=$(pwd)/venv/bin
ExecStart=$(pwd)/venv/bin/gunicorn --config gunicorn_config.py wsgi:app
ExecReload=/bin/kill -s HUP \$MAINPID
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

echo "✅ تم إنشاء ملف الخدمة: pos-system.service"

# تشغيل النظام
echo "🚀 تشغيل النظام..."
echo "يمكنك تشغيل النظام بإحدى الطرق التالية:"
echo ""
echo "1. التشغيل المباشر:"
echo "   source venv/bin/activate"
echo "   python simple_pos.py"
echo ""
echo "2. التشغيل بـ Gunicorn:"
echo "   source venv/bin/activate"
echo "   gunicorn --config gunicorn_config.py wsgi:app"
echo ""
echo "3. التشغيل كخدمة نظام:"
echo "   sudo cp pos-system.service /etc/systemd/system/"
echo "   sudo systemctl daemon-reload"
echo "   sudo systemctl enable pos-system"
echo "   sudo systemctl start pos-system"
echo ""
echo "4. التشغيل بـ Docker:"
echo "   docker-compose up -d"
echo ""
echo "🌐 الرابط: http://your-server-ip:5001"
echo "🔐 بيانات الدخول:"
echo "   اسم المستخدم: admin"
echo "   كلمة المرور: 3110"
echo ""
echo "✅ تم الانتهاء من الإعداد بنجاح!"
