import copy
import allure
import pytest


from utils import helpers
from utils.order_data import BASE_ORDER_DATA


class TestCreateOrder:
    @allure.title('Проверка создания заказа с параметризацией, статус код 201')
    @allure.step('Отправляем POST запрос на создание с параметризацией')
    @pytest.mark.parametrize(
        "payload, description",
        [
            ({"color": ["BLACK"]}, "Черный цвет"),
            ({"color": ["GREY"]}, "Серый цвет"),
            ({"color": ["BLACK", "GREY"]}, "Оба цвета"),
            ({}, "Без цвета (поле color не передаём)"),
        ]
    )
    def test_create_order_status_code(self, payload, description):
        order_data = copy.deepcopy(BASE_ORDER_DATA)
        order_data.update(payload) 
        response = helpers.create_order(order_data)
        assert response.status_code == 201

    @allure.title('Проверка создания заказа с параметризацией, в ответе не пустой track_id')
    @allure.step('Отправляем POST запрос на создание с параметризацией')
    @pytest.mark.parametrize(
        "payload, description",
        [
            ({"color": ["BLACK"]}, "Черный цвет"),
            ({"color": ["GREY"]}, "Серый цвет"),
            ({"color": ["BLACK", "GREY"]}, "Оба цвета"),
            ({}, "Без цвета (поле color не передаём)"),
        ]
    )
    def test_create_order_returns_track(self, payload, description):
        order_data = copy.deepcopy(BASE_ORDER_DATA)
        order_data.update(payload) 
        response = helpers.create_order(order_data)
        assert response.json().get("track") is not None