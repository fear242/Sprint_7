import requests
import allure


URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'


class TestCourierDelete:

    @allure.title('Проверка удаления существующего курьера')
    def test_delete_existing_courier(self,register_new_courier_and_return_login_password):

        login_pass = register_new_courier_and_return_login_password
        payload = {
            "login": login_pass[0],
            "password": login_pass[1]
        }
        response = requests.post(f'{URL}/login', data=payload)
        courier = response.json()["id"]
        response_1 = requests.delete(f'{URL}/{courier}')

        assert response.status_code == 200
        assert response_1.text == '{"ok":true}'

    @allure.title('Проверка удаления несуществующего курьера')
    def test_delete_non_existing_courier(self):

        response = requests.delete(f'{URL}/0')

        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Курьера с таким id нет."}'

    @allure.title('Проверка удаления курьера, запрос без айди')
    def test_delete_without_id(self):

        response = requests.delete(URL)

        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Not Found."}'

