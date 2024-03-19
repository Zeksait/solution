# solution
Реализация тестового задания для Элвис

1) переименовать env в .env и заменить параметры своими
2) создать папку postgres-db: mkdir postgres-db
3) сбилдить контейнеры и запустить: docker compose build && docker compose up -d
4) Создать таблицу: docker compose exec flask python manage.py create_db
5) Заполнить таблицу данными: docker compose exec flask python manage.py create_data
6) проверить в браузере: http://localhost:5000/

Зайти в шелл: docker compose exec flask python manage.py shell
Посмотреть логи фласк в реальном времени: docker compose logs -f flask
