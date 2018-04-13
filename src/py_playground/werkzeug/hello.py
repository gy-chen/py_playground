from werkzeug.wrappers import Request, Response


def application(environ, start_response):
    request = Request(environ)
    text = 'Hello {}!'.format(request.args.get('name', 'World'))
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    with make_server('', 4413, application) as httpd:
        httpd.serve_forever()
