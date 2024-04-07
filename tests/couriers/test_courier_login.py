import requests


class TestCourierLogin:

    def test_login_existing_courier(self, register_new_courier_and_return_login_password):
        courier_data = register_new_courier_and_return_login_password
        payload = {
            "login": courier_data[0],
            "password": courier_data[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        assert "id" in response.text

    def test_login_non_existing_courier(self, generate_and_return_login_password_without_registration):
        courier_data = generate_and_return_login_password_without_registration
        payload = {
            "login": courier_data["login"],
            "password": courier_data["password"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Учетная запись не найдена"}'

    def test_login_courier_without_password(self, register_new_courier_and_return_login_password):
        courier_data = register_new_courier_and_return_login_password
        payload = {
            "login": courier_data[0],
            "password": ''
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для входа"}'
