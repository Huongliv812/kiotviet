from function.base_function import create_bitable_field, get_bitable_fields, create_bitable_record

def process_product(client, table_id, product_data):
    # Danh sách các trường cần thiết
    required_fields = ['product_id', 'product_code', 'product_name', 'base_price', 'category_name', 
                       'branch_name', 'on_hand', 'reserved', 'cost']

    # Lấy danh sách các fields hiện có trong Bitable
    bitable_fields = get_bitable_fields(client, table_id)

    # Kiểm tra và chỉ tạo những trường cần thiết nếu chúng chưa tồn tại
    for field in required_fields:
        if field not in bitable_fields:
            new_field = create_bitable_field(client, table_id, field)
            if new_field:
                bitable_fields[field] = new_field

    processed_data = []

    for product in product_data.get('data', []):
        product_info = {
            'product_id': product.get('id'),
            'product_code': product.get('code'),
            'product_name': product.get('name'),
            'base_price': product.get('basePrice'),
            'category_name': product.get('categoryName')
        }

        for inventory in product.get('inventories', []):
            inventory_info = {
                'branch_name': inventory.get('branchName'),
                'on_hand': inventory.get('onHand', 0),
                'reserved': inventory.get('reserved', 0),
                'cost': inventory.get('cost', 0.0)
            }

            combined_info = {**product_info, **inventory_info}
            processed_data.append(combined_info)

    # Chèn dữ liệu vào Bitable
    for record in processed_data:
        create_bitable_record(client, table_id, record, list(record.keys()), bitable_fields)
