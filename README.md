# Online store DJANGO

Учебный проект на Django — сайт с главной страницей и страницей контактов.

## Технологии
- Python 3.12
- Django 6.1.1
- Bootstrap 5

## Установка и запуск
```bash
python -m venv venv
venv\Scripts\activate
pip install poetry
poetry install
python manage.py runserver
```

## Структура проекта
- `catalog/` — приложение с контроллерами и маршрутами
- `templates/` — HTML шаблоны
- `config/` — настройки проекта

## Ветки (GitFlow)
- `main` — стабильный код
- `develop` — разработка
- `future/homework_XX` — ветки для каждого задания
