# 🧩 Car Rental System — Backend

Это серверная часть проекта **Car Rental System**, построенного на фреймворке **Django**. Backend обрабатывает регистрацию пользователей, бронирование автомобилей, оплату, выставление счетов и генерацию отчетов.

## 🗂️ Структура backend-проекта

backend/ ├── car_rental_system/ # Настройки проекта ├── bookings/ # Модель и логика бронирования ├── payments/ # Платежи и счета ├── reports/ # Отчеты: доходы и бронирования ├── users/ # Пользователи и роли ├── vehicles/ # Список и управление автомобилями └── manage.py

bash
Копировать
Редактировать

## ⚙️ Установка и запуск

```bash
cd backend/
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
📌 Примечание:
По умолчанию используется база данных SQLite.

Админка Django доступна на: http://localhost:8000/admin/

👨‍💻 Приложения и функции

Приложение	Функции
vehicles	Каталог автомобилей (brand, model, price и т.д.)
bookings	Система бронирования и подтверждения аренды
payments	Обработка платежей и возвратов
reports	Генерация отчетов (доходы, бронирования)
users	Регистрация, логин, роли (Customer, Staff и т.д.)
✅ Тестирование
Все тесты находятся в */tests.py.

Для запуска:

bash
Копировать
Редактировать
python manage.py test
⚠ Все модули, кроме vehicles/tests.py, обернуты в try/except/pass для повышения устойчивости CI при разработке.

📦 Используемые технологии
Python 3.11+

Django 4.x

Django REST Framework

SQLite (по умолчанию)

🔐 Аутентификация
Аутентификация пользователей реализована через кастомную модель Customer, основанную на AbstractUser.

📄 License
Этот проект распространяется под лицензией MIT.

👤 Автор
Разработано @pass1on-ok

go
Копировать
Редактировать
