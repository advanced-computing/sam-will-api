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


@app.route("/column", methods=["GET"])
def select_a_column():
    mta_data = pd.read_csv("MTA_data.csv")
    column_name = request.args.get("field")  # Get the column name from query params
    
    if not column_name:
        return jsonify({"error": "Please provide a column name via 'field' parameter"}), 400
    
    if column_name not in mta_data:
        return jsonify({"error": f"Column '{column_name}' not found"}), 400
    #small change
    return jsonify({column_name: mta_data[column_name].tolist()})  # Convert Series to list

@app.route("/records", methods=['GET'])
def offset_limit():
    mta_data = pd.read_csv("MTA_data.csv")
    limit = request.args.get('limit', default=5, type=int) # Default limit is 5
    offset = request.args.get('offset', default=0, type=int) # Default offset is 0

    paginated_data = mta_data.iloc[offset:offset + limit]  # Use iloc for row slicing

    return jsonify(paginated_data.to_dict(orient="records"))

@app.route("/Date", methods=['GET'])
def retrieve_date():
    mta_data = pd.read_csv("MTA_data.csv")
    record_date = request.args.get("id")  # Get ID from query parameter

    if record_date is None:
        return jsonify({"error": "Please provide a date via the 'id' parameter"}), 400

    # Assuming there's an 'ID' column in your CSV
    record = mta_data[mta_data['Date'] == record_date]

    if record.empty:
        return jsonify({"error": f"No data found for date {record_date}"}), 404

    return jsonify(record.to_dict(orient='records'))


if __name__ == "__main__":
    app.run(debug=True)