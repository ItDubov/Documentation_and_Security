# LMS Project (Django + DRF + Celery + Stripe + Docker)

## 🚀 Локальный запуск проекта через Docker

### 1. Установка Docker

Установите Docker Desktop:  
https://www.docker.com/products/docker-desktop/

---

### 2. Клонирование репозитория

```bash
git clone <repo_url>
cd Documentation_and_Security
3. Создание файла .env

Создайте файл .env в корне проекта:

SECRET_KEY=your_secret_key
DEBUG=True

STRIPE_SECRET_KEY=sk_test_xxx

REDIS_HOST=redis
REDIS_PORT=6379

DB_NAME=lms_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
4. Запуск проекта
docker compose up --build
📦 Поднимаемые сервисы

После запуска автоматически стартуют:

Django (gunicorn)
PostgreSQL
Redis
Celery worker
Celery Beat
nginx (reverse proxy)
🌐 Проверка работоспособности
✅ API и документация

Открыть в браузере:

http://localhost/api/docs/
✅ Проверка контейнеров
docker ps

Должны отображаться:

django_app
postgres_db
redis
celery
celery-beat
nginx
✅ Проверка Redis
docker exec -it redis redis-cli ping

Ожидаемый ответ:

PONG
✅ Проверка Celery
docker compose logs celery

Ожидаемый статус:

ready
✅ Проверка Celery Beat
docker compose logs celery-beat

Ожидаемый статус:

Scheduler: Sending due task
💳 Проверка Stripe

Тестовая карта:

4242 4242 4242 4242
📬 Проверка email

Отправленные письма отображаются в логах контейнера Django.

🛑 Остановка проекта
docker compose down
🚀 Деплой проекта на сервер (Yandex Cloud)
📌 Приложение доступно по адресу:
http://<SERVER_IP>
⚙️ Ручной деплой
1. Подключение к серверу
ssh ubuntu@SERVER_IP
2. Установка Docker
sudo apt update
sudo apt install docker.io -y
sudo apt install docker-compose -y
3. Клонирование проекта
git clone <repo_url>
cd Documentation_and_Security
4. Создание .env

Создать файл .env аналогично локальной настройке.

5. Запуск проекта
docker compose up -d --build
✅ Проверка работы

Открыть в браузере:

http://SERVER_IP
🔄 CI/CD (GitHub Actions)
⚙️ Что делает pipeline

При каждом push в ветку develop:

Запускается линтинг (flake8)
Выполняются тесты Django
Проверяется сборка Docker
Выполняется автоматический деплой на сервер
🔐 GitHub Secrets

В репозитории необходимо добавить:

SERVER_IP — IP сервера
SERVER_USER — пользователь (обычно ubuntu)
SSH_KEY — приватный SSH ключ
🚀 Запуск деплоя
git add .
git commit -m "deploy"
git push origin develop

После этого:

автоматически запускается CI/CD pipeline
при успешном выполнении происходит деплой на сервер
⚠️ Возможные проблемы
Docker не установлен
Порт 80 закрыт на сервере
Неверно настроен .env
Используется localhost вместо db/redis
Не настроены GitHub Secrets
Контейнеры не запущены
🎯 Итог

Проект реализует:

Django + DRF API
Автогенерацию документации (drf-spectacular)
Stripe платежи
Celery + Celery Beat
PostgreSQL + Redis
Docker + nginx
CI/CD через GitHub Actions
Автоматический деплой на сервер