# Sprint_7
Final project of seventh sprint on "Python QA automation" course
Structure:
Sprint_7/
├-tests
│  ├-couriers - Наборы проверок, связанных с курьерами
│  │  ├-test_courier_create.py - Проверки создания курьера в системе
│  │  ├-test_courier_delete.py - Проверки удаления курьера из системы
│  │  └-test_courier_login.py - Проверка входа курьера в систему
│  └-orders - Наборы проверок, связанных с заказами
│     ├-test_order_create.py - Проверки создания заказа
│     ├-test_order_list.py - Проверка получения списка заказов
│     ├-test_order_take.py - Проверки взятия заказов в работу
│     └-test_order_track.py - Проверки отслеживания заказа
├-allure_results - Отчёты о тестах
├-conftest.py - Фикстуры
├-data.py - Набор данных для создания заказа
├-README.md - Этот файл
└-requirements.txt - Внешние зависимости
