import pytest
import requests
import allure

from data import ORDERS_CREATE_API, TEST_ORDER_COLORS, TEST_ORDER_PAYLOAD_TEMPLATE


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа с различными цветами")
    @pytest.mark.parametrize(
        "colors",
        [
            TEST_ORDER_COLORS["BLACK_ONLY"],
            TEST_ORDER_COLORS["GREY_ONLY"],
            TEST_ORDER_COLORS["BOTH_COLORS"],
            TEST_ORDER_COLORS["NO_COLOR"],
        ],
        ids=["black-only", "grey-only", "both-colors", "no-color"],
    )
    def test_create_order_with_various_colors(self, colors):
        payload = TEST_ORDER_PAYLOAD_TEMPLATE.copy()
        payload["color"] = colors
        response = requests.post(ORDERS_CREATE_API, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()

