import requests


class TestOrderTrack:

    def test_order_tracking(self, create_order_return_track):
        track = create_order_return_track
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t={track}')
        assert response.status_code == 200
        assert 'order' in response.text

    def test_order_tracking_without_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=')
        assert response.status_code == 400
        assert response.text == '{"code":400,"message":"Недостаточно данных для поиска"}'

    def test_order_tracking_non_existing_track(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders/track?t=0')
        assert response.status_code == 404
        assert response.text == '{"code":404,"message":"Заказ не найден"}'
