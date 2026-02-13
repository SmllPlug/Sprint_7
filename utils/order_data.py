from faker import Faker


fake = Faker('ru_RU')
BASE_ORDER_DATA = {
    'firstName': fake.first_name_male(),
    "lastName": fake.last_name_male(),
    "address": fake.address(),
    "metroStation": 4,
    "phone": f'+7{fake.random_int(9000000000, 9999999999)}',
    "rentTime": 5,
    "deliveryDate": fake.date_between(
        start_date='-5y',
        end_date='today'
    ).strftime("%Y-%m-%d"),
    "comment": fake.text(max_nb_chars=50),
}

COLOR_ORDER_DATA = [
    (["BLACK"], "Черный цвет"),
    (["GREY"], "Серый цвет"),
    (["BLACK", "GREY"], "Оба цвета"),
    ([], "Без цвета")
]
