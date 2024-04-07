import requests
import allure


class TestOrderList:

    @allure.title('Проверка получения списка заказов')
    def test_receive_orders_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=30')
        assert response.status_code == 200
