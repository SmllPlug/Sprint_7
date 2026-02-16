import requests
import random
import string


from utils.urls import Urls
from allure import step


@step('Генерация рандомной строки длинной {length}')
def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

@step('Создание данных для курьера')
def create_courier_data():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
          'login': login,
          'password': password,
          'firstName': first_name
    }

@step('Создание курьера без логина')
def create_courier_without_login():
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return {
          'password': password,
          'firstName': first_name
    }

@step('Создание курьера без пароля')
def create_courier_without_password():
      login = generate_random_string(10)
      first_name = generate_random_string(10)
      return {
              'login': login,
              'firstName': first_name
      }

@step('Создание курьера')
def create_courier(payload):
      return requests.post(Urls.CREATE_COURIER, json=payload)

@step('Регистрация нового курьера')
def register_new_courier_and_return_login_password():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
          'login': login,
          'password': password,
          'firstName': first_name
    }
    response = requests.post(Urls.CREATE_COURIER, json=payload)
    if response.status_code == 201:
          login_pass.append(login)
          login_pass.append(password)
          login_pass.append(first_name)
    return login_pass

@step('Авторизация курьера')
def login_courier(login, password):
      payload = {
            'login': login,
            'password': password
      }
      response = requests.post(Urls.LOGIN_COURIER, json=payload)
      return response

@step('Получения ID курьера')
def get_courier_id(login, password):
      response = login_courier(login, password)
      if response.status_code == 200:
            return response.json().get('id')
      return None

@step('Удаление курьера')
def delete_courier_by_id(courier_id):
      return requests.delete(f'{Urls.DELETE_COURIER}{courier_id}')

@step('Создание заказа')
def create_order(order_data):
      return requests.post(Urls.CREATE_ORDER, json=order_data)

@step('Получение списка заказов')
def get_order_list():
      return requests.get(Urls.GET_ORDER_LIST)

@step('Получение заказа по его номеру')
def get_order_by_track(track_number):
      return requests.get(Urls.GET_ORDER_BY_TRACK, params={'t': track_number})

@step('Принятие заказа')
def take_order(order_id, courier_id):
      url = f'{Urls.TAKE_ORDER}{order_id}'
      return requests.put(url, params={'courierId': courier_id})