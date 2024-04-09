import requests
import allure


URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders/track'


class TestOrderTrack:

    @allure.title('Проверка получения заказа по трек-номеру')
    def test_order_tracking(self, create_order_return_data):

        track = create_order_return_data[0]
        response = requests.get(f'{URL}?t={track}')

        assert response.status_code == 200
        assert 'order' in response.text

    @allure.title('Проверка получения заказа по запросу без трек-номера')
    def test_order_tracking_without_track(self):

        response = requests.get(f'{URL}?t=')

        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    @allure.title('Проверка получения заказа с несуществующим трек-номером')
    def test_order_tracking_non_existing_track(self):

        response = requests.get(f'{URL}?t=0')

        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Заказ не найден"}'
