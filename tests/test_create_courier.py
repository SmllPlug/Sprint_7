import requests
import allure


from utils.urls import Urls
from utils import helpers


class TestCreateCourier:
    @allure.title('Проверка создания курьера с валидными данными, статус код 201')
    @allure.step('Отправляем POST запрос на создание курьера с валидными данными')
    def test_create_courier_with_valid_data_status_code(self, cleanup_courier):
        courier_data = helpers.create_courier_data()
        response = helpers.create_courier(courier_data)
        courier_id = helpers.get_courier_id(courier_data['login'], courier_data['password']) 
        cleanup_courier(courier_id)
        assert response.status_code == 201

    @allure.title('Проверка созздания курьера с валидными данными, в ответе "ok":true')
    @allure.step('Отправляем POST запрос на создание курьера с валидными данными')
    def test_create_courier_with_valid_data_login_message(self, cleanup_courier):
        courier_data = helpers.create_courier_data()
        response = helpers.create_courier(courier_data)
        courier_id = helpers.get_courier_id(courier_data['login'], courier_data['password']) 
        cleanup_courier(courier_id)
        assert response.json() == {"ok": True}

    @allure.title('Проверка создания курьера с уже существующим логином, статус код 409')
    @allure.step('Отправляем POST запрос на создание курьера с уже существующим логином')
    def test_create_courier_with_existing_login_status_code(self, created_courier):
        response = requests.post(Urls.CREATE_COURIER, json={
            'login': created_courier['login'],
            'password': created_courier['password'],
            'firstName': created_courier['firstName']
        })
        assert response.status_code == 409

    @allure.title('Проверка создания курьера с уже существующим логином, в ответе "message": "Этот логин уже используется"')
    @allure.step('Отправляем POST запрос на создание курьера с уже существующим логином')
    def test_create_courier_with_existing_login_message(self, created_courier):
        response = requests.post(Urls.CREATE_COURIER, json={
            'login': created_courier['login'],
            'password': created_courier['password'],
            'firstName': created_courier['firstName']
        })
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Проверка создания курьера без логина, статус код 400')
    @allure.step('Отправляем POST запрос на создание курьера без логина')
    def test_create_courier_without_login_status_code(self):
        courier_without_login = helpers.create_courier_without_login()
        response = requests.post(Urls.CREATE_COURIER, json=courier_without_login)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера без логина, в ответе "message": "Недостаточно данных для создания учетной записи"')
    @allure.step('Отправляем POST запрос на создание курьера без логина')
    def test_create_courier_without_login_message(self):
        courier_without_login = helpers.create_courier_without_login()
        response = requests.post(Urls.CREATE_COURIER, json=courier_without_login)
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка создания курьера без пароля, статус код 400')
    @allure.step('Отправляем POST запрос на создание курьера без пароля')
    def test_create_courier_without_password_status_code(self):
        courier_without_password = helpers.create_courier_without_password()
        response = requests.post(Urls.CREATE_COURIER, json=courier_without_password)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера без пароля, в ответе "message": "Недостаточно данных для создания учетной записи"')
    @allure.step('Отправляем POST запрос на создание курьера без пароля')
    def test_create_courier_without_password_message(self):
        courier_without_password = helpers.create_courier_without_password()
        response = requests.post(Urls.CREATE_COURIER, json=courier_without_password)
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"