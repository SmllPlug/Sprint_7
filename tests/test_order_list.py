import allure
import requests


from utils import helpers
from utils.urls import Urls


class TestOrderList:
    @allure.title('Проверка получения списка заказов, статус код 200')
    @allure.step('Отправляем GET запрос на получение списка заказов')
    def test_get_order_list_status_code(self):
        response = helpers.get_order_list()
        assert response.status_code == 200

    @allure.title('Проверка получения списка заказов, в ответе есть список заказов')
    @allure.step('Отправляем GET запрос на получение списка заказов')
    def test_get_order_list_has_orders(self):
        response = helpers.get_order_list()
        assert isinstance(response.json().get('orders'), list)

    @allure.title('Проверка получения списка заказов c несуществующим курьером, статус код 404')
    @allure.step('Отправляем GET запрос на получение списка заказов')
    def test_get_order_list_with_invalid_courier_id_status_code(self):
        response = requests.get(Urls.GET_ORDER_LIST, params={"courierId": 999999999})
        assert response.status_code == 404

    @allure.title('Проверка получения списка заказов c несуществующим курьером, в ответе "message": "Курьер с идентификатором courierId не найден"')
    @allure.step('Отправляем GET запрос на получение списка заказов')
    def test_get_order_list_with_invalid_courier_id_message(self):
        response = requests.get(Urls.GET_ORDER_LIST, params={"courierId": 999999999})
        assert response.json()["message"] == "Курьер с идентификатором 999999999 не найден"