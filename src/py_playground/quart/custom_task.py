import asyncio
from quart import Quart

app = Quart(__name__)


async def custom_hello():
    while True:
        print("Hello from custom hello")
        await asyncio.sleep(5)


@app.route('/')
def hello():
    return 'Hello, Quart'


def create_custom_hello_task():
    # the application will use only one event loop
    # so the task created here will execute when the event loop start to run in other place
    loop = asyncio.get_event_loop()
    return loop.create_task(custom_hello())


if __name__ == '__main__':
    create_custom_hello_task()
    app.run()
