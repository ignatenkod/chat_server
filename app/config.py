import os

PORT = int(os.getenv("CHAT_PORT", "8000"))
DB_NAME = os.getenv("DB_NAME", "chat.db")
