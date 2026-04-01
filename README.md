# LMS Project (Django + DRF + Celery + Stripe + Docker)

## 🚀 Запуск проекта через Docker

### 1. Установить Docker

Установите Docker Desktop:  
https://www.docker.com/products/docker-desktop/

---

### 2. Клонировать репозиторий

git clone <repo_url>  
cd Documentation_and_Security

---

### 3. Создать файл .env

Создайте файл `.env` в корне проекта:

SECRET_KEY=
DEBUG=  

STRIPE_SECRET_KEY= 

REDIS_HOST=
REDIS_PORT=

DB_NAME=  
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

---

### 4. Запуск проекта

docker compose up --build

После запуска будут подняты:

- Django (web)
- PostgreSQL (db)
- Redis
- Celery worker
- Celery Beat

---

## 📌 Проверка работоспособности сервисов

### ✅ 1. Django (API + документация)

Открыть в браузере:

http://localhost:8000/api/docs/

Если Swagger открылся → сервис работает

---

### ✅ 2. PostgreSQL

Проверить контейнер:

docker ps

Должен быть контейнер:
postgres_db

---

### ✅ 3. Redis

Проверка:

docker exec -it redis redis-cli ping

Ожидаемый ответ:
PONG

---

### ✅ 4. Celery worker

Логи:

docker compose logs celery

Должно быть:
ready

Это означает, что воркер обрабатывает задачи

---

### ✅ 5. Celery Beat

docker compose logs celery-beat

Должно быть:
Scheduler: Sending due task

Это означает, что периодические задачи работают

---

## 💳 Проверка Stripe оплаты

Используйте тестовую карту:

4242 4242 4242 4242

---

## 📬 Проверка email

Письма отправляются через console backend и отображаются в логах контейнера Django.

---

## 🛑 Остановка проекта

docker compose down