import queue


class ConnectionHandler:
    """handle connection

    continues read from connection, and put result in output_queue.
    continues read from input_queue, and send it to conn.
    """

    def __init__(self, conn, input_queue=None, output_queue=None):
        self._conn = conn
        self._input_queue = input_queue or queue.Queue()
        self._output_queue = output_queue or queue.Queue()
        self._broken = False

    def is_broken(self):
        return self._broken

    def handle_input(self):
        while True:
            data = self._conn.recv(4096)
            if not data:
                self._broken
                break
            self._output_queue.put(data)

    def handle_output(self):
        while True:
            data = self._input_queue.get()
            self._conn.sendall(data)
