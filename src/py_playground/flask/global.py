from flask import Flask, g

app = Flask(__name__)


@app.route('/global/<value>')
def global_usage(value):
    # This value will be available in this request.
    # see http://flask.pocoo.org/docs/0.12/api/#application-globals
    g.thing = value
    return "{}".format(g.get('thing'))
