import requests
import allure


class TestOrderTake:

    @allure.title('Проверка принятия существующего заказа существующим курьером')
    def test_take_order_with_track(self, create_order_return_id, create_and_login_courier_return_id):
        order = create_order_return_id
        courier = create_and_login_courier_return_id
        response = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order}?courierId={courier}')
        assert response.status_code == 200
        assert response.text == '{"ok":true}'

    @allure.title('Проверка принятия заказа без айди')
    def test_take_order_without_order_id(self,create_and_login_courier_return_id):
        courier = create_and_login_courier_return_id
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/?courierId={courier}')
        assert response.status_code == 404  # В документации указана 400, но сервер возвращает 404
        assert response.text == '{"code":404,"message":"Not Found."}'

    @allure.title('Проверка принятия заказа без айди курьера')
    def test_take_order_without_courier_id(self, create_order_return_id):
        order = create_order_return_id
        response = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order}?courierId=')
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    @allure.title('Проверка принятия заказа с несуществующим айди')
    def test_take_order_with_non_existing_id(self, create_and_login_courier_return_id):
        courier = create_and_login_courier_return_id
        response = requests.put(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/0?courierId={courier}')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Заказа с таким id не существует"}'

    @allure.title('Проверка принятия заказа с несуществующим айди курьера')
    def test_take_order_with_non_existing_courier(self, create_order_return_id):
        order = create_order_return_id
        response = requests.put(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/{order}?courierId=0')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Курьера с таким id не существует"}'
