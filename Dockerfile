# Используем минимальный образ Python на Alpine
FROM python:3.10-alpine

# Устанавливаем зависимости для aiosqlite (SQLite3 в Alpine)
RUN apk add --no-cache sqlite

# Копируем код и зависимости
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Запускаем сервер
CMD ["python", "-m", "app.core.server"]
