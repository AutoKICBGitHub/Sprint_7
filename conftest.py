import requests
import pytest

from data import (
    COURIER_CREATE_API,
    COURIER_LOGIN_API,
    COURIER_DELETE_API,
    ORDERS_CREATE_API,
    ORDERS_CANCEL_API,
    TEST_ORDER_PAYLOAD_TEMPLATE,
)
from helpers import generate_courier_data


@pytest.fixture
def created_courier():
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
        "courier_id": courier_id,
        "create_response": create_response
    }
    
    yield courier_data
    
    if courier_id:
        requests.delete(COURIER_DELETE_API.format(courier_id=courier_id))


@pytest.fixture
def courier(created_courier):
    return created_courier


@pytest.fixture
def created_order(request):
    colors = getattr(request, "param", [])
    payload = TEST_ORDER_PAYLOAD_TEMPLATE.copy()
    payload["color"] = colors
    
    create_response = requests.post(ORDERS_CREATE_API, json=payload)
    
    track = None
    if create_response.status_code == 201:
        track = create_response.json().get("track")
    
    order_data = {
        "track": track,
        "create_response": create_response
    }
    
    yield order_data
    
    if track:
        requests.put(ORDERS_CANCEL_API, json={"track": track}) 