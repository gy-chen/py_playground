#coding: utf-8
from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = ['{}: {}\n'.format(k, v) for k, v in environ.items()]
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(sum([len(s) for s in response_body])))
    ]
    start_response(status, response_headers)
    return response_body

def start_simple_wsgi():
    httpd = make_server(
        '127.0.0.1',
        4413,
        application
    )

    httpd.handle_request()

if __name__ == '__main__':
    start_simple_wsgi()
