import asyncio
import websockets

async def mitm(websocket):
    msg = await websocket.recv()
    tamp = msg.replace("Alice" , "Adam")
    print("Original Message is tampered")
    async with websockets.connect("ws://localhost:5091") as mitm_sender:
        await mitm_sender.send(tamp)
        print("Message sent")

async def main():
    async with websockets.serve(mitm,'localhost',5090):
        print("Waiting to intercept....")
        await asyncio.Future()

asyncio.run(main())