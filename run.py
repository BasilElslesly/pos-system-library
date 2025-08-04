#!/usr/bin/env python3
"""
نظام نقطة البيع - ملف التشغيل المبسط
POS System - Simple Run Script
"""

import os
import sys

# إضافة المجلد الحالي لمسار Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from simple_pos import app, socketio, init_db
    
    def main():
        """دالة التشغيل الرئيسية"""
        print("🚀 تشغيل نظام نقطة البيع المتكامل...")
        print("=" * 50)
        print("📱 الرابط: http://localhost:5001")
        print("🔐 بيانات الدخول:")
        print("   اسم المستخدم: admin")
        print("   كلمة المرور: 3110")
        print("=" * 50)
        print("💡 للإيقاف: اضغط Ctrl+C")
        print()
        
        # إنشاء قاعدة البيانات
        init_db()
        
        # تشغيل الخادم
        socketio.run(
            app,
            host='0.0.0.0',
            port=5001,
            debug=False,
            use_reloader=False
        )
    
    if __name__ == '__main__':
        main()
        
except ImportError as e:
    print(f"❌ خطأ في الاستيراد: {e}")
    print("💡 تأكد من تثبيت المتطلبات:")
    print("   pip install -r requirements.txt")
    sys.exit(1)
except Exception as e:
    print(f"❌ خطأ في التشغيل: {e}")
    sys.exit(1)
