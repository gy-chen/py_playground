import time
import logging
from . import Greeter
from ..signal import set_exit_handler

logging.basicConfig(level=logging.DEBUG)
set_exit_handler()

actor = Greeter.start()

while True:
    actor.ask({'msg': 'Hi?'})
    time.sleep(3)
