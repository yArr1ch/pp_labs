
# PP lab4

-Створено репозиторій та склоновано його

-Встановлено конкретну версію Python 3.8.* за допомогою утиліти pyenv

-Створене віртуальне середовище за допомогою virtualenv

-Додано Flask у файл requirements.txt

-Реалізовано адресу api/v1/hello-world-2, яка відповідає текстом Hello World 2

-Запущено проект через WSGI сервер gunicorn


Для створення віртуального середовища, було використано: virtualenv
$ python -m pip install virtualenv

Налаштовано та активовано за допомогою:
$ python -m virtualenv venv

Встановлено залежності:
$ pip install -r requirements.txt

Запускаємо проект через gunicorn:
gunicorn main:app
127.0.0.1:8000/api/v1/hello-world-2