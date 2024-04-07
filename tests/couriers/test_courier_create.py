import requests
import allure


class TestCourierCreation:

    @allure.title('Проверка регистрации нового курьера')
    def test_register_new_courier(self, generate_and_return_login_password_without_registration):
        payload = generate_and_return_login_password_without_registration
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'

    @allure.title('Проверка повторной регистрации курьера')
    def test_register_similar_courier(self, register_new_courier_and_return_login_password):
        login_pass = register_new_courier_and_return_login_password
        payload = {
            "login": login_pass[0],
            "password": login_pass[1],
            "firstName": login_pass[2]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409
        assert response.text == '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'

    @allure.title('Проверка регистрации курьера без указания пароля')
    def test_register_courier_without_password(self, generate_and_return_login_password_without_registration):
        login_pass = generate_and_return_login_password_without_registration
        payload = {
            "login": login_pass["login"],
            "firstName": login_pass["firstName"]
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
