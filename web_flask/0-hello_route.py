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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
