import os
import binascii
from werkzeug.wrappers import Request, Response
from werkzeug.local import Local, LocalManager

local = Local()
local_manager = LocalManager([local])


def application(environ, start_response):
    new = os.urandom(5)
    previous = getattr(local, 'monshin', None)
    text = "previous: {}\nnew: {}".format(binascii.hexlify(previous) if previous else None, binascii.hexlify(new))
    local.monshin = new
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    with make_server('', 4413, application) as httpd:
        httpd.serve_forever()
