import requests

def get_contact_list(kiotviet_token, retailer, include_total=True, include_customer_group=True, include_customer_social=True, order_direction="desc", order_by="createdDate", page_size=None, current_item=None):
    url = 'https://public.kiotapi.com/customers'
    
    headers = {
        'Authorization': f'Bearer {kiotviet_token}',
        'Retailer': retailer
    }

    # Tham số truy vấn
    params = {}

    if include_total:
        params['includeTotal'] = include_total
    if include_customer_group:
        params['includeCustomerGroup'] = include_customer_group
    if include_customer_social:
        params['includeCustomerSocial'] = include_customer_social
    if order_direction:
        params['orderDirection'] = order_direction
    if order_by:
        params['orderBy'] = order_by
    if page_size:
        params['pageSize'] = page_size
    if current_item:
        params['currentItem'] = current_item

    # Gọi API
    response = requests.get(url, headers=headers, params=params)

    # Kiểm tra response
    if response.status_code == 200:
        print("Customer list retrieved successfully.")
        return response.json()  # Trả về JSON chứa danh sách khách hàng
    else:
        print(f"Failed to retrieve customers. Status code: {response.status_code}")
        return None
