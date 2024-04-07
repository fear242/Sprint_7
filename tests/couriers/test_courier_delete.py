import requests


class TestCourierDelete:

    def test_delete_existing_courier(self,register_new_courier_and_return_login_password):
        login_pass = register_new_courier_and_return_login_password
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        courier = response.json()["id"]
        response_1 = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier}')
        assert response.status_code == 200
        assert response_1.text == '{"ok":true}'

    def test_delete_non_existing_courier(self):
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/0')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Курьера с таким id нет."}'

    def test_delete_without_id(self):
        response = requests.delete('https://qa-scooter.praktikum-services.ru/api/v1/courier/')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Not Found."}'

