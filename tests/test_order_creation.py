import pytest
import allure

from data import TEST_ORDER_COLORS


@allure.feature("Создание заказа")
class TestOrderCreation:

    @allure.title("Создание заказа с различными цветами")
    @pytest.mark.parametrize(
        "created_order",
        [
            TEST_ORDER_COLORS["BLACK_ONLY"],
            TEST_ORDER_COLORS["GREY_ONLY"],
            TEST_ORDER_COLORS["BOTH_COLORS"],
            TEST_ORDER_COLORS["NO_COLOR"],
        ],
        indirect=True,
        ids=["black-only", "grey-only", "both-colors", "no-color"],
    )
    def test_create_order_with_various_colors(self, created_order):
        response = created_order["create_response"]
        
        with allure.step("Проверить статус ответа"):
            assert response.status_code == 201
        
        with allure.step("Проверить наличие track в ответе"):
            assert "track" in response.json()

