import time
from concurrent.futures import ThreadPoolExecutor

SAY_TIMES = 10
DELAY = 3


def say_time(delay):
    time.sleep(delay)
    print("Hi!", time.time())


def no_concurrent(times=SAY_TIMES, delay=DELAY):
    for _ in range(times):
        say_time(delay)


def concurrent(times=SAY_TIMES, delay=DELAY):
    executor = ThreadPoolExecutor()
    for _ in range(times):
        executor.submit(say_time, delay)


if __name__ == '__main__':
    # no_concurrent()
    concurrent()
