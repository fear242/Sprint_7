import json
import pytest
import requests
import random
import string
from data import UserData


@pytest.fixture()
def generate_and_return_login_password_without_registration():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    yield payload
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/:id', data=payload)


@pytest.fixture()
def register_new_courier_and_return_login_password():

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    yield login_pass
    requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/:id', data=payload)


@pytest.fixture()
def create_order_return_id():
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
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload_string)
    track = response.json()["track"]
    response_1 = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
    order = response_1.json()["order"]["id"]
    return order


@pytest.fixture()
def create_order_return_track():
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
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload_string)
    track = response.json()["track"]
    return track


@pytest.fixture()
def create_and_login_courier_return_id():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload_register = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload_register)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    payload_login = {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload_login)
    courier = response.json()["id"]
    yield courier
    requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier}')
