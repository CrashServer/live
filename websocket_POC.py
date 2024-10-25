import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, Server!"
        await websocket.send(message)
        print(f">>> Sent: {message}")

        response = await websocket.recv()
        print(f"<<< Received: {response}")

asyncio.run(send_message())