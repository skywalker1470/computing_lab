import asyncio
import websockets

async def bob_server(websocket):
    message = await websocket.recv()
    print(f"The message is : {message}")

async def main():
    async with websockets.serve(bob_server , 'localhost' , 5091):
        print("Waiting for the message....")
        await asyncio.Future()

asyncio.run(main())