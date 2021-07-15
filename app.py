"""
Simples Flask app code.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Returns a simple statement"""
    return "Hello World!"
