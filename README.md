# solution
Реализация тестового задания для Элвис

### Инструкция

1) перейти в папку: 
    ```sh
    cd solution
    ```
1) в файле env заменить параметры своими:
    ```sh
    nano env
    ```
2) переименовать env в .env:
    ```sh
    mv env .env
    ```
3) создать папку postgres-db:
    ```sh
    mkdir postgres-db
    ```
4) сбилдить контейнеры и запустить:
    ```sh
    docker compose build && docker compose up -d
    ```
5) Создать таблицу:
    ```sh
    docker compose exec flask python manage.py create_db
    ```
6) Заполнить таблицу данными:
    ```sh
    docker compose exec flask python manage.py create_data
    ```
7) проверить в браузере: http://localhost:5000/


### Заметки

Зайти в шелл flask:
    ```sh
    docker compose exec flask python manage.py shell
    ```
Посмотреть логи фласк в реальном времени:
    ```sh
    docker compose logs -f flask
    ```
Опустить контейнеры:
    ```sh
    docker compose down
    ```