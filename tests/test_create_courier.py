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
    def test_courier_can_be_created(self, courier_for_creation_test):
        response = courier_for_creation_test["create_response"]
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_cannot_create_duplicate_courier(self, created_courier):
        payload = {
            "login": created_courier["login"],
            "password": created_courier["password"],
            "firstName": created_courier["first_name"]
        }
        response = requests.post(COURIER_CREATE_API, json=payload)
        assert response.status_code == 409
        assert response.json().get("message") == CREATE_DUPLICATE_MESSAGE

    @allure.title("Ошибка при отсутствии обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_missing_required_fields_return_error(self, missing_field):
        from helpers import generate_courier_data
        
        login, password, first_name = generate_courier_data()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        payload.pop(missing_field)
        response = requests.post(COURIER_CREATE_API, json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == CREATE_MISSING_FIELD_MESSAGE

