#!/usr/bin/python3
"""The script starts a web flask application
"""
from flask import Flask


app = Flask(__name__)
"""The flask app instance"""
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """The homepage"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_page(text):
    """The c page route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python_page(text='is cool'):
    """The python page route"""
    return 'Python {}'.format(text.replace('/', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
