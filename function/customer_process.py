from function.base_function import create_bitable_record, create_bitable_field, get_bitable_fields

def process_customer(client, table_id, customer_data):
    # Danh sách các trường cần thiết
    required_fields = ['customer_id', 'customer_code', 'customer_name', 'contact_number', 
                       'email', 'address', 'created_at', 'modified_at', 'debt', 
                       'total_invoiced', 'total_revenue', 'total_point', 'branch_id',
                       'location_name', 'ward_name']

    # Lấy danh sách các fields hiện có trong Bitable
    bitable_fields = get_bitable_fields(client, table_id)
    
    # Kiểm tra và chỉ tạo những trường cần thiết nếu chúng chưa tồn tại
    for field in required_fields:
        if field not in bitable_fields:
            new_field = create_bitable_field(client, table_id, field)
            if new_field:
                bitable_fields[field] = new_field

    # Xử lý từng khách hàng
    for customer in customer_data.get('data', []):
        customer_info = {
            "customer_id": customer.get("id"),
            "customer_code": customer.get("code"),
            "customer_name": customer.get("name", ""),
            "contact_number": customer.get("contactNumber", ""),
            "email": customer.get("email", ""),
            "address": customer.get("address", ""),
            "created_at": customer.get("createdDate", ""),
            "modified_at": customer.get("modifiedDate", ""),
            "debt": customer.get("debt", 0),
            "total_invoiced": customer.get("totalInvoiced", 0),
            "total_revenue": customer.get("totalRevenue", 0),
            "total_point": customer.get("totalPoint", 0),
            "branch_id": customer.get("branchId", ""),
            "location_name": customer.get("locationName", ""),
            "ward_name": customer.get("wardName", "")
        }

        # Chèn dữ liệu vào Bitable
        create_bitable_record(client, table_id, customer_info, list(customer_info.keys()), bitable_fields)
