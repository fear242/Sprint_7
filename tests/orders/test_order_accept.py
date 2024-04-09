import requests
import allure


URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/'


class TestOrderAccept:

    @allure.title('Проверка принятия существующего заказа существующим курьером')
    def test_take_order_with_track(self, create_order_return_data, register_new_courier_and_return_login_password):

        order = create_order_return_data[1]
        courier = register_new_courier_and_return_login_password[3]
        response = requests.put(f'{URL}{order}?courierId={courier}')

        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Проверка принятия заказа без айди')
    @allure.issue('', 'Фактические status_code и text отличны от заявленных в документации')
    def test_take_order_without_order_id(self, register_new_courier_and_return_login_password):

        courier = register_new_courier_and_return_login_password[3]
        response = requests.put(f'{URL}?courierId={courier}')

        assert response.status_code == 400  # BUG: Сервер возвращает 404
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'
        # BUG: Сервер возвращает {"code":404,"message":"Not Found."}

    @allure.title('Проверка принятия заказа без айди курьера')
    def test_take_order_without_courier_id(self, create_order_return_data):

        order = create_order_return_data[1]
        response = requests.put(f'{URL}{order}?courierId=')

        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    @allure.title('Проверка принятия заказа с несуществующим айди')
    def test_take_order_with_non_existing_id(self, register_new_courier_and_return_login_password):

        courier = register_new_courier_and_return_login_password[3]
        response = requests.put(f'{URL}0?courierId={courier}')

        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Заказа с таким id не существует"}'

    @allure.title('Проверка принятия заказа с несуществующим айди курьера')
    def test_take_order_with_non_existing_courier(self, create_order_return_data):

        order = create_order_return_data[1]
        response = requests.put(f'{URL}{order}?courierId=0')

        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Курьера с таким id не существует"}'
