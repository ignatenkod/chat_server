# 🚀 Async WebSocket Chat Server

**Легковесный чат-сервер на Python с использованием asyncio и WebSockets**  
Без лишних зависимостей — только асинхронность, комнаты и SQLite для истории.

---

## 🔥 Фичи

- **WebSocket-сервер** на `asyncio` + `websockets`
- **Комнаты** с broadcast-рассылкой сообщений
- **Сохранение истории** в SQLite через `aiosqlite`
- **Кастомные middleware** (логирование, аутентификация)
- **Alpine Docker-образ** (<50MB)
- Своя система роутинга сообщений (JSON-based)

---

## 🛠 Установк

### Локальный запуск
```bash
git clone https://github.com/ваш-репозиторий.git
cd chat-server
pip install -r requirements.txt
python -m app.core.server
```

### Docker
```bash
docker build -t chat-server .
docker run -p 8000:8000 chat-server
```

---

## 📡 API-формат сообщений

**Вход в комнату:**
```json
{"action": "join", "room": "general"}
```

**Отправка сообщения:**
```json
{"action": "message", "room": "general", "text": "Привет!"}
```

---

## 🧪 Тестирование

1. **Через `websocat`**:
   ```bash
   websocat ws://localhost:8000
   ```

2. **Python-клиент**:
   ```python
   import asyncio, websockets
   async def test_client():
       async with websockets.connect("ws://localhost:8000") as ws:
           await ws.send('{"action": "join", "room": "test"}')
           await ws.send('{"action": "message", "room": "test", "text": "Hi"}')
   asyncio.run(test_client())
   ```

---

## 📁 Структура проекта

```
chat-server/
├── app/
│   ├── core/          # Ядро сервера
│   ├── rooms/         # Логика комнат
│   ├── storage/       # SQLite-интеграция
│   └── config.py      # Настройки
├── Dockerfile         # Alpine-образ
└── requirements.txt   # Зависимости
```

---

## 💡 Примеры использования

### 1. Групповой чат
- Создайте комнату `game-lobby` и пригласите друзей.

### 2. Логирование событий
- Все сообщения сохраняются в БД:
  ```bash
  sqlite3 chat.db "SELECT * FROM messages;"
  ```

---

## 🚀 Дорожная карта

- [ ] Добавить JWT-аутентификацию
- [ ] Поддержка приватных комнат
- [ ] REST API для истории чата
- [ ] Статистика активности

---

## 📜 Лицензия

MIT — свободное использование с указанием авторства.

---

> **Автор**: Диана 
> **Версия**: 1.0.0  
> **Технологии**: Python 3.10+, asyncio, WebSockets, SQLite
```
