import socket
import sys
import select
import logging


def handle(conn):
    conn.setblocking(False)
    inputs = [conn, sys.stdin]
    outputs = [conn]
    sys.stdout.write(">>> ")
    sys.stdout.flush()
    while True:
        readable, writeable, exp = select.select(inputs, outputs, inputs)

        if conn in readable:
            data = conn.recv(4096)
            if not data:
                break
            sys.stdout.write(data.decode('utf8'))
            sys.stdout.write('\n')
            sys.stdout.flush()

        if conn in writeable and sys.stdin in readable:
            cmd = sys.stdin.readline()[:-1]
            conn.sendall(cmd.encode('utf8'))
            sys.stdout.write(">>> ")
            sys.stdout.flush()

        if conn in exp:
            break


def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 4413))
    s.listen(1)

    conn, _ = s.accept()
    try:
        handle(conn)
    except KeyboardInterrupt:
        pass
    finally:
        conn.close()
        s.close()


if __name__ == '__main__':
    serve()
