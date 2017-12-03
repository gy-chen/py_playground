import signal
import asyncio
import websockets
from faker import Faker

fake = Faker()


async def word_generator(websocket, path):
    while True:
        await asyncio.sleep(1)
        await websocket.send(fake.word())


async def client(name):
    async with websockets.connect('ws://localhost:4413') as websocket:
        while True:
            word = await websocket.recv()
            print("{} Received {}".format(name, word))


async def server():
    await websockets.serve(word_generator, 'localhost', 4413)


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
