# 🚀 دليل النشر السريع | Quick Deployment Guide

## 📋 خطوات النشر على الخادم | Server Deployment Steps

### 1. إعداد الخادم | Server Setup

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت المتطلبات الأساسية
sudo apt install python3 python3-pip python3-venv nginx git curl -y

# إنشاء مستخدم للتطبيق (اختياري)
sudo useradd -m -s /bin/bash posuser
sudo usermod -aG sudo posuser
```

### 2. تحميل المشروع | Download Project

```bash
# الانتقال للمجلد المناسب
cd /opt

# تحميل المشروع
sudo git clone https://github.com/your-username/pos-system.git
sudo chown -R posuser:posuser pos-system
cd pos-system
```

### 3. التثبيت التلقائي | Automatic Installation

```bash
# تشغيل سكريبت النشر
chmod +x deploy.sh
./deploy.sh
```

### 4. إعداد الخدمة | Service Setup

```bash
# نسخ ملف الخدمة
sudo cp pos-system.service /etc/systemd/system/

# تعديل المسارات في ملف الخدمة
sudo nano /etc/systemd/system/pos-system.service

# تفعيل الخدمة
sudo systemctl daemon-reload
sudo systemctl enable pos-system
sudo systemctl start pos-system

# التحقق من الحالة
sudo systemctl status pos-system
```

### 5. إعداد Nginx | Nginx Setup

```bash
# نسخ إعداد Nginx
sudo cp nginx.conf /etc/nginx/sites-available/pos-system

# تفعيل الموقع
sudo ln -s /etc/nginx/sites-available/pos-system /etc/nginx/sites-enabled/

# اختبار الإعداد
sudo nginx -t

# إعادة تشغيل Nginx
sudo systemctl restart nginx
```

### 6. إعداد SSL | SSL Setup

```bash
# تثبيت Certbot
sudo apt install certbot python3-certbot-nginx -y

# الحصول على شهادة SSL
sudo certbot --nginx -d your-domain.com

# تجديد تلقائي
echo "0 12 * * * /usr/bin/certbot renew --quiet" | sudo crontab -
```

## 🐳 النشر باستخدام Docker | Docker Deployment

### 1. تثبيت Docker

```bash
# تثبيت Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# تثبيت Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### 2. تشغيل التطبيق

```bash
# بناء وتشغيل الحاويات
docker-compose up -d

# مراقبة السجلات
docker-compose logs -f

# إيقاف التطبيق
docker-compose down
```

## ⚙️ إعدادات الإنتاج | Production Settings

### متغيرات البيئة | Environment Variables

```bash
# إنشاء ملف البيئة
cat > .env << EOF
FLASK_ENV=production
SECRET_KEY=your-very-secure-secret-key-here
PORT=5001
HOST=127.0.0.1
DATABASE_PATH=/opt/pos-system/data/pos_system.db
EOF
```

### إعدادات الأمان | Security Settings

```bash
# إعداد جدار الحماية
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable

# إعداد fail2ban
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## 📊 المراقبة والصيانة | Monitoring & Maintenance

### مراقبة النظام | System Monitoring

```bash
# مراقبة الخدمة
sudo systemctl status pos-system

# مراقبة السجلات
sudo journalctl -u pos-system -f

# مراقبة استخدام الموارد
htop
```

### النسخ الاحتياطية | Backups

```bash
# تشغيل النسخ الاحتياطي يدوياً
./backup.sh

# جدولة النسخ الاحتياطية
crontab -e
# إضافة السطر التالي للنسخ اليومي في الساعة 2 صباحاً:
0 2 * * * /opt/pos-system/backup.sh
```

### التحديثات | Updates

```bash
# تحديث الكود
cd /opt/pos-system
git pull origin main

# إعادة تشغيل الخدمة
sudo systemctl restart pos-system
```

## 🔧 استكشاف الأخطاء | Troubleshooting

### مشاكل شائعة | Common Issues

#### 1. الخدمة لا تعمل
```bash
# فحص السجلات
sudo journalctl -u pos-system --no-pager

# فحص المنفذ
sudo netstat -tlnp | grep :5001

# إعادة تشغيل الخدمة
sudo systemctl restart pos-system
```

#### 2. مشاكل قاعدة البيانات
```bash
# فحص ملف قاعدة البيانات
ls -la /opt/pos-system/data/

# فحص الصلاحيات
sudo chown -R posuser:posuser /opt/pos-system/data/
```

#### 3. مشاكل Nginx
```bash
# فحص إعداد Nginx
sudo nginx -t

# فحص السجلات
sudo tail -f /var/log/nginx/error.log
```

## 📱 الوصول للنظام | System Access

### الروابط | URLs
- **HTTP:** http://your-domain.com
- **HTTPS:** https://your-domain.com
- **IP مباشر:** http://your-server-ip:5001

### بيانات الدخول | Login Credentials
- **اسم المستخدم:** admin
- **كلمة المرور:** 3110

⚠️ **مهم:** تأكد من تغيير كلمة المرور الافتراضية بعد التثبيت!

## 📞 الدعم | Support

إذا واجهت أي مشاكل:

1. راجع ملف `TROUBLESHOOTING.md`
2. تحقق من السجلات في مجلد `logs/`
3. تأكد من تشغيل جميع الخدمات
4. راجع الوثائق في `README_COMPLETE.md`

---

**تم إعداد هذا الدليل لضمان نشر سهل وآمن للنظام** 🚀
