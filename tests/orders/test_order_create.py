import pytest
import requests
import json
import allure
from data import UserData


URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'


class TestOrderCreate:

    @allure.title('Проверка создания заказа самокатов разного цвета')
    @pytest.mark.parametrize('color', ["BLACK", "GREY", "BLACK, GREY", ""])
    def test_order_creation(self, color):

        payload = {
            "firstName": UserData.firstName,
            "lastName": UserData.lastName,
            "address": UserData.address,
            "metroStation": 4,
            "phone": UserData.phone,
            "rentTime": 5,
            "deliveryDate": UserData.deliveryDate,
            "comment": UserData.comment,
            "color": [color]
        }
        payload_string = json.dumps(payload)
        response = requests.post(URL, data=payload_string)

        assert response.status_code == 201
        assert "track" in response.text
