import websockets
import asyncio

async def server(message):
    async with websockets.connect('ws://localhost:5090') as mitm:
        await mitm.send(message)

asyncio.run(server("Hi this is Alice!"))
