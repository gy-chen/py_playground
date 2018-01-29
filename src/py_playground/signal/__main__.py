import logging
import time
import os
from . import set_exit_handler

logging.basicConfig(level=logging.INFO)
set_exit_handler()

logging.info("Running in pid: %s" % os.getpid())

while True:
    try:
        logging.info('Try to stop me?')
        time.sleep(5)
    except KeyboardInterrupt:
        logging.info('Ignore KeyboardInterrupt')
