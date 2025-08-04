# 🏪 نظام نقطة البيع المتكامل | Integrated POS System

![POS System](https://img.shields.io/badge/POS-System-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

نظام نقطة بيع متكامل ومتطور مبني بـ Python و Flask، يوفر إدارة شاملة للمبيعات والمخزون والعملاء والموردين مع ميزات الذكاء الاصطناعي والتحليلات المتقدمة.

**A comprehensive Point of Sale system built with Python & Flask, providing complete management for sales, inventory, customers, and suppliers with AI features and advanced analytics.**

## 🌟 الميزات الرئيسية | Key Features

### 🛒 نقطة البيع المتقدمة
- **بحث ذكي** مع اقتراحات للمنتجات
- **دعم الباركود** وماسح ضوئي
- **طرق دفع متعددة** (نقدي، فودافون كاش، البريد المصري، انستاباي)
- **نظام خصومات متقدم** (سريع ومخصص)
- **تنبيهات المخزون** الذكية

### 📦 إدارة المخزون
- **تتبع المخزون** في الوقت الفعلي
- **تنبيهات المخزون المنخفض**
- **تحليل المنتجات الراكدة**
- **توقعات إعادة التموين**

### 👥 إدارة العملاء والموردين
- **قاعدة بيانات شاملة**
- **برامج الولاء** والمكافآت
- **تحليل العملاء غير النشطين**
- **إدارة الحسابات الآجلة**

### 🔄 المرتجعات والاستبدال
- **أنواع متعددة** من المرتجعات
- **تحديث المخزون تلقائياً**
- **إيصالات استرداد**

### 📊 التقارير والتحليلات
- **تقارير مالية شاملة**
- **الميزانية العمومية المحسنة**
- **تحليل الأرباح المتقدم**
- **رؤى الأداء التجاري**

### 🤖 الذكاء الاصطناعي
- **توقعات المبيعات**
- **تحليل الأنماط**
- **توصيات المنتجات**
- **تحسين المخزون**

## 🛠️ التقنيات المستخدمة | Technologies

- **Backend:** Python 3.8+, Flask 3.0.0, SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Real-time:** Flask-SocketIO
- **Analytics:** NumPy, Pandas, Matplotlib, Scikit-learn
- **Deployment:** Docker, Nginx, Gunicorn

## 🚀 التثبيت والتشغيل | Installation & Setup

### التشغيل السريع | Quick Start

```bash
# 1. استنساخ المشروع
git clone https://github.com/your-username/pos-system.git
cd pos-system

# 2. تثبيت المتطلبات
pip install -r requirements_server.txt

# 3. تشغيل النظام
python simple_pos.py
```

### التشغيل بـ Docker | Docker

```bash
# بناء وتشغيل
docker-compose up -d

# مراقبة السجلات
docker-compose logs -f
```

### النشر على الخادم | Server Deployment

```bash
# تشغيل سكريپت النشر التلقائي
chmod +x deploy.sh
./deploy.sh
```

## 🌐 الوصول للنظام | System Access

- **الرابط المحلي:** http://localhost:5001
- **اسم المستخدم:** admin
- **كلمة المرور:** 3110

## 📁 هيكل المشروع | Project Structure

```
pos-system/
├── 📄 simple_pos.py              # الملف الرئيسي
├── 📄 wsgi.py                    # نقطة دخول WSGI
├── 📄 requirements_server.txt    # متطلبات الخادم
├── 📄 deploy.sh                 # سكريپت النشر
├── 📄 docker-compose.yml        # إعداد Docker
├── 📁 templates/                # قوالب HTML
├── 📁 static/                   # الملفات الثابتة
└── 📄 README.md                 # هذا الملف
```

## 🔧 الميزات المتقدمة | Advanced Features

### طرق الدفع | Payment Methods
- نقدي تقليدي
- فودافون كاش
- البريد المصري
- انستاباي (البنوك المصرية)
- بطاقة ائتمان
- دفع مختلط

### التقارير المالية | Financial Reports
- قائمة الأرباح والخسائر
- الميزانية العمومية
- قائمة التدفقات النقدية
- قائمة الدخل
- قائمة المركز المالي
- الذمم المدينة والدائنة

### التحليلات | Analytics
- المنتجات الأكثر مبيعاً
- المنتجات الراكدة
- العملاء غير النشطين
- تحليل الربحية
- توقعات المبيعات

## 📊 البيانات التجريبية | Sample Data

النظام يأتي مع بيانات تجريبية جاهزة للاختبار:
- **5 منتجات** مختلفة
- **4 عملاء** مع أرصدة متنوعة
- **4 موردين** مع مستحقات
- **عمليات بيع** تجريبية

## 🤝 المساهمة | Contributing

نرحب بمساهماتكم! يرجى:
1. Fork المشروع
2. إنشاء branch جديد
3. Commit التغييرات
4. إنشاء Pull Request

## 📄 الترخيص | License

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 📞 الدعم | Support

- **الوثائق الشاملة:** [README_COMPLETE.md](README_COMPLETE.md)
- **دليل النشر:** [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **معلومات التطبيق:** [APP_INFO.md](APP_INFO.md)

---

**تم تطوير هذا النظام بـ ❤️ للمجتمع العربي**

**Developed with ❤️ for the Arabic community**
