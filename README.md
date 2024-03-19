# solution
Реализация тестового задания для Элвис

1) в файле env заменить параметры своими
2) переименовать env в .env: mv env .env
3) создать папку postgres-db: mkdir postgres-db
4) сбилдить контейнеры и запустить: docker compose build && docker compose up -d
5) Создать таблицу: docker compose exec flask python manage.py create_db
6) Заполнить таблицу данными: docker compose exec flask python manage.py create_data
7) проверить в браузере: http://localhost:5000/

Зайти в шелл: docker compose exec flask python manage.py shell
Посмотреть логи фласк в реальном времени: docker compose logs -f flask
