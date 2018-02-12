import signal
import asyncio
import websockets
from faker import Faker

fake = Faker()

connected = set()


async def word_generator(websocket, path):
    while True:
        await asyncio.sleep(1)
        await websocket.send(fake.word())


async def client(name):
    async with websockets.connect('ws://localhost:4413') as websocket:
        while True:
            word = await websocket.recv()
            print("{} Received {}".format(name, word))


async def hello_on_someone_connected(websocket, path):
    connected.add(websocket)

    async def send_hello(ws):
        try:
            await ws.send("Hello!")
        except websockets.ConnectionClosed:
            pass

    await asyncio.wait([send_hello(ws) for ws in connected])

    while True:
        try:
            pong_waiter = await websocket.ping()
            await asyncio.wait_for(pong_waiter, timeout=1)
        except (asyncio.TimeoutError, websockets.ConnectionClosed):
            connected.remove(websocket)
            break


async def server():
    await websockets.serve(hello_on_someone_connected, 'localhost', 4413)


def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        server(),
        client("client 1"),
        client("client 2")
    ))
    loop.close()


if __name__ == '__main__':
    start()
