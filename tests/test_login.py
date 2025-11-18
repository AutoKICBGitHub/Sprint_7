import requests
import pytest
import allure

from data import (
    COURIER_LOGIN_API,
    LOGIN_MISSING_FIELD_MESSAGE,
    LOGIN_NOT_FOUND_MESSAGE,
    TEST_NONEXISTENT_LOGIN,
    TEST_NONEXISTENT_PASSWORD,
    TEST_WRONG_PASSWORD,
)


@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Успешная авторизация курьера")
    def test_courier_can_login_and_receive_id(self, courier):
        payload = {"login": courier["login"], "password": courier["password"]}
        response = requests.post(COURIER_LOGIN_API, json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка при отсутствии обязательных полей")
    def test_login_requires_all_fields(self, courier):
        payload = {"password": courier["password"]}
        response = requests.post(COURIER_LOGIN_API, json=payload)
        assert response.status_code == 400
        assert response.json().get("message") == LOGIN_MISSING_FIELD_MESSAGE

    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_nonexistent_user_returns_error(self):
        payload = {
            "login": TEST_NONEXISTENT_LOGIN,
            "password": TEST_NONEXISTENT_PASSWORD
        }
        response = requests.post(COURIER_LOGIN_API, json=payload)
        assert response.status_code == 404
        assert response.json().get("message") == LOGIN_NOT_FOUND_MESSAGE

    @allure.title("Ошибка при неправильном пароле")
    def test_login_wrong_password_returns_error(self, courier):
        payload = {
            "login": courier["login"],
            "password": TEST_WRONG_PASSWORD
        }
        response = requests.post(COURIER_LOGIN_API, json=payload)
        assert response.status_code == 404
        assert response.json().get("message") == LOGIN_NOT_FOUND_MESSAGE

