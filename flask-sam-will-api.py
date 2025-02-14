from flask import Flask, jsonify, request
import pandas as pd 

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World! From Will and Sam </p>"

@app.route("/data")
def convert_and_print():
    mta_data = pd.read_csv("MTA_data.csv")
    json_data = mta_data.to_dict(orient='records')  # Convert to Python list of dicts
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)