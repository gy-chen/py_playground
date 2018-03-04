import socketio
from flask import Flask, render_template

sio = socketio.Server()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('socketio.html')


@sio.on('dog')
def on_dog(sid, data):
    return "LaaLaa"


@sio.on('cat')
def on_cat(sid, data):
    return "Meow"


app = socketio.Middleware(sio, app)
