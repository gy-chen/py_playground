import asyncio


async def get_http_root(host, port=80):
    connect = asyncio.open_connection(host, port)
    reader, writer = await connect
    content = ('GET / HTTP/1.1\r\n'
               'Host: 127.0.0.1\r\n'
               'Connection: close\r\n\r\n')
    writer.write(content.encode('utf-8'))
    response = await reader.read()
    print(response)
