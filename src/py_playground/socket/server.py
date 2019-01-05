import logging
import socket
import threading
import queue
import sys
from .handler import ConnectionHandler

logging.basicConfig(level=logging.DEBUG)


def handle(connection_handler):
    logging.debug('handle connection')
    # mimic interactive shell, except one input and then one output
    while not connection_handler.is_broken():
        sys.stdout.write(">>> ")
        sys.stdout.flush()
        cmd = sys.stdin.readline()[:-1]
        connection_handler.input_queue.put(cmd.encode('utf8'))
        try:
            res = connection_handler.output_queue.get(timeout=5)
        except queue.Empty:
            continue
        sys.stdout.write(res.decode('utf8'))
        sys.stdout.write("\n")
        sys.stdout.flush()
    logging.debug('end of handling connection')


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 4413))
    s.listen(5)

    conn, addr = s.accept()
    logging.debug('accept connection from {}'.format(addr))
    handler = ConnectionHandler(conn)
    threading.Thread(target=handler.handle_input).start()
    threading.Thread(target=handler.handle_output).start()
    try:
        handle(handler)
    except KeyboardInterrupt:
        pass
    finally:
        logging.debug('exit main program')
        sys.exit()


if __name__ == '__main__':
    serve()
