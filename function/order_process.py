from function.base_function import create_bitable_field, get_bitable_fields, create_bitable_record

def process_order(client, table_id, order_data):
    # Danh sách các trường cần thiết (cập nhật cho KiotViet)
    required_fields = ['order_id', 'order_code', 'customer_name', 'customer_phone',
                       'customer_email', 'address', 'province', 'district', 'ward',
                       'status', 'payment_status', 'total_price',
                       'product_code', 'product_name', 'product_quantity', 'product_price']

    # Lấy danh sách các fields hiện có trong Bitable
    bitable_fields = get_bitable_fields(client, table_id)
    
    # Kiểm tra và chỉ tạo những trường cần thiết nếu chúng chưa tồn tại
    for field in required_fields:
        if field not in bitable_fields:
            new_field = create_bitable_field(client, table_id, field)
            if new_field:
                bitable_fields[field] = new_field

    processed_data = []

    for order in order_data.get('data', []):
        order_id = order['id']
        order_code = order.get('code', 'N/A')
        customer_name = order.get('customerName', 'Unknown')
        customer_phone = order.get('orderDelivery', {}).get('contactNumber', 'Unknown')
        customer_email = order.get('customerEmail', 'N/A')  # Kiểm tra xem có trường này không
        total_price = order.get('total', 0)
        payment_status = order.get('paymentStatus', 'N/A')  # Cập nhật nếu có trường này
        status = order.get('statusValue', 'N/A')

        # Địa chỉ giao hàng
        order_delivery = order.get('orderDelivery', {})
        address = order_delivery.get('address', '')
        # KiotViet không cung cấp chi tiết province, district, ward riêng lẻ trong ví dụ, nên bạn cần xử lý nếu có

        # Lặp qua từng sản phẩm trong đơn hàng
        for item in order.get('orderDetails', []):
            product_code = item.get('productCode', 'Unknown')
            product_name = item.get('productName', 'Unknown')
            product_quantity = item.get('quantity', 1)
            product_price = item.get('price', 0)

            processed_data.append({
                'order_id': order_id,
                'order_code': order_code,
                'customer_name': customer_name,
                'customer_phone': customer_phone,
                'customer_email': customer_email,
                'address': address,
                'province': '',   # Nếu có, hãy cập nhật trường này
                'district': '',   # Nếu có, hãy cập nhật trường này
                'ward': '',       # Nếu có, hãy cập nhật trường này
                'status': status,
                'payment_status': payment_status,
                'total_price': total_price,
                'product_code': product_code,
                'product_name': product_name,
                'product_quantity': product_quantity,
                'product_price': product_price
            })

    # Chèn dữ liệu vào Bitable
    for record in processed_data:
        create_bitable_record(client, table_id, record, list(record.keys()), bitable_fields)
