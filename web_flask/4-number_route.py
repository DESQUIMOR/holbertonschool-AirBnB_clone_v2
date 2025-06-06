#!/usr/bin/python3
"""Flask web application with dynamic routes.

Routes:
    /: returns "Hello HBNB!"
    /hbnb: returns "HBNB"
    /c/<text>: returns "C <text>" (underscores replaced with spaces)
    /python/(<text>): returns "Python <text>" (default is "is cool")
    /number/<n>: returns "<n> is a number" (only if n is integer)
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Route /: display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route /hbnb: display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route /c/<text>: display 'C ' followed by text
    with _ replaced by space
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route /python/(<text>): display 'Python ' followed by text
    or default value if no text is provided
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route /number/<n>: display '<n> is a number'
    only if n is an integer
    """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
