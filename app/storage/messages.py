import aiosqlite
from datetime import datetime

DB_NAME = "chat.db"

async def init_db():
    """Инициализация БД."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "CREATE TABLE IF NOT EXISTS messages "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "room TEXT, text TEXT, timestamp DATETIME)"
        )
        await db.commit()

async def save_message(room: str, text: str):
    """Сохранение сообщения в SQLite."""
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "INSERT INTO messages (room, text, timestamp) VALUES (?, ?, ?)",
            (room, text, datetime.now().isoformat()),
        )
        await db.commit()
