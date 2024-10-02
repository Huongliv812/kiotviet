import requests

def get_order_list(kiotviet_token, retailer, page_size=None, current_item=None, order_by=None, order_direction=None, include_payment=False, include_order_delivery=False):
    url = 'https://public.kiotapi.com/orders/'

    headers = {
        'Authorization': f'Bearer {kiotviet_token}',
        'Retailer': retailer
    }

    # Tham số truy vấn
    params = {}

    if page_size:
        params['pageSize'] = page_size
    if current_item:
        params['currentItem'] = current_item
    if order_by:
        params['orderBy'] = order_by
    if order_direction:
        params['orderDirection'] = order_direction
    if include_payment:
        params['includePayment'] = str(include_payment).lower()
    if include_order_delivery:
        params['includeOrderDelivery'] = str(include_order_delivery).lower()

    # Gọi API
    response = requests.get(url, headers=headers, params=params)

    # Kiểm tra kết quả
    if response.status_code == 200:
        print("Order list retrieved successfully.")
        return response.json()  # Trả về JSON chứa danh sách đơn hàng
    else:
        print(f"Failed to retrieve orders. Status code: {response.status_code}")
        return None
