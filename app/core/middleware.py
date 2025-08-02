from websockets.server import WebSocketServerProtocol

async def logging_middleware(websocket: WebSocketServerProtocol, message: str):
    """Логирование входящих сообщений."""
    print(f"Получено сообщение от {websocket.remote_address}: {message}")
    return message
