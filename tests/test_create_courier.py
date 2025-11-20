import requests
import pytest
import allure

from data import (
    COURIER_CREATE_API,
    CREATE_DUPLICATE_MESSAGE,
    CREATE_MISSING_FIELD_MESSAGE,
)


@allure.feature("Создание курьера")
class TestCourierCreate:

    @allure.title("Успешное создание курьера")
    def test_courier_can_be_created(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["first_name"]
        }
        
        with allure.step("Создать курьера"):
            response = requests.post(COURIER_CREATE_API, json=payload)
        
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 201
        
        with allure.step("Проверить тело ответа"):
            assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, created_courier):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"],
            "firstName": created_courier["first_name"]
        }
        
        with allure.step("Попытаться создать курьера с уже существующим логином"):
            response = requests.post(COURIER_CREATE_API, json=payload)
        
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 409
        
        with allure.step("Проверить сообщение об ошибке"):
            assert response.json().get("message") == CREATE_DUPLICATE_MESSAGE

    @allure.title("Ошибка при отсутствии обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_missing_required_fields_return_error(self, courier_data, missing_field):
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"],
            "firstName": courier_data["first_name"]
        }
        payload.pop(missing_field)
        
        with allure.step(f"Создать курьера без обязательного поля {missing_field}"):
            response = requests.post(COURIER_CREATE_API, json=payload)
        
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 400
        
        with allure.step("Проверить сообщение об ошибке"):
            assert response.json().get("message") == CREATE_MISSING_FIELD_MESSAGE

