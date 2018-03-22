import asyncio
import os
import sys
from logging import Logger
from pathlib import Path
from ssl import SSLContext
from quart import Quart
from quart.serving import Server
from types import ModuleType
from typing import Dict, List, Optional, Tuple, TYPE_CHECKING, Union, Coroutine  # noqa: F401

app = Quart(__name__)


async def custom_hello():
    while True:
        print("Hello from custom hello")
        await asyncio.sleep(5)


@app.route('/')
def hello():
    return 'Hello, Quart'


async def _observe_changes() -> bool:
    last_updates: Dict[ModuleType, float] = {}
    while True:
        for module in list(sys.modules.values()):
            filename = getattr(module, '__file__', None)
            if filename is None:
                continue
            mtime = Path(filename).stat().st_mtime
            if mtime > last_updates.get(module, mtime):
                return True
            last_updates[module] = mtime
        await asyncio.sleep(1)


def run_app(
        app: 'Quart',
        *custom_tasks: List[Coroutine],
        host: str = '127.0.0.1',
        port: int = 5000,
        access_log_format: str,
        ssl: Optional[SSLContext] = None,
        logger: Optional[Logger] = None,
        timeout: int,
        debug: bool = False,
        use_reloader: bool = False,
) -> None:
    """Create a server to run the app on given the options.

    Arguments:
        app: The Quart app to run.
        host: Hostname e.g. localhost
        port: The port to listen on.
        ssl: Optional SSLContext to use.
        logger: Optional logger for serving (access) logs.
        use_reloader: Automatically reload on changes.
    """
    loop = asyncio.get_event_loop()
    for custom_task in custom_tasks:
        loop.create_task(custom_task)
    loop.set_debug(debug)
    create_server = loop.create_server(
        lambda: Server(app, loop, logger, access_log_format, timeout),
        host, port, ssl=ssl,
    )
    server = loop.run_until_complete(create_server)

    scheme = 'http' if ssl is None else 'https'
    print("Running on {}://{}:{} (CTRL + C to quit)".format(scheme, host, port))  # noqa: T001

    try:
        if use_reloader:
            loop.run_until_complete(_observe_changes())
            server.close()
            loop.run_until_complete(server.wait_closed())
            # Restart this process (only safe for dev/debug)
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            loop.run_forever()
    except KeyboardInterrupt:  # pragma: no cover
        pass
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    run_app(app,
            custom_hello(),
            access_log_format="%(h)s %(r)s %(s)s %(b)s %(D)s",
            timeout=5)
