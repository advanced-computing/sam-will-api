from flask import Flask, jsonify, request, Response
import pandas as pd 
import io

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
    
    else:
        mta_data_filtered = column_filter(mta_data, column_name)

    return jsonify({column_name: mta_data_filtered.tolist()})

def column_filter(df, column_name):
    if column_name not in df.columns:
        print(f"'{column_name}' is not in the dataframe")
    else:
        return pd.DataFrame(df[column_name])
    

@app.route("/records", methods=['GET'])
def offset_limit():
    mta_data = pd.read_csv("MTA_data.csv")

    limit = request.args.get('limit', default=5, type=int) # Default limit is 5
    offset = request.args.get('offset', default=0, type=int) # Default offset is 0

    output = limit_offset(mta_data, limit, offset)
    return jsonify(output.to_dict(orient="records"))

def limit_offset(df, limit, offset):

    paginated_data = df.iloc[offset:offset + limit]  # Use iloc for row slicing

    return paginated_data

@app.route("/Date", methods=['GET'])
def retrieve_date():
    mta_data = pd.read_csv("MTA_data.csv")
    record_date = request.args.get("id")  # Get ID from query parameter

    if record_date is None:
        return jsonify({"error": "Please provide a date via the 'id' parameter"}), 400
    else:
        record = select_date(mta_data,record_date)

    return jsonify(record.to_dict(orient='records'))

def select_date(df,date):

    if date not in df["Date"].values:
        print(f"'{date}' is not in the data")
    else:
        return df[df["Date"]==date]

@app.route("/get_data", methods=["GET"])
def get_data():

    data = pd.read_csv("MTA_data.csv")
    output_format = request.args.get("format", "json").lower()

    if output_format == "csv":
        csv_buffer = io.StringIO()
        data.to_csv(csv_buffer, index=False)
        response = Response(csv_buffer.getvalue(), content_type="text/plain")
        return response
    
    if output_format == "json":
        return jsonify(data.to_dict(orient="records"))
    

if __name__ == "__main__":
    app.run(debug=True)