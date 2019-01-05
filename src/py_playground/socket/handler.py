import queue
import logging

logging.basicConfig(level=logging.DEBUG)


class ConnectionHandler:
    """handle connection

    continues read from connection, and put result in output_queue.
    continues read from input_queue, and send it to conn.
    """

    def __init__(self, conn, input_queue=None, output_queue=None):
        self._conn = conn
        self.input_queue = input_queue or queue.Queue()
        self.output_queue = output_queue or queue.Queue()
        self._broken = False

    def close(self):
        self._conn.close()

    def is_broken(self):
        return self._broken

    def handle_input(self):
        while not self._broken:
            data = self._conn.recv(4096)
            if not data:
                self._broken = True
                self._conn.close()
                break
            self.output_queue.put(data)
        logging.debug('end of handling input')

    def handle_output(self):
        while not self._broken:
            try:
                data = self.input_queue.get(timeout=5)
            except queue.Empty:
                logging.debug('waiting for input')
                continue
            self._conn.sendall(data)
        logging.debug('end of handding output')
