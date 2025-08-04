# 🏪 نظام نقطة البيع المتكامل | Integrated POS System

![POS System](https://img.shields.io/badge/POS-System-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

نظام نقطة بيع متكامل ومتطور مبني بتقنيات حديثة، يوفر إدارة شاملة للمبيعات والمخزون والعملاء والموردين مع ميزات الذكاء الاصطناعي والتحليلات المتقدمة.

**A comprehensive and advanced Point of Sale system built with modern technologies, providing complete management for sales, inventory, customers, and suppliers with AI features and advanced analytics.**

## 📋 جدول المحتويات | Table of Contents

- [الميزات الرئيسية](#الميزات-الرئيسية)
- [التقنيات المستخدمة](#التقنيات-المستخدمة)
- [متطلبات النظام](#متطلبات-النظام)
- [التثبيت والتشغيل](#التثبيت-والتشغيل)
- [النشر على الخادم](#النشر-على-الخادم)
- [دليل الاستخدام](#دليل-الاستخدام)
- [هيكل المشروع](#هيكل-المشروع)
- [API Documentation](#api-documentation)
- [الأمان](#الأمان)
- [المساهمة](#المساهمة)
- [الترخيص](#الترخيص)

## 🌟 الميزات الرئيسية | Key Features

### 🛒 نقطة البيع (POS) المتقدمة
- **واجهة سهلة الاستخدام** لإنشاء الفواتير بسرعة
- **بحث ذكي مع اقتراحات** للمنتجات بالاسم أو الباركود
- **فلاتر سريعة** (متوفر، مخزون منخفض، الأكثر مبيعاً، حديث)
- **دعم الباركود** مع ماسح ضوئي مدمج
- **طرق دفع متعددة:**
  - نقدي تقليدي
  - فودافون كاش
  - البريد المصري
  - انستاباي (البنوك المصرية)
  - بطاقة ائتمان
  - دفع مختلط
- **نظام خصومات متقدم:**
  - خصومات سريعة (5%, 10%, 15%, 20%)
  - خصم على مستوى المنتج أو الفاتورة
  - خصم بالمبلغ أو النسبة المئوية
- **إدارة سلة المشتريات:**
  - إضافة/حذف/تعديل المنتجات بسهولة
  - تعديل الكميات في أي وقت
  - عرض فوري للمجاميع والخصومات
- **تنبيهات ذكية:**
  - تنبيه عند نفاد المخزون
  - تحذير عند المخزون المنخفض
  - عرض حالة المنتج بصرياً

### 📦 إدارة المخزون
- **تتبع المخزون** في الوقت الفعلي
- **تنبيهات المخزون المنخفض**
- **إدارة المنتجات** الشاملة
- **تقارير المخزون** التفصيلية
- **تحليل حركة المنتجات**

### 👥 إدارة العملاء والموردين المتقدمة
- **قاعدة بيانات العملاء** الشاملة
- **برامج الولاء للعملاء:**
  - نقاط المكافآت
  - خصومات العضوية
  - عروض خاصة للعملاء المميزين
  - تتبع تاريخ الشراء
- **تحليل العملاء المتقدم:**
  - العملاء الأكثر ربحية
  - العملاء غير النشطين (لم يشتروا من فترة)
  - تحليل أنماط الشراء
  - توقعات سلوك العملاء
- **إدارة الموردين** والمشتريات
- **تتبع الحسابات الآجلة**
- **سجل المعاملات** التفصيلي مع التواريخ

### 💰 إدارة المدفوعات
- **تحصيل من العملاء** المدينين
- **دفع للموردين** الدائنين
- **سجل المدفوعات** الشامل
- **إحصائيات المدفوعات** الفورية
- **تتبع التدفق النقدي**

### 📊 التقارير والتحليلات المتقدمة
- **تقارير المبيعات المفصلة:**
  - مبيعات يومية/شهرية/سنوية
  - تحليل الأوقات والأيام
  - أفضل المنتجات مبيعاً وربحية
  - تقارير العملاء والموردين
- **التحليل المالي الشامل:**
  - إجمالي الربح وصافي الربح
  - الربح بعد خصم جميع المصروفات
  - تحليل التدفق النقدي
  - معدلات الربحية
- **تقارير المخزون الذكية:**
  - المنتجات الأقل مبيعاً
  - المنتجات الراكدة (لم تُباع لفترة)
  - توقعات إعادة التموين
  - تحليل دوران المخزون
- **رؤى الأداء التجاري:**
  - مؤشرات الأداء الرئيسية (KPIs)
  - اتجاهات المبيعات
  - تحليل الموسمية
  - توقعات النمو

### 🔄 المرتجعات والاستبدال
- **أنواع المرتجعات المتعددة:**
  - إرجاع كامل
  - إرجاع جزئي
  - استبدال منتج
  - استرداد نقدي
- **إدارة شاملة للمرتجعات:**
  - تسجيل عمليات الإرجاع والاستبدال
  - تحديث المخزون تلقائياً
  - تتبع أسباب الإرجاع
  - إصدار إيصالات استرداد
- **إحصائيات المرتجعات:**
  - معدل الإرجاع الشهري
  - أسباب الإرجاع الأكثر شيوعاً
  - تحليل المنتجات المرتجعة

### 🖨️ الطباعة والإيصالات
- **طباعة اختيارية** للفواتير
- **إيصالات مفصلة** مع معلومات الشركة
- **تخصيص تصميم الفاتورة**
- **معلومات الشركة** في كل فاتورة
- **إيصالات الاسترداد** للمرتجعات

### 🤖 الذكاء الاصطناعي والتحليلات
- **توقعات المبيعات** الذكية
- **تحليل الأنماط** والاتجاهات
- **توصيات المنتجات**
- **تحسين المخزون** التلقائي
- **تحليل سلوك العملاء**
- **تحديد المنتجات الراكدة**
- **العملاء غير النشطين**
- **تحليل الربحية المتقدم**

## 🛠️ التقنيات المستخدمة | Technologies Used

### Backend Technologies
- **Python 3.8+** - لغة البرمجة الأساسية
- **Flask 3.0.0** - إطار عمل الويب
- **Flask-SocketIO 5.3.6** - للاتصال في الوقت الفعلي
- **SQLite** - قاعدة البيانات المحلية
- **Gunicorn 21.2.0** - خادم WSGI للإنتاج

### Frontend Technologies
- **HTML5** - هيكل الصفحات
- **CSS3** - التصميم والتنسيق
- **JavaScript (ES6+)** - التفاعل والديناميكية
- **Bootstrap 5.3** - إطار عمل CSS
- **Font Awesome** - الأيقونات
- **Chart.js** - الرسوم البيانية

### Data Analysis & AI Libraries
- **NumPy** - العمليات الرياضية والمصفوفات
- **Pandas** - تحليل البيانات ومعالجتها
- **Matplotlib** - الرسوم البيانية الأساسية
- **Seaborn** - الرسوم البيانية المتقدمة
- **Scikit-learn** - خوارزميات التعلم الآلي
- **Plotly** - الرسوم التفاعلية
- **SciPy** - العمليات العلمية المتقدمة

### Development Tools
- **Git** - نظام إدارة الإصدارات
- **Docker** - الحاويات والنشر
- **Nginx** - خادم الويب (للإنتاج)
- **systemd** - إدارة الخدمات
- **SQLite** - قاعدة بيانات محلية سريعة

### Libraries & Dependencies
```
Flask==3.0.0
Flask-SocketIO==5.3.6
python-socketio==5.10.0
python-engineio==4.7.1
Werkzeug==3.0.1
Jinja2==3.1.2
gunicorn==21.2.0
eventlet==0.33.3
```

## 💻 متطلبات النظام | System Requirements

### الحد الأدنى | Minimum Requirements
- **نظام التشغيل:** Windows 10, Ubuntu 18.04+, macOS 10.14+
- **Python:** 3.8 أو أحدث
- **الذاكرة:** 512 MB RAM
- **التخزين:** 100 MB مساحة فارغة
- **الشبكة:** اتصال إنترنت (للتحديثات)

### المستحسن | Recommended
- **نظام التشغيل:** Ubuntu 20.04+ LTS
- **Python:** 3.11+
- **الذاكرة:** 2 GB RAM
- **التخزين:** 1 GB مساحة فارغة
- **المعالج:** 2 cores CPU

## 🚀 التثبيت والتشغيل | Installation & Setup

### التشغيل السريع | Quick Start

```bash
# 1. تحميل المشروع
git clone https://github.com/your-username/pos-system.git
cd pos-system

# 2. تشغيل السكريبت التلقائي
chmod +x deploy.sh
./deploy.sh

# 3. تشغيل النظام
python simple_pos.py
```

### التثبيت اليدوي | Manual Installation

```bash
# 1. إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# أو
venv\Scripts\activate     # Windows

# 2. تثبيت المتطلبات
pip install -r requirements_server.txt

# 3. تشغيل النظام
python simple_pos.py
```

### التشغيل بـ Docker | Docker Deployment

```bash
# بناء وتشغيل الحاوية
docker-compose up -d

# مراقبة السجلات
docker-compose logs -f
```

## 🌐 النشر على الخادم | Server Deployment

### 1. النشر على Ubuntu Server

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت Python و pip
sudo apt install python3 python3-pip python3-venv -y

# تحميل المشروع
git clone https://github.com/your-username/pos-system.git
cd pos-system

# تشغيل سكريبت النشر
chmod +x deploy.sh
./deploy.sh

# تثبيت كخدمة نظام
sudo cp pos-system.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pos-system
sudo systemctl start pos-system
```

### 2. إعداد Nginx (اختياري)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /socket.io/ {
        proxy_pass http://127.0.0.1:5001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 3. إعداد SSL مع Let's Encrypt

```bash
# تثبيت Certbot
sudo apt install certbot python3-certbot-nginx -y

# الحصول على شهادة SSL
sudo certbot --nginx -d your-domain.com

# تجديد تلقائي
sudo crontab -e
# إضافة السطر التالي:
0 12 * * * /usr/bin/certbot renew --quiet
```

## 📖 دليل الاستخدام | User Guide

### بيانات الدخول الافتراضية | Default Login
- **اسم المستخدم:** admin
- **كلمة المرور:** 3110

### الوصول للنظام | System Access
- **الرابط المحلي:** http://localhost:5001
- **الرابط على الشبكة:** http://your-server-ip:5001

### الصفحات الرئيسية | Main Pages

#### 🏠 الصفحة الرئيسية | Dashboard
- عرض الإحصائيات العامة
- مبيعات اليوم والشهر
- المنتجات المطلوبة
- أحدث المعاملات

#### 🛒 نقطة البيع | POS
- إنشاء فواتير جديدة
- إضافة المنتجات للفاتورة
- اختيار العميل وطريقة الدفع
- طباعة الفاتورة

#### 📦 إدارة المنتجات | Products Management
- إضافة منتجات جديدة
- تعديل بيانات المنتجات
- حذف المنتجات
- تتبع المخزون

#### 👥 إدارة العملاء | Customers Management
- إضافة عملاء جدد
- تعديل بيانات العملاء
- عرض سجل المعاملات
- إدارة الحسابات الآجلة

#### 🚚 إدارة الموردين | Suppliers Management
- إضافة موردين جدد
- تعديل بيانات الموردين
- إدارة المشتريات
- تتبع المستحقات

#### 💰 إدارة المدفوعات | Payments Management
- تحصيل من العملاء
- دفع للموردين
- سجل المدفوعات
- إحصائيات التدفق النقدي

#### 📊 التقارير | Reports
- تقارير المبيعات
- تقارير المخزون
- تقارير العملاء والموردين
- تحليلات الأرباح

## 📁 هيكل المشروع | Project Structure

```
pos-system/
├── 📄 simple_pos.py              # الملف الرئيسي للتطبيق
├── 📄 wsgi.py                    # نقطة دخول WSGI
├── 📄 gunicorn_config.py         # إعدادات Gunicorn
├── 📄 requirements_server.txt    # متطلبات الخادم
├── 📄 Dockerfile                # ملف Docker
├── 📄 docker-compose.yml        # إعداد Docker Compose
├── 📄 deploy.sh                 # سكريبت النشر
├── 📄 README_COMPLETE.md        # هذا الملف
├── 📁 templates/                # قوالب HTML
│   ├── 📄 base.html             # القالب الأساسي
│   ├── 📄 login.html            # صفحة تسجيل الدخول
│   ├── 📄 dashboard.html        # الصفحة الرئيسية
│   ├── 📄 pos.html              # نقطة البيع
│   ├── 📄 products.html         # إدارة المنتجات
│   ├── 📄 customers.html        # إدارة العملاء
│   ├── 📄 suppliers.html        # إدارة الموردين
│   ├── 📄 payments.html         # إدارة المدفوعات
│   ├── 📄 sales.html            # إدارة المبيعات
│   ├── 📄 purchases.html        # إدارة المشتريات
│   ├── 📄 reports.html          # التقارير
│   └── 📄 returns.html          # المرتجعات
├── 📁 static/                   # الملفات الثابتة
│   ├── 📁 css/                  # ملفات CSS
│   ├── 📁 js/                   # ملفات JavaScript
│   ├── 📁 images/               # الصور والأيقونات
│   └── 📄 manifest.json         # ملف PWA
├── 📁 data/                     # قاعدة البيانات
│   └── 📄 simple_pos.db         # ملف SQLite
└── 📁 logs/                     # ملفات السجلات
    ├── 📄 access.log            # سجل الوصول
    └── 📄 error.log             # سجل الأخطاء
```

## 🔌 API Documentation

### Authentication APIs
```
POST /login                      # تسجيل الدخول
GET  /logout                     # تسجيل الخروج
```

### Products APIs
```
GET    /api/products             # جلب جميع المنتجات
POST   /api/products/add         # إضافة منتج جديد
PUT    /api/products/edit/{id}   # تعديل منتج
DELETE /api/products/delete/{id} # حذف منتج
```

### Customers APIs
```
GET    /api/customers            # جلب جميع العملاء
POST   /api/customers/add        # إضافة عميل جديد
PUT    /api/customers/edit/{id}  # تعديل عميل
DELETE /api/customers/delete/{id}# حذف عميل
GET    /api/customers/stats      # إحصائيات العملاء
```

### Suppliers APIs
```
GET    /api/suppliers            # جلب جميع الموردين
POST   /api/suppliers/add        # إضافة مورد جديد
PUT    /api/suppliers/edit/{id}  # تعديل مورد
DELETE /api/suppliers/delete/{id}# حذف مورد
GET    /api/suppliers/stats      # إحصائيات الموردين
```

### Sales APIs
```
GET  /api/sales                  # جلب جميع المبيعات
POST /api/sales/add              # إضافة مبيعة جديدة
GET  /api/sales/stats            # إحصائيات المبيعات
```

### Payments APIs
```
POST /api/payments/add           # إضافة مدفوعة جديدة
GET  /api/payments/history       # سجل المدفوعات
```

### Dashboard APIs
```
GET /api/dashboard/stats         # إحصائيات الصفحة الرئيسية
```

## 🔒 الأمان | Security

### ميزات الأمان المدمجة | Built-in Security Features
- **تشفير الجلسات** باستخدام Flask sessions
- **حماية CSRF** للنماذج
- **تنظيف المدخلات** لمنع SQL injection
- **تحديد الصلاحيات** للوصول للصفحات
- **تسجيل العمليات** لمراقبة النشاط

### توصيات الأمان | Security Recommendations
- تغيير كلمة المرور الافتراضية
- استخدام HTTPS في الإنتاج
- تحديث النظام بانتظام
- عمل نسخ احتياطية دورية
- مراقبة ملفات السجلات

## 🤝 المساهمة | Contributing

نرحب بمساهماتكم في تطوير النظام! يرجى اتباع الخطوات التالية:

1. **Fork** المشروع
2. إنشاء **branch** جديد للميزة
3. **Commit** التغييرات
4. **Push** للـ branch
5. إنشاء **Pull Request**

### إرشادات المساهمة | Contribution Guidelines
- اتبع معايير Python PEP 8
- أضف تعليقات واضحة للكود
- اختبر التغييرات قبل الإرسال
- حدث الوثائق عند الحاجة

## 📄 الترخيص | License

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 📞 الدعم والتواصل | Support & Contact

- **البريد الإلكتروني:** support@pos-system.com
- **الموقع:** https://pos-system.com
- **التوثيق:** https://docs.pos-system.com
- **المجتمع:** https://community.pos-system.com

## 🙏 شكر وتقدير | Acknowledgments

- شكر خاص لمجتمع Python و Flask
- شكر لجميع المساهمين في المشروع
- شكر لمستخدمي النظام وملاحظاتهم القيمة

---

**تم تطوير هذا النظام بـ ❤️ للمجتمع العربي**

**Developed with ❤️ for the Arabic community**
