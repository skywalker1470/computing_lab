import asyncio
import websockets

async def client(message,tampered):
    async with websockets.connect("ws://localhost:5090") as websocket:
        if tampered:
            await websocket.send("NO")
        else:
            await websocket.send(message)

asyncio.run(client("yes",False))
asyncio.run(client("yes",True))
