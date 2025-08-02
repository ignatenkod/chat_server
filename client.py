import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        # Вход в комнату
        await websocket.send('{"action": "join", "room": "general"}')
        print(await websocket.recv())  # Ответ сервера

        # Отправка сообщения
        await websocket.send('{"action": "message", "room": "general", "text": "Тестовое сообщение"}')

        # Получение ответов (например, broadcast от других клиентов)
        while True:
            response = await websocket.recv()
            print(f"Получено: {response}")

asyncio.run(chat_client())
