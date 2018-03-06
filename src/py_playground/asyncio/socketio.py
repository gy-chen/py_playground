import os
import socketio
from aiohttp import web

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)


async def index(request):
    return web.HTTPFound('./static/index.html')


@sio.on('binary')
async def binary(sid, data):
    print("received", data)
    await sio.emit('binary', os.urandom(32))


app.router.add_static('/static', os.path.join(os.path.dirname(__file__), 'socketio'))
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app, port=8000)
