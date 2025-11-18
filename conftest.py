import requests
import random
import string
import pytest

from data import COURIER_CREATE_API, COURIER_LOGIN_API, COURIER_DELETE_API


def generate_courier_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    return login, password, first_name


@pytest.fixture
def courier():
    login, password, first_name = generate_courier_data()
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    create_response = requests.post(COURIER_CREATE_API, json=payload)
    
    courier_id = None
    if create_response.status_code == 201:
        login_response = requests.post(
            COURIER_LOGIN_API,
            json={"login": login, "password": password}
        )
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
    
    courier_data = {
        "login": login,
        "password": password,
        "first_name": first_name,
        "courier_id": courier_id
    }
    
    yield courier_data
    
    if courier_id:
        requests.delete(COURIER_DELETE_API.format(courier_id=courier_id)) 