import requests
import allure


class TestOrderTrack:

    @allure.title('Проверка получения заказа по трек-номеру')
    def test_order_tracking(self, create_order_return_track):
        track = create_order_return_track
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
        assert response.status_code == 200
        assert 'order' in response.text

    @allure.title('Проверка получения заказа по запросу без трек-номера')
    def test_order_tracking_without_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=')
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    @allure.title('Проверка получения заказа с несуществующим трек-номером')
    def test_order_tracking_non_existing_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=0')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Заказ не найден"}'
