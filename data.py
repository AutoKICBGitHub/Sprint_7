BASE_URL = "https://qa-scooter.praktikum-services.ru"

COURIER_CREATE_API = f"{BASE_URL}/api/v1/courier"
COURIER_LOGIN_API = f"{BASE_URL}/api/v1/courier/login"
COURIER_DELETE_API = f"{BASE_URL}/api/v1/courier/{{courier_id}}"

ORDERS_CREATE_API = f"{BASE_URL}/api/v1/orders"
ORDERS_LIST_API = f"{BASE_URL}/api/v1/orders"
ORDERS_CANCEL_API = f"{BASE_URL}/api/v1/orders/cancel"

CREATE_MISSING_FIELD_MESSAGE = "Недостаточно данных для создания учетной записи"
CREATE_DUPLICATE_MESSAGE = "Этот логин уже используется. Попробуйте другой."

LOGIN_MISSING_FIELD_MESSAGE = "Недостаточно данных для входа"
LOGIN_NOT_FOUND_MESSAGE = "Учетная запись не найдена"

TEST_NONEXISTENT_LOGIN = "nonexistent_user_12345"
TEST_NONEXISTENT_PASSWORD = "somepass123"
TEST_WRONG_PASSWORD = "wrongpassword123"
TEST_ORDER_COLORS = {
    "BLACK_ONLY": ["BLACK"],
    "GREY_ONLY": ["GREY"],
    "BOTH_COLORS": ["BLACK", "GREY"],
    "NO_COLOR": [],
}

TEST_ORDER_PAYLOAD_TEMPLATE = {
    "firstName": "Тест",
    "lastName": "Тестов",
    "address": "Тестовая улица, дом 1",
    "metroStation": 4,
    "phone": "+79991234567",
    "rentTime": 5,
    "deliveryDate": "2024-12-31",
    "comment": "Тестовый комментарий",
    "color": []
}

