# Базовый образ: лёгкий Python 3.11 на Alpine Linux
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем список зависимостей
COPY requirements.txt .

# Устанавливаем зависимости (--no-cache-dir уменьшает размер образа)
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY app.py .

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Команда запуска приложения при старте контейнера
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
