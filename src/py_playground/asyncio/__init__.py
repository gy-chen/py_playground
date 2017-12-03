import asyncio


async def say(what, count):
    for _ in range(count):
        print(what)
        await asyncio.sleep(1)


def run_simple():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(say('Hello asyncio', 10))
    loop.run_until_complete(say('Hello Monshin', 10))
    loop.close()


def run_tasks():
    loop = asyncio.get_event_loop()
    loop.create_task(say('Hello asyncio', 10))
    loop.create_task(say('Hello Monshin', 10))
    loop.run_forever()
    loop.close()


def run_gather():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        say('Hello asyncio', 10),
        say('Hello Monshin', 10)
    ))
    loop.close()


if __name__ == '__main__':
    # run_simple()
    # run_tasks()
    run_gather()
