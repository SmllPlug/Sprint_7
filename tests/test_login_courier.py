import requests
import allure


from utils.urls import Urls
from utils import helpers


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера с валидными данными, статус код 200')
    @allure.step('Отправляем POST запрос на авторизацию курьера с валидными данными')
    def test_login_courier_with_valid_data_status_code(self, created_courier):
        response = helpers.login_courier(created_courier['login'], created_courier['password'])
        assert response.status_code == 200

    @allure.title('Проверка авторизации курьера с валидными данными, в ответе есть id курьера')
    @allure.step('Отправляем POST запрос на авторизацию курьера с валидными данными')
    def test_login_courier_with_valid_data_has_id(self, created_courier):
        response = helpers.login_courier(created_courier['login'], created_courier['password'])
        assert response.json().get('id') is not None
    
    @allure.title('Проверка авторизации курьера с несуществующим логином, статус код 404')
    @allure.step('Отправляем POST запрос на авторизацию курьера с несуществующим логином')
    def test_login_courier_with_nonexistent_login_status_code(self, created_courier):
        wrong_login = created_courier['login'] + 'wrong'
        response = helpers.login_courier(wrong_login, created_courier['password'])
        assert response.status_code == 404

    @allure.title('Проверка авторизации курьера с несуществующим логином, в ответе "message": "Учетная запись не найдена"')
    @allure.step('Отправляем POST запрос на авторизацию курьера с несуществующим логином')
    def test_login_courier_with_nonexistent_login_message(self, created_courier):
        wrong_login = created_courier['login'] + 'wrong'
        response = helpers.login_courier(wrong_login, created_courier['password'])
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка авторизации курьера с несуществующим паролем, статус код 404')
    @allure.step('Отправляем POST запрос на авторизацию курьера с несуществующим паролем')
    def test_login_courier_with_nonexistent_password_status_code(self, created_courier):
        wrong_password = created_courier['password'] + 'wrong'
        response = helpers.login_courier(created_courier['login'], wrong_password)
        assert response.status_code == 404

    @allure.title('Проверка авторизации курьера с несуществующим паролем, в ответе "message": "Учетная запись не найдена"')
    @allure.step('Отправляем POST запрос на авторизацию курьера с несуществующим паролем')
    def test_login_courier_with_nonexistent_password_message(self, created_courier):
        wrong_password = created_courier['password'] + 'wrong'
        response = helpers.login_courier(created_courier['login'], wrong_password)
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка авторизации несуществующего курьера, статус код 404')
    @allure.step('Отправляем POST запрос на авторизацию несуществующего курьера')
    def test_login_nonexistent_courier_status_code(self):
        courier_data = helpers.create_courier_data()
        response = helpers.login_courier(courier_data['login'], courier_data['password'])
        assert response.status_code == 404

    @allure.title('Проверка авторизации несуществующего курьера, в ответе "message": "Учетная запись не найдена"')
    @allure.step('Отправляем POST запрос на авторизацию несуществующего курьера')
    def test_login_nonexistent_courier_message(self):
        courier_data = helpers.create_courier_data()
        response = helpers.login_courier(courier_data['login'], courier_data['password'])
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Проверка авторизации курьера без логина, статус код 400')
    @allure.step('Отправляем POST запрос на авторизацию курьера без логина')
    def test_login_courier_without_login_status_code(self, created_courier):
        response = requests.post(Urls.LOGIN_COURIER, json={
            'login': '',
            'password': created_courier['password']
            })
        assert response.status_code == 400

    @allure.title('Проверка авторизации курьера без логина, в ответе "message": "message":  "Недостаточно данных для входа"')
    @allure.step('Отправляем POST запрос на авторизацию курьера без логина')
    def test_login_courier_without_login_message(self, created_courier):
        response = requests.post(Urls.LOGIN_COURIER, json={
            'login': '',
            'password': created_courier['password']
            })
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Проверка авторизации курьера без пароля, статус код 400')
    @allure.step('Отправляем POST запрос на авторизацию курьера без пароля')
    def test_login_courier_without_password_status_code(self, created_courier):
        response = requests.post(Urls.LOGIN_COURIER, json={
            'login': created_courier['login'],
            "password": ""
            })
        assert response.status_code == 400

    @allure.title('Проверка авторизации курьера без пароля, в ответе "message": "message":  "Недостаточно данных для входа"')
    @allure.step('Отправляем POST запрос на авторизацию курьера без пароля')
    def test_login_courier_without_password_message(self, created_courier):
        response = requests.post(Urls.LOGIN_COURIER, json={
            'login': created_courier['login'],
            "password": ""
            })
        assert response.json()["message"] == "Недостаточно данных для входа"