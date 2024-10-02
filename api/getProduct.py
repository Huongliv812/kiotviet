import requests

def get_product_list(kiotviet_token, retailer, page_size=None, current_item=None, include_inventory=True):
    url = 'https://public.kiotapi.com/products'

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
    if include_inventory:
        params['includeInventory'] = include_inventory

    # Gọi API
    response = requests.get(url, headers=headers, params=params)

    # Kiểm tra kết quả
    if response.status_code == 200:
        print("Product list retrieved successfully.")
        return response.json()  # Trả về JSON chứa danh sách sản phẩm
    else:
        print(f"Failed to retrieve products. Status code: {response.status_code}")
        return None
