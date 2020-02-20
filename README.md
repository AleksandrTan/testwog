#Приложение для тестирования REST API.

##Стек:
1. Python  - 3.7.2

2. Django 3.0.3

3. DataBase - Sqlite

##Структура приложения(testwogs):
 
1. settings.py - файл настроек

2. 

##Порядок работы:
Приложение для тестирования API запускается через консоль Django с использованием manage.py

Команда - _**manage.py runtest <аргумент>**_

Аргументы команды:

1. _**manage.py runtest help**_ - выводит список аргументов для команды и их описание

2. _**manage.py runtest showtests**_ - список всех тестов

3. **_manage.py runtest <test_name>_** - запускае указанный тест

4. _**manage.py runtest runall**_ - запускает все зарегистрированные тесты