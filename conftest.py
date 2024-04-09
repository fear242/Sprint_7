import json
import pytest
import random
import string
import requests
import allure
from data import UserData


URL_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/'
URL_orders = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/'


@pytest.fixture()
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string


@allure.title('Генерация и возврат учётных данных курьера')
@pytest.fixture()
def generate_and_return_login_password_without_registration(generate_random_string):
    login = generate_random_string
    password = generate_random_string
    first_name = generate_random_string

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


@allure.title('Регистрация курьера и возврат его данных')
@allure.description('Фикстура возыращает список из login, password, firstName, id курьера. И удаляет его по завершении '
                    'теста')
@pytest.fixture()
def register_new_courier_and_return_login_password(generate_random_string):
    login_pass = []

    login = generate_random_string
    password = generate_random_string
    first_name = generate_random_string

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(URL_courier, data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    payload_login = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response_login = requests.post(f'{URL_courier}login', data=payload_login)
    if response_login.status_code == 200:
        courier_id = response_login.json()["id"]
        login_pass.append(courier_id)

    yield login_pass
    requests.delete(f'{URL_courier}:id', data=payload)


@allure.title('Создание заказа и возврат track и id списком')
@pytest.fixture()
def create_order_return_data():
    payload = {
        "firstName": UserData.firstName,
        "lastName": UserData.lastName,
        "address": UserData.address,
        "metroStation": 4,
        "phone": UserData.phone,
        "rentTime": 5,
        "deliveryDate": UserData.deliveryDate,
        "comment": UserData.comment,
        "color": ["BLACK"]
    }
    payload_string = json.dumps(payload)
    response = requests.post(URL_orders, data=payload_string)
    track = response.json()["track"]
    response_1 = requests.get(f'{URL_orders}track?t={track}')
    order_id = response_1.json()["order"]["id"]
    order_data = [track, order_id]
    return order_data
