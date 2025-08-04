#!/usr/bin/env python3
"""
نظام نقطة البيع المبسط
يعمل بدون قاعدة بيانات معقدة
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from flask_socketio import SocketIO
import json
import os
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
socketio = SocketIO(app, cors_allowed_origins="*")

# إعداد قاعدة البيانات البسيطة
DB_FILE = 'simple_pos.db'

def init_db():
    """إنشاء قاعدة البيانات البسيطة"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # جدول المنتجات
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # جدول العملاء
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            balance REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # جدول الموردين
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            balance REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # جدول المبيعات
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            total_amount REAL NOT NULL,
            payment_method TEXT DEFAULT 'نقدي',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # جدول عناصر المبيعات
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sale_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sale_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            price REAL,
            FOREIGN KEY (sale_id) REFERENCES sales (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        )
    ''')

    # جدول المدفوعات
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL, -- 'customer' or 'supplier'
            entity_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # إدراج بيانات تجريبية
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        sample_products = [
            ('لابتوب Dell', 15000, 10),
            ('ماوس لاسلكي', 150, 50),
            ('كيبورد', 300, 30),
            ('شاشة 24 بوصة', 3000, 15),
            ('سماعات', 200, 25)
        ]
        cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", sample_products)

    # إدراج عملاء تجريبيين مع أرصدة آجلة
    cursor.execute("SELECT COUNT(*) FROM customers")
    if cursor.fetchone()[0] == 0:
        sample_customers = [
            ('أحمد محمد علي', '01234567890', -1500.00),  # مدين بـ 1500
            ('فاطمة حسن', '01098765432', -750.00),       # مدينة بـ 750
            ('محمد أحمد', '01122334455', -2200.00),      # مدين بـ 2200
            ('سارة علي', '01555666777', 0.00)            # لا يوجد دين
        ]
        cursor.executemany("INSERT INTO customers (name, phone, balance) VALUES (?, ?, ?)", sample_customers)

    # إدراج موردين تجريبيين مع أرصدة آجلة
    cursor.execute("SELECT COUNT(*) FROM suppliers")
    if cursor.fetchone()[0] == 0:
        sample_suppliers = [
            ('شركة النور للتجارة', '01234567890', 5000.00),    # مستحق له 5000
            ('مؤسسة الأمل التجارية', '01098765432', 3200.00), # مستحق له 3200
            ('شركة المستقبل', '01333444555', 1800.00),       # مستحق له 1800
            ('مؤسسة التقدم', '01666777888', 0.00)            # لا يوجد مستحقات
        ]
        cursor.executemany("INSERT INTO suppliers (name, phone, balance) VALUES (?, ?, ?)", sample_suppliers)
    
    conn.commit()
    conn.close()

# بيانات المستخدم الافتراضي
DEFAULT_USER = {'username': 'admin', 'password': '3110'}

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """تسجيل الدخول"""
    if request.method == 'POST':
        # التحقق من نوع البيانات المرسلة
        if request.is_json:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        else:
            username = request.form.get('username')
            password = request.form.get('password')

        if username == DEFAULT_USER['username'] and password == DEFAULT_USER['password']:
            session['user_id'] = 1
            session['username'] = username

            if request.is_json:
                return jsonify({'success': True, 'message': 'تم تسجيل الدخول بنجاح', 'redirect': url_for('index')})
            else:
                flash('تم تسجيل الدخول بنجاح', 'success')
                return redirect(url_for('index'))
        else:
            if request.is_json:
                return jsonify({'success': False, 'message': 'اسم المستخدم أو كلمة المرور غير صحيحة'})
            else:
                flash('اسم المستخدم أو كلمة المرور غير صحيحة', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    """تسجيل الخروج"""
    session.clear()
    flash('تم تسجيل الخروج بنجاح', 'success')
    return redirect(url_for('login'))

@app.route('/pos')
def pos():
    """نقطة البيع"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('pos.html')

@app.route('/products')
def products():
    """إدارة المنتجات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('products.html')

@app.route('/customers')
def customers():
    """إدارة العملاء"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('customers.html')

@app.route('/suppliers')
def suppliers():
    """إدارة الموردين"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('suppliers.html')

@app.route('/sales')
def sales():
    """إدارة المبيعات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('sales.html')

@app.route('/purchases')
def purchases():
    """إدارة المشتريات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('purchases.html')

@app.route('/reports')
def reports():
    """التقارير والتحليلات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('reports.html')

@app.route('/returns')
def returns():
    """إدارة المرتجعات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('returns.html')

@app.route('/out-of-stock')
def out_of_stock():
    """المنتجات غير المتوفرة"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('out_of_stock.html')

@app.route('/historical-data')
def historical_data():
    """إضافة بيانات تاريخية"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('historical_data.html')

@app.route('/payments')
def payments():
    """إدارة المدفوعات"""
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('payments.html')

# APIs
@app.route('/api/products')
def api_products():
    """API للمنتجات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, quantity FROM products")
    products = cursor.fetchall()
    conn.close()
    
    products_data = []
    for product in products:
        products_data.append({
            'id': product[0],
            'name': product[1],
            'selling_price': product[2],
            'current_quantity': product[3],
            'purchase_price': product[2] * 0.7,  # تقدير
            'alert_quantity': 5
        })
    
    return jsonify({'success': True, 'data': products_data})

@app.route('/api/customers')
def api_customers():
    """API للعملاء"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})
    
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, balance FROM customers")
    customers = cursor.fetchall()
    conn.close()
    
    customers_data = []
    for customer in customers:
        customers_data.append({
            'id': customer[0],
            'name': customer[1],
            'phone': customer[2] or '',
            'balance': customer[3],
            'address': ''
        })
    
    return jsonify({'success': True, 'data': customers_data})

@app.route('/api/suppliers')
def api_suppliers():
    """API للموردين"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone, balance FROM suppliers")
    suppliers = cursor.fetchall()
    conn.close()

    suppliers_data = []
    for supplier in suppliers:
        suppliers_data.append({
            'id': supplier[0],
            'name': supplier[1],
            'phone': supplier[2] or '',
            'balance': supplier[3],
            'address': ''
        })

    return jsonify({'success': True, 'data': suppliers_data})

@app.route('/api/products/add', methods=['POST'])
def api_add_product():
    """API لإضافة منتج جديد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})
    
    try:
        data = request.get_json()
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
            (data['name'], data['selling_price'], data.get('current_quantity', 0))
        )
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'تم إضافة المنتج بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/sales/add', methods=['POST'])
def api_add_sale():
    """API لإضافة مبيعة جديدة"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})
    
    try:
        data = request.get_json()
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # إضافة المبيعة
        cursor.execute(
            "INSERT INTO sales (customer_id, total_amount, payment_method) VALUES (?, ?, ?)",
            (data.get('customer_id'), data['total_amount'], data.get('payment_method', 'نقدي'))
        )
        sale_id = cursor.lastrowid
        
        # إضافة عناصر المبيعة
        for item in data.get('items', []):
            cursor.execute(
                "INSERT INTO sale_items (sale_id, product_id, quantity, price) VALUES (?, ?, ?, ?)",
                (sale_id, item['product_id'], item['quantity'], item['price'])
            )
            
            # تحديث المخزون
            cursor.execute(
                "UPDATE products SET quantity = quantity - ? WHERE id = ?",
                (item['quantity'], item['product_id'])
            )
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True, 
            'message': 'تم حفظ الفاتورة بنجاح',
            'sale_id': sale_id
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/sales')
def api_sales():
    """API للمبيعات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT s.id, s.customer_id, s.total_amount, s.payment_method, s.created_at, c.name
        FROM sales s
        LEFT JOIN customers c ON s.customer_id = c.id
        ORDER BY s.created_at DESC
    ''')
    sales = cursor.fetchall()
    conn.close()

    sales_data = []
    for sale in sales:
        sales_data.append({
            'id': sale[0],
            'customer_id': sale[1],
            'customer_name': sale[5] or 'عميل نقدي',
            'total_amount': sale[2],
            'payment_method': sale[3],
            'created_at': sale[4]
        })

    return jsonify({'success': True, 'data': sales_data})

@app.route('/api/sales/stats')
def api_sales_stats():
    """API لإحصائيات المبيعات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # إجمالي المبيعات اليوم
    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM sales WHERE date(created_at) = date('now')")
    today_sales = cursor.fetchone()[0]

    # إجمالي المبيعات هذا الشهر
    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM sales WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')")
    month_sales = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        'success': True,
        'data': {
            'today_sales': today_sales,
            'month_sales': month_sales
        }
    })

@app.route('/api/purchases')
def api_purchases():
    """API للمشتريات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    return jsonify({'success': True, 'data': []})

@app.route('/api/purchases/stats')
def api_purchases_stats():
    """API لإحصائيات المشتريات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    return jsonify({
        'success': True,
        'data': {
            'today_purchases': 0,
            'month_purchases': 0
        }
    })

@app.route('/api/customers/stats')
def api_customers_stats():
    """API لإحصائيات العملاء"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(balance), 0) FROM customers WHERE balance < 0")
    total_debt = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        'success': True,
        'data': {
            'total_customers': total_customers,
            'total_debt': abs(total_debt)
        }
    })

@app.route('/api/suppliers/stats')
def api_suppliers_stats():
    """API لإحصائيات الموردين"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM suppliers")
    total_suppliers = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(balance), 0) FROM suppliers WHERE balance > 0")
    total_payable = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        'success': True,
        'data': {
            'total_suppliers': total_suppliers,
            'total_payable': total_payable
        }
    })

@app.route('/api/dashboard/stats')
def api_dashboard_stats():
    """API لإحصائيات الصفحة الرئيسية"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # مبيعات اليوم
    cursor.execute("SELECT COALESCE(SUM(total_amount), 0) FROM sales WHERE date(created_at) = date('now')")
    today_sales = cursor.fetchone()[0]

    # عدد العملاء
    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    # عدد المنتجات
    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    # المنتجات المطلوبة
    cursor.execute("SELECT COUNT(*) FROM products WHERE quantity <= 5")
    low_stock = cursor.fetchone()[0]

    conn.close()

    return jsonify({
        'success': True,
        'data': {
            'today_sales': today_sales,
            'total_customers': total_customers,
            'total_products': total_products,
            'low_stock_products': low_stock
        }
    })

@app.route('/api/payments/add', methods=['POST'])
def api_add_payment():
    """API لإضافة مدفوعة جديدة"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()
        payment_type = data['type']  # 'customer' or 'supplier'
        entity_id = data['entity_id']
        amount = float(data['amount'])
        notes = data.get('notes', '')

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # تسجيل المدفوعة
        cursor.execute(
            "INSERT INTO payments (type, entity_id, amount, notes) VALUES (?, ?, ?, ?)",
            (payment_type, entity_id, amount, notes)
        )

        # تحديث رصيد العميل أو المورد
        if payment_type == 'customer':
            # تحصيل من عميل (تقليل الدين)
            cursor.execute(
                "UPDATE customers SET balance = balance + ? WHERE id = ?",
                (amount, entity_id)
            )
        else:  # supplier
            # دفع لمورد (تقليل المستحقات)
            cursor.execute(
                "UPDATE suppliers SET balance = balance - ? WHERE id = ?",
                (amount, entity_id)
            )

        conn.commit()
        conn.close()

        return jsonify({
            'success': True,
            'message': 'تم تسجيل المدفوعة بنجاح'
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/payments/history')
def api_payment_history():
    """API لسجل المدفوعات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # جلب سجل المدفوعات مع أسماء العملاء والموردين
        cursor.execute('''
            SELECT p.id, p.type, p.entity_id, p.amount, p.notes, p.created_at,
                   CASE
                       WHEN p.type = 'customer' THEN c.name
                       ELSE s.name
                   END as entity_name
            FROM payments p
            LEFT JOIN customers c ON p.type = 'customer' AND p.entity_id = c.id
            LEFT JOIN suppliers s ON p.type = 'supplier' AND p.entity_id = s.id
            ORDER BY p.created_at DESC
            LIMIT 100
        ''')

        payments = cursor.fetchall()
        conn.close()

        payments_data = []
        for payment in payments:
            payments_data.append({
                'id': payment[0],
                'type': payment[1],
                'entity_id': payment[2],
                'amount': payment[3],
                'notes': payment[4],
                'created_at': payment[5],
                'entity_name': payment[6]
            })

        return jsonify({'success': True, 'data': payments_data})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/products/edit/<int:product_id>', methods=['PUT'])
def api_edit_product(product_id):
    """API لتعديل منتج"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?",
            (data['name'], data['selling_price'], data.get('current_quantity', 0), product_id)
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم تحديث المنتج بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def api_delete_product(product_id):
    """API لحذف منتج"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم حذف المنتج بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/customers/add', methods=['POST'])
def api_add_customer():
    """API لإضافة عميل جديد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers (name, phone, balance) VALUES (?, ?, ?)",
            (data['name'], data.get('phone', ''), data.get('balance', 0))
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم إضافة العميل بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/customers/edit/<int:customer_id>', methods=['PUT'])
def api_edit_customer(customer_id):
    """API لتعديل عميل"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE customers SET name = ?, phone = ? WHERE id = ?",
            (data['name'], data.get('phone', ''), customer_id)
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم تحديث العميل بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/customers/delete/<int:customer_id>', methods=['DELETE'])
def api_delete_customer(customer_id):
    """API لحذف عميل"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم حذف العميل بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/suppliers/add', methods=['POST'])
def api_add_supplier():
    """API لإضافة مورد جديد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO suppliers (name, phone, balance) VALUES (?, ?, ?)",
            (data['name'], data.get('phone', ''), data.get('balance', 0))
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم إضافة المورد بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/suppliers/edit/<int:supplier_id>', methods=['PUT'])
def api_edit_supplier(supplier_id):
    """API لتعديل مورد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.get_json()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE suppliers SET name = ?, phone = ? WHERE id = ?",
            (data['name'], data.get('phone', ''), supplier_id)
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم تحديث المورد بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/api/suppliers/delete/<int:supplier_id>', methods=['DELETE'])
def api_delete_supplier(supplier_id):
    """API لحذف مورد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM suppliers WHERE id = ?", (supplier_id,))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'تم حذف المورد بنجاح'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

# APIs المرتجعات والاستبدال
@app.route('/api/returns')
def get_returns():
    """API لجلب جميع المرتجعات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # إنشاء جدول المرتجعات إذا لم يكن موجوداً
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS returns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                return_type TEXT NOT NULL,
                original_invoice_id INTEGER,
                total_amount REAL NOT NULL,
                reason TEXT NOT NULL,
                notes TEXT,
                status TEXT DEFAULT 'completed',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            SELECT id, return_type, original_invoice_id, total_amount, reason,
                   notes, status, created_at
            FROM returns
            ORDER BY created_at DESC
        """)

        returns = []
        for row in cursor.fetchall():
            returns.append({
                'id': row[0],
                'return_type': row[1],
                'original_invoice_id': row[2],
                'total_amount': float(row[3]),
                'reason': row[4],
                'notes': row[5],
                'status': row[6],
                'created_at': row[7]
            })

        conn.close()
        return jsonify({'success': True, 'data': returns})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/returns/add', methods=['POST'])
def add_return():
    """API لإضافة مرتجع جديد"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        data = request.json
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # إضافة المرتجع
        cursor.execute("""
            INSERT INTO returns (return_type, original_invoice_id, total_amount, reason, notes, status)
            VALUES (?, ?, ?, ?, ?, 'completed')
        """, (
            data['return_type'],
            data.get('original_invoice_id'),
            data['total_amount'],
            data['reason'],
            data.get('notes', '')
        ))

        return_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'return_id': return_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/returns/stats')
def get_returns_stats():
    """API لإحصائيات المرتجعات"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'غير مصرح'})

    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # إنشاء جدول المرتجعات إذا لم يكن موجوداً
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS returns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                return_type TEXT NOT NULL,
                original_invoice_id INTEGER,
                total_amount REAL NOT NULL,
                reason TEXT NOT NULL,
                notes TEXT,
                status TEXT DEFAULT 'completed',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # مرتجعات اليوم
        cursor.execute("""
            SELECT COUNT(*), COALESCE(SUM(total_amount), 0)
            FROM returns
            WHERE date(created_at) = date('now')
        """)
        today_stats = cursor.fetchone()

        # مرتجعات الشهر
        cursor.execute("""
            SELECT COUNT(*), COALESCE(SUM(total_amount), 0)
            FROM returns
            WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
        """)
        month_stats = cursor.fetchone()

        # إجمالي المرتجعات
        cursor.execute("SELECT COUNT(*), COALESCE(SUM(total_amount), 0) FROM returns")
        total_stats = cursor.fetchone()

        # معدل الإرجاع
        cursor.execute("SELECT COUNT(*) FROM sales WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')")
        month_sales = cursor.fetchone()[0]

        return_rate = (month_stats[0] / month_sales * 100) if month_sales > 0 else 0

        conn.close()

        return jsonify({
            'success': True,
            'data': {
                'today_returns': today_stats[0],
                'today_amount': float(today_stats[1]),
                'month_returns': month_stats[0],
                'month_amount': float(month_stats[1]),
                'total_returns': total_stats[0],
                'total_amount': float(total_stats[1]),
                'return_rate': round(return_rate, 2)
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # إنشاء قاعدة البيانات
    init_db()
    
    print("🚀 تشغيل نظام نقطة البيع المبسط...")
    print("📱 الرابط: http://localhost:5001")
    print("🔐 بيانات الدخول:")
    print("   اسم المستخدم: admin")
    print("   كلمة المرور: 3110")
    print("=" * 50)
    
    try:
        socketio.run(app, host='0.0.0.0', port=5001, debug=False)
    except Exception as e:
        print(f"❌ خطأ في تشغيل التطبيق: {e}")
        input("اضغط Enter للخروج...")
