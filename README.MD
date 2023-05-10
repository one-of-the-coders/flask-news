# НОВОСТНОЙ ПОРТАЛ
Новостной сайт, где КАЖДЫЙ может разместить свою выдуманную новость

# Описание
Новостной сайт создан с учебной целью

## Технологии
* Python
* Flask
* WTForms
* SQLAlchemy

# Как запустить
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venv/Scripts/sctivate
```
3. Установите зависимости
```commandline
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SECRET_KEY
```
5. Запустите flask приложение
```commandline
flask run
```