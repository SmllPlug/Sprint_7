import pytest
import requests


from utils import helpers
from utils.urls import Urls
from utils.order_data import BASE_ORDER_DATA


@pytest.fixture
def courier_data():
    return {
        'login': helpers.generate_random_string(10),
        'password': helpers.generate_random_string(10),
        'firstName': helpers.generate_random_string(10)
    }

@pytest.fixture
def courier_without_login():
    return {
        'password': helpers.generate_random_string(10),
        'firstName': helpers.generate_random_string(10)
    }

@pytest.fixture
def cleanup_courier():
    id_to_delete = []

    def register(courier_id):
        if courier_id is not None:
            id_to_delete.append(courier_id)
    yield register
    for courier_id in id_to_delete:
        helpers.delete_courier_by_id(courier_id)

@pytest.fixture
def courier_without_password():
    return {
        'login': helpers.generate_random_string(10),
        'firstName': helpers.generate_random_string(10)
    }   

@pytest.fixture
def created_courier(courier_data):
    response = requests.post(Urls.CREATE_COURIER, json=courier_data)
    assert response.status_code == 201
    courier_id = helpers.get_courier_id(courier_data['login'], courier_data['password'])
    assert courier_id is not None
    yield {
        'login': courier_data['login'],
        'password': courier_data['password'],
        'firstName': courier_data['firstName'],
        'courier_id': courier_id
    }
    helpers.delete_courier_by_id(courier_id)