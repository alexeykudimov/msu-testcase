## MSU TESTCASE
## Стек:
* Python 3.9
* Django 3.2
* DRF
* Postgres
## Функционал:
* Регистрация пользователя
* Авторизация пользователя
* Добавление новой задачи
* Изменение/удаление задачи (только для создателя задачи)
* Список задач
* Список задач, созданных текущим пользователем
## Запуск
#### 1) Установить Docker на компьютер
#### 2) Клонировать этот репозиторий
#### 3) В корне создать файл .env.dev
    DEBUG=1
    SECRET_KEY=156eca1c3da67b3951edc0bf0728fd52
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    
    #db
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_DB=msu_test
    POSTGRES_USER=msu_test_user
    POSTGRES_PASSWORD=msu_test_pass
    POSTGRES_HOST=msu_test_db
    POSTGRES_PORT=5432
    DATABASE=postgres
   
#### 4) Собрать и запустить контейнер
    docker-compose up --build
#### 5) Перейти по адресу
    http://127.0.0.1:8000/api/swagger/

