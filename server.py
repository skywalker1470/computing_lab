import asyncio
import websockets

async def server(websocket):
    message = await websocket.recv()
    if(message == "yes"):
        print(f"The message is not tampered: {message}")
    else:
        print(f"The message is tampered: {message}")

async def main():
    async with websockets.serve(server,"localhost",5090):
        print("Waiting for messages")
        await asyncio.Future()

asyncio.run(main())