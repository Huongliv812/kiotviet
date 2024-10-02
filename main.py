from flask import Flask, request, render_template, redirect, url_for
from api.getProduct import get_product_list
from api.getOrderList import get_order_list
from api.getContactList import get_contact_list
from function.product_process import process_product
from function.order_process import process_order
from function.customer_process import process_customer
from baseopensdk import BaseClient

app = Flask(__name__, template_folder='view')

# Trang chọn loại đồng bộ
@app.route('/', methods=['GET', 'POST'])
def choose_type():
    if request.method == 'POST':
        api_type = request.form['api_type']
        if api_type == 'get_product':
            return redirect(url_for('product_form'))
        elif api_type == 'get_order':
            return redirect(url_for('order_form'))
        elif api_type == 'get_customer':
            return redirect(url_for('contact_form'))
    return render_template('choose_type.html')

# Trang đồng bộ sản phẩm
@app.route('/product_form', methods=['GET', 'POST'])
def product_form():
    if request.method == 'POST':
        APP_TOKEN = request.form['APP_TOKEN']
        PERSONAL_BASE_TOKEN = request.form['PERSONAL_BASE_TOKEN']
        TABLE_ID = request.form['TABLE_ID']
        KIOTVIET_TOKEN = request.form['KIOTVIET_TOKEN']
        page_size = request.form.get('pageSize')
        current_item = request.form.get('currentItem')

        # Gọi API KiotViet để lấy danh sách sản phẩm
        product_data = get_product_list(
            kiotviet_token=KIOTVIET_TOKEN, 
            retailer="bkeshop", 
            page_size=page_size, 
            current_item=current_item
        )

        if product_data:
            client = BaseClient.builder().app_token(APP_TOKEN).personal_base_token(PERSONAL_BASE_TOKEN).build()
            process_product(client, TABLE_ID, product_data)
            return "Product data successfully synced to Bitable."
        else:
            return "Failed to sync products."

    return render_template('product_form.html')

# Trang đồng bộ đơn hàng
@app.route('/order_form', methods=['GET', 'POST'])
def order_form():
    if request.method == 'POST':
        APP_TOKEN = request.form['APP_TOKEN']
        PERSONAL_BASE_TOKEN = request.form['PERSONAL_BASE_TOKEN']
        TABLE_ID = request.form['TABLE_ID']
        KIOTVIET_TOKEN = request.form['KIOTVIET_TOKEN']
        page_size = request.form.get('pageSize')
        current_item = request.form.get('currentItem')

        # Gọi API KiotViet để lấy danh sách đơn hàng
        order_data = get_order_list(
            kiotviet_token=KIOTVIET_TOKEN, 
            retailer="bkeshop", 
            page_size=page_size, 
            current_item=current_item
        )

        if order_data:
            client = BaseClient.builder().app_token(APP_TOKEN).personal_base_token(PERSONAL_BASE_TOKEN).build()
            process_order(client, TABLE_ID, order_data)
            return "Order data successfully synced to Bitable."
        else:
            return "Failed to sync orders."

    return render_template('order_form.html')

# Trang đồng bộ khách hàng
@app.route('/contact_form', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        APP_TOKEN = request.form['APP_TOKEN']
        PERSONAL_BASE_TOKEN = request.form['PERSONAL_BASE_TOKEN']
        TABLE_ID = request.form['TABLE_ID']
        KIOTVIET_TOKEN = request.form['KIOTVIET_TOKEN']
        page_size = request.form.get('pageSize')
        current_item = request.form.get('currentItem')

        # Gọi API KiotViet để lấy danh sách khách hàng
        customer_data = get_contact_list(
            kiotviet_token=KIOTVIET_TOKEN, 
            retailer="bkeshop", 
            page_size=page_size, 
            current_item=current_item
        )

        if customer_data:
            client = BaseClient.builder().app_token(APP_TOKEN).personal_base_token(PERSONAL_BASE_TOKEN).build()
            process_customer(client, TABLE_ID, customer_data)
            return "Customer data successfully synced to Bitable."
        else:
            return "Failed to sync customers."

    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
