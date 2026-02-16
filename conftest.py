import pytest
import requests


from utils import helpers
from utils.urls import Urls


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
def created_courier():
    courier_data = helpers.create_courier_data()
    helpers.create_courier(courier_data)
    courier_id = helpers.get_courier_id(courier_data['login'], courier_data['password'])
    yield {
        'login': courier_data['login'],
        'password': courier_data['password'],
        'firstName': courier_data['firstName'],
        'courier_id': courier_id
    }
    if courier_id:
        helpers.delete_courier_by_id(courier_id)