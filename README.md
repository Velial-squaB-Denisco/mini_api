# Tasks API

Мини-API для учёта задач.

## Установка и запуск
Все команды выполняются из корня проекта.

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
python3 seed_statuses.py
uvicorn app.main:app --reload
```
Для запуска тестов:
```bash
pytest
```
Для запуска в Docker:
```bash
docker build -t mini_api .
docker run -p 8000:8000 mini_api
```
Если нужны примеры API то они есть в Swagger по адресу http://127.0.0.1:8000/#docs

PS: Я понимаю что нужно добавить в gitignore БД, но я не стал этого делать, чтобы было проще проверить работу API. А так в идеале нужно добавить скрипт заполнения таблицы status (ну или вообще отказаться от неё так как в тз её не было, но добавив её можно выйграть на том чтобы не писать дополнительные проверки и так проще для масштабирования статусов).