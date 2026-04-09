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

http://localhost:8000/api/docs/

---

### ✅ 2. PostgreSQL

docker ps

Контейнер:
postgres_db

---

### ✅ 3. Redis

docker exec -it redis redis-cli ping

Ответ:
PONG

---

### ✅ 4. Celery worker

docker compose logs celery

Статус:
ready

---

### ✅ 5. Celery Beat

docker compose logs celery-beat

Статус:
Scheduler: Sending due task

---

## 💳 Проверка Stripe оплаты

Тестовая карта:

4242 4242 4242 4242

---

## 📬 Проверка email

Письма отображаются в логах контейнера Django.

---

## 🛑 Остановка проекта

docker compose down

---

# 🚀 Деплой и CI/CD (GitHub Actions)

Проект поддерживает автоматический деплой через GitHub Actions.

## ⚙️ Как работает pipeline

При каждом push в ветку `main`:

1. Запускаются тесты  
2. Если тесты успешны → выполняется деплой  
3. Проект обновляется на сервере через SSH  

---

## 🔐 Настройка SSH доступа

### 1. Генерация ключа (на сервере или локально)

ssh-keygen -t rsa -b 4096

---

### 2. Добавление публичного ключа на сервер

cat ~/.ssh/id_rsa.pub

Добавить в:

~/.ssh/authorized_keys

---

### 3. Настройка прав

chmod 700 ~/.ssh  
chmod 600 ~/.ssh/authorized_keys  

---

## 🔑 GitHub Secrets

В репозитории:

Settings → Secrets and variables → Actions

Добавить:

- SERVER_HOST → IP сервера  
- SERVER_USER → пользователь (deploy)  
- SERVER_SSH_KEY → приватный SSH ключ  

Приватный ключ:

cat ~/.ssh/id_rsa

---

## ⚙️ GitHub Actions Workflow

Файл:

.github/workflows/deploy.yml

Workflow:

- устанавливает зависимости  
- запускает тесты  
- при успехе подключается к серверу  
- выполняет git pull  
- устанавливает зависимости  
- применяет миграции  
- перезапускает сервис  

---

## 🚀 Запуск деплоя

git add .  
git commit -m "setup CI/CD"  
git push origin main  

После push:

- автоматически запускается pipeline  
- при успешных тестах происходит деплой  

---

## ⚠️ Возможные проблемы

- SSH ключ не добавлен  
- неверные GitHub Secrets  
- не установлен Docker / зависимости  
- не настроен сервер  
- ошибки в .env  
- сервисы не запущены  

---

## 🎯 Итог

Проект поддерживает:

- Docker окружение  
- PostgreSQL + Redis  
- Celery + Celery Beat  
- Stripe платежи  
- CI/CD через GitHub Actions  
- Автоматический деплой на сервер  