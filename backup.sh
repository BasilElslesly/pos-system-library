#!/bin/bash

# سكريبت النسخ الاحتياطي لنظام نقطة البيع
# POS System Backup Script

# إعدادات النسخ الاحتياطي
BACKUP_DIR="/backup/pos-system"
APP_DIR="/path/to/pos-system"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="pos_backup_$DATE"

# إنشاء مجلد النسخ الاحتياطي
mkdir -p "$BACKUP_DIR"

echo "🔄 بدء النسخ الاحتياطي لنظام نقطة البيع..."
echo "📅 التاريخ: $(date)"
echo "📁 المجلد: $BACKUP_DIR/$BACKUP_NAME"

# إنشاء مجلد النسخة الاحتياطية
mkdir -p "$BACKUP_DIR/$BACKUP_NAME"

# نسخ قاعدة البيانات
echo "📊 نسخ قاعدة البيانات..."
if [ -f "$APP_DIR/data/simple_pos.db" ]; then
    cp "$APP_DIR/data/simple_pos.db" "$BACKUP_DIR/$BACKUP_NAME/"
    echo "✅ تم نسخ قاعدة البيانات"
else
    echo "⚠️ لم يتم العثور على قاعدة البيانات"
fi

# نسخ ملفات الإعداد
echo "⚙️ نسخ ملفات الإعداد..."
cp "$APP_DIR/simple_pos.py" "$BACKUP_DIR/$BACKUP_NAME/" 2>/dev/null
cp "$APP_DIR/gunicorn_config.py" "$BACKUP_DIR/$BACKUP_NAME/" 2>/dev/null
cp "$APP_DIR/requirements_server.txt" "$BACKUP_DIR/$BACKUP_NAME/" 2>/dev/null

# نسخ السجلات
echo "📝 نسخ السجلات..."
if [ -d "$APP_DIR/logs" ]; then
    cp -r "$APP_DIR/logs" "$BACKUP_DIR/$BACKUP_NAME/"
    echo "✅ تم نسخ السجلات"
fi

# نسخ الملفات المرفوعة (إن وجدت)
if [ -d "$APP_DIR/uploads" ]; then
    echo "📎 نسخ الملفات المرفوعة..."
    cp -r "$APP_DIR/uploads" "$BACKUP_DIR/$BACKUP_NAME/"
fi

# إنشاء ملف معلومات النسخة الاحتياطية
echo "📋 إنشاء ملف المعلومات..."
cat > "$BACKUP_DIR/$BACKUP_NAME/backup_info.txt" << EOF
نظام نقطة البيع - معلومات النسخة الاحتياطية
POS System - Backup Information

تاريخ النسخ: $(date)
الخادم: $(hostname)
المستخدم: $(whoami)
حجم النسخة: $(du -sh "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)
مسار التطبيق: $APP_DIR

الملفات المنسوخة:
$(ls -la "$BACKUP_DIR/$BACKUP_NAME")
EOF

# ضغط النسخة الاحتياطية
echo "🗜️ ضغط النسخة الاحتياطية..."
cd "$BACKUP_DIR"
tar -czf "$BACKUP_NAME.tar.gz" "$BACKUP_NAME"
rm -rf "$BACKUP_NAME"

# حساب الحجم النهائي
BACKUP_SIZE=$(du -sh "$BACKUP_NAME.tar.gz" | cut -f1)

echo "✅ تم إنشاء النسخة الاحتياطية بنجاح!"
echo "📁 الملف: $BACKUP_DIR/$BACKUP_NAME.tar.gz"
echo "📏 الحجم: $BACKUP_SIZE"

# حذف النسخ القديمة (الاحتفاظ بآخر 7 نسخ)
echo "🧹 تنظيف النسخ القديمة..."
cd "$BACKUP_DIR"
ls -t pos_backup_*.tar.gz | tail -n +8 | xargs -r rm
echo "✅ تم تنظيف النسخ القديمة"

# إرسال تنبيه (اختياري)
# يمكن إضافة إرسال بريد إلكتروني أو إشعار هنا

echo "🎉 انتهت عملية النسخ الاحتياطي بنجاح!"
echo "⏰ الوقت المستغرق: $(($(date +%s) - $(date -d "$(date)" +%s))) ثانية"
