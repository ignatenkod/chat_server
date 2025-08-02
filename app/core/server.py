import asyncio
import logging
from typing import Dict, Set
from websockets.server import WebSocketServerProtocol, serve

from app.config import PORT
from app.rooms.manager import RoomManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatServer:
    def __init__(self):
        self.active_connections: Set[WebSocketServerProtocol] = set()
        self.room_manager = RoomManager()

    async def handle_connection(self, websocket: WebSocketServerProtocol):
        """Обработка нового подключения."""
        self.active_connections.add(websocket)
        logger.info(f"Новое подключение: {websocket.remote_address}")
        
        try:
            async for message in websocket:
                message = await logging_middleware(websocket, message)
                await self.room_manager.handle_message(websocket, message)
        except Exception as e:
            logger.error(f"Ошибка: {e}")
        finally:
            self.active_connections.remove(websocket)
            logger.info(f"Отключение: {websocket.remote_address}")

    async def run(self):
        """Запуск сервера."""
        async with serve(self.handle_connection, "0.0.0.0", PORT):
            logger.info(f"Сервер запущен на ws://0.0.0.0:{PORT}")
            await asyncio.Future()  # Бесконечный цикл

if __name__ == "__main__":
    server = ChatServer()
    asyncio.run(server.run())
