from api.getProduct import get_product_list
from baseopensdk import BaseClient
from function.product_process import process_product

def test_add_product_record():
    # Giả lập thông tin kết nối và bảng
    APP_TOKEN = "EHVfbNry1a81WusjwX2lsCa3gyb"  # Thay bằng App Token của bạn
    PERSONAL_BASE_TOKEN = "pt-hYncnlcOR-K5XDLuooOTNvFi69hfFPh4Zkua4maRAQAAIMAA2h8AgZApcS7l"  # Thay bằng Personal Base Token của bạn
    TABLE_ID = "tblb9ymhgF5koawB"  # Thay bằng Table ID của bảng trong Bitable

    # Khởi tạo client Base
    client = BaseClient.builder() \
        .app_token(APP_TOKEN) \
        .personal_base_token(PERSONAL_BASE_TOKEN) \
        .build()

    # Gọi API KiotViet để lấy danh sách sản phẩm
    kiotviet_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJuYmYiOjE3Mjc4MzczODQsImV4cCI6MTcyNzkyMzc4NCwiaXNzIjoiaHR0cDovL2lkLmtpb3R2aWV0LnZuIiwiY2xpZW50X2lkIjoiODlkMWU4MDctMTFhOC00YzkyLTk2N2ItMTk2YjQ4NWU3OGRiIiwiY2xpZW50X1JldGFpbGVyQ29kZSI6ImJrZXNob3AiLCJjbGllbnRfUmV0YWlsZXJJZCI6IjgxMzk1NiIsImNsaWVudF9Vc2VySWQiOiI2MDU4NiIsImNsaWVudF9TZW5zaXRpdmVBcGkiOiJUcnVlIiwiY2xpZW50X0dyb3VwSWQiOiIyOCIsImlhdCI6MTcyNzgzNzM4NCwic2NvcGUiOlsiUHVibGljQXBpLkFjY2VzcyJdfQ.x_9xoHqB6xH57aa84iO76-bbPQ9rOSDI3Jsz4Q5NTRXX12IaCzbNI6QPuR4VOk1xjmKDOtojhu9o03yUaCOWvWZOpf-hZny0v6lIr6Hz-AtXTIzuJb52RvGrKu8pqzWyzSlnH5c7hDamLLt-g4BFBwJAKctADGIjJDvp4xOJ9McvEs3nKrHGabZeJvFjy8Rkn6OOOCKOucb-WKVcm1YZMioMxaHWZ-TZcLWGwYmg6oOUstJPdpb-dveeREl2eoP6hF7LG5FOMYRymcmrPd04WT0H9sGlS62mmFymdTjuQ88ZlRf7214goO_B-sNe__TYS0W0r7IqygKWJ8pAi7aHGQ"  # Thay bằng KiotViet Token của bạn
    retailer = "bkeshop"  # Thay bằng Retailer của bạn

    # Lấy danh sách sản phẩm từ API
    product_data = get_product_list(kiotviet_token, retailer, page_size=200, current_item=2)

    if product_data:
        # In ra dữ liệu để kiểm tra xem dữ liệu có được lấy về chính xác không
        print("Product data retrieved from KiotViet API:")
        print(product_data)

        # Xử lý và chèn dữ liệu vào Bitable
        process_product(client, TABLE_ID, product_data)
        print("Product data successfully synced to Bitable.")
    else:
        print("Failed to retrieve product data.")

if __name__ == "__main__":
    test_add_product_record()
