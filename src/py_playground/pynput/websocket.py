import asyncio
import websockets
from queue import Empty
from . import pressed_chars
from ..asyncio.websocket import client

connected = set()

async def key_generator(websocket, path):
    connected.add(websocket)
    while True:
        try:
            key = pressed_chars.get(block=False)
            print('send {}'.format(key))
            for ws in connected:
                await ws.send(str(key))
        except Empty:
            pass
        except:
            connected.remove(websocket)
        finally:
            await asyncio.sleep(1)


async def server():
    await websockets.serve(key_generator, 'localhost', 4413)


def start():
    from . import get_keyboard_listener
    keyboard_listener = get_keyboard_listener()
    keyboard_listener.start()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        server(),
        client('Client 1'),
        client('Cleint 2')
    ))
    loop.close()

if __name__ == '__main__':
    start()