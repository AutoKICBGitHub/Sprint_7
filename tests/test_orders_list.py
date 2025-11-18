import requests
import allure

from data import ORDERS_LIST_API


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_orders_list_contains_orders_array(self):
        response = requests.get(ORDERS_LIST_API)
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

