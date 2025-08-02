import json
from typing import Dict, Set
from websockets.server import WebSocketServerProtocol

from app.storage.messages import save_message

class RoomManager:
    def __init__(self):
        self.rooms: Dict[str, Set[WebSocketServerProtocol]] = {}

    async def handle_message(self, websocket: WebSocketServerProtocol, message: str):
        """Обработка входящего сообщения и роутинг."""
        try:
            data = json.loads(message)
            action = data.get("action")

            if action == "join":
                await self.join_room(websocket, data["room"])
            elif action == "message":
                await self.broadcast_message(websocket, data["room"], data["text"])
        except json.JSONDecodeError:
            await websocket.send('{"error": "Invalid JSON"}')

    async def join_room(self, websocket: WebSocketServerProtocol, room_name: str):
        """Подключение пользователя к комнате."""
        if room_name not in self.rooms:
            self.rooms[room_name] = set()
        self.rooms[room_name].add(websocket)
        await websocket.send(f'{{"status": "Joined room {room_name}"}}')

    async def broadcast_message(self, sender: WebSocketServerProtocol, room_name: str, text: str):
        """Отправка сообщения всем в комнате."""
        if room_name not in self.rooms:
            await sender.send('{"error": "Room not found"}')
            return

        message = json.dumps({"room": room_name, "text": text})
        await save_message(room_name, text)  # Сохраняем в SQLite
        
        # Рассылка всем, кроме отправителя
        for conn in self.rooms[room_name]:
            if conn != sender:
                await conn.send(message)
