import requests
import allure

from data import ORDERS_LIST_API


@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_orders_list_contains_orders_array(self):
        with allure.step("Получить список заказов"):
            response = requests.get(ORDERS_LIST_API)
        
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 200
        
        with allure.step("Проверить наличие поля orders в ответе"):
            assert "orders" in response.json()
        
        with allure.step("Проверить что orders является списком"):
            assert isinstance(response.json()["orders"], list)

