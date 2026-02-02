import asyncio
import websockets

connected_clients = set()

async def chat_server(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(chat_server, "localhost", 8765)

print("Server started at ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()