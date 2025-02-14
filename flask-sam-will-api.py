from flask import Flask, jsonify, request
import pandas as pd 

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World! From Will and Sam </p>"