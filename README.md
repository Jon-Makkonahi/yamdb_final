# Учебный проект "YaMDb API" ![example workflow](https://github.com/Jon-Makkonahi/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Проект YaMDb позволяет добавлять новых пользователей,
собирает отзывы пользователей на различные произведения.

### Авторы:
- Daniil Bibikov (Jon-Makkonahi) https://github.com/Jon-Makkonahi

### Технологии:
- Python
- Django
- DRF

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:Jon-Makkonahi/yamdb_final.git
cd api_yambd
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Если необходимо, заполненить базу данных тестовыми данными:

1. перейдите в корневую папку проекта, где находится файл csv_importer.py
2. запустите скрипт csv_importer.py:
```
python3 csv_importer.py
```

Запустить проект:

```bash
python3 manage.py runserver
```

## Документация к API:

```
http://127.0.0.1:8000/redoc/
```

Регистрация нового пользователя:

```
http://127.0.0.1:8000/api/v1/auth/signup/
```
## Запуск Docker:
Запустите docker-compose командой 

```bash
sudo docker-compose up -d --build
```
У вас развернётся проект, запущенный через Gunicorn с базой данных Postgres.
Выполнить миграции, создать суперпользователя и заполнить БД данными, а также собрать статику.

```bash
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py csv_importer.py
sudo docker-compose exec web python manage.py collectstatic --no-input
```
Остановка контейнеров и их удаление вместе со всеми зависимостями
```bash
sudo docker-compose down -v
```
