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


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """The python page route"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
