from flask import Flask

app = Flask(__name__)

content = "Hello 一二三"


@app.route('/utf8')
def utf8():
    return content.encode('utf8')


@app.route('/big5')
def big5():
    # try to remove headers and see how it show up in browser
    headers = {
        'Content-Type': 'text/plain; charset=big5'
    }
    return content.encode('big5'), headers


if __name__ == '__main__':
    app.run(debug=True)
