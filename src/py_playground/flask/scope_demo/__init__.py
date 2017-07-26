from flask import Flask
from . import secretvaluer

app = Flask(__name__)
app.debug = True
app.threaded = True

@app.route('/')
def index():
    message = "Hello: {:04d}".format(secretvaluer.singleton.get_secret_value())
    secretvaluer.singleton.generate_secret_value()
    message += "Hello: {:04d}".format(secretvaluer.singleton.get_secret_value())
    return message

def run():
    app.run(threaded=True)

if __name__ == '__main__':
    run()