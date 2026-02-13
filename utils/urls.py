class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = f'{BASE_URL}/api/v1/courier'
    LOGIN_COURIER = f'{BASE_URL}/api/v1/courier/login'
    # Требует Id курьера в конце запроса
    DELETE_COURIER = f'{BASE_URL}/api/v1/courier/'
    CREATE_ORDER = f'{BASE_URL}/api/v1/orders'
    GET_ORDER_LIST = f'{BASE_URL}/api/v1/orders'
    # Требует Id заказа в конце запроса
    TAKE_ORDER = f'{BASE_URL}/api/v1/orders/accept/'
    GET_ORDER_BY_TRACK = f'{BASE_URL}/api/v1/orders/track'