Итоговый проект по автоматизированному тестированию функционала страницы https://b2c.passport.rt.ru сайта "Ростелеком"
При тестировании сайта были написаны:
ручные чек-лист и тест-кейсы;
баг-репорты;
автоматизированные тесты (настроены на запуск через Run).
При тестировании сайта были применены следующие техники тест-дизайна:
разбиение на классы эквивалентности;
анализ граничных значений;
тестирование состояний и переходов.
И в позитивных, и в негативных тестах для страницы восстановления пароля необходимо вручную вводить символы с картинки.

Папка pages содержит следующие файлы:
api_reg_email.py - GET-запросы к виртуальному почтовому ящику (1secmail.com) для получения валидного email и кода для регистрации на сайте и восстановления пароля;
auth.py - функции-обертки для локаторов, распределенные по классам в зависимости от тематики тестов;
base.py - функции для применения к локаторам явных ожиданий, получения главной страницы сайта и пути текущей страницы;
config.py - основной URL тестируемого сайта;
locators.py - XPath- и CSS-локаторы web-элементов сайта;
settings.py - учетные данные, используемые в процессе теста.
Папка tests содержит следующие файлы:
test_negative_auth_page - негативные тесты страницы авторизации;
test_negative_reg_page - негативные тесты страницы регистрации;
test_negative_new_password_page - негативные тесты страницы восстановления пароля;
test_positive_auth_page - позитивные тесты страницы авторизации;
test_positive_reg_page - позитивные тесты страницы регистрации;
test_positive_new_password_page - позитивные тесты страницы восстановления пароля.
Также проект содержит такие файлы, как:
conftest.py - фикстура для работы с браузером;
pytest.ini - маркеры для параметризации;
requirements.txt - используемые при тестировании библиотеки PyCharm.
