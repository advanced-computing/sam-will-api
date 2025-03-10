from flask import Flask, jsonify, request, Response
import pandas as pd 
import io
import duckdb

#connecting to the database
con = duckdb.connect('mta_data.db')
mta_df = con.table('mta').to_df()
con.close()

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Return a friendly HTTP greeting."""

    return "<p>Hello, World! From Will and Sam </p>"

@app.route("/data")
def convert_and_print():
    #mta_data = pd.read_csv("MTA_data.csv")
    mta_df
    json_data = mta_df.to_dict(orient='records')  # Convert to Python list of dicts
    return jsonify(json_data)


@app.route("/column", methods=["GET"])
def select_a_column():
    #mta_data = pd.read_csv("MTA_data.csv")
    mta_df
    column_name = request.args.get("field")  # Get the column name from query params
    
    if not column_name:
        return jsonify({"error": "Please provide a column name via 'field' parameter"}), 400
    
    else:
        mta_data_filtered = column_filter(mta_df, column_name)

    return jsonify({column_name: mta_data_filtered.tolist()})

def column_filter(df, column_name):
    if column_name not in df.columns:
        print(f"'{column_name}' is not in the dataframe")
    else:
        return pd.DataFrame(df[column_name])
    

@app.route("/records", methods=['GET'])
def offset_limit():
    #mta_data = pd.read_csv("MTA_data.csv")
    mta_df

    limit = request.args.get('limit', default=5, type=int) # Default limit is 5
    offset = request.args.get('offset', default=0, type=int) # Default offset is 0

    output = limit_offset(mta_df, limit, offset)
    return jsonify(output.to_dict(orient="records"))

def limit_offset(df, limit, offset):

    paginated_data = df.iloc[offset:offset + limit]  # Use iloc for row slicing

    return paginated_data

@app.route("/Date", methods=['GET'])
def retrieve_date():
    #mta_data = pd.read_csv("MTA_data.csv")
    mta_df
    record_date = request.args.get("id")  # Get ID from query parameter

    if record_date is None:
        return jsonify({"error": "Please provide a date via the 'id' parameter"}), 400
    else:
        record = select_date(mta_df,record_date)

    return jsonify(record.to_dict(orient='records'))

def select_date(df,date):

    if date not in df["Date"].values:
        print(f"'{date}' is not in the data")
    else:
        return df[df["Date"]==date]

@app.route("/get_data", methods=["GET"])
def get_data():

    #data = pd.read_csv("MTA_data.csv")
    mta_df
    output_format = request.args.get("format", "json").lower()

    if output_format == "csv":
        csv_buffer = io.StringIO()
        mta_df.to_csv(csv_buffer, index=False)
        response = Response(csv_buffer.getvalue(), content_type="text/plain")
        return response
    
    if output_format == "json":
        return jsonify(mta_df.to_dict(orient="records"))
    



@app.route("/users", methods=["POST"])
def add_users():
    #data = request.get("username", "age", "country")
    data = request.get_json()

    username = data["username"]
    age = data["age"]
    country = data["country"]


    con = duckdb.connect('mta_data.db')
    con.sql("CREATE TABLE IF NOT EXISTS users(username TEXT, age INT, country TEXT)")
    
    con.sql(f"INSERT INTO user VALUES ('{username}','{age}','{country}')")
    con.commit()



@app.route("/users", methods=["GET"])
def show_user():
    con = duckdb.connect('mta_data.db')
    #con.table('users').show()
    #from ChatGPT https://chatgpt.com/c/67cf35b5-a2ec-8009-a359-3ee708735f7e
    df = con.execute("SELECT * FROM users").fetchdf()
    
    # Convert DataFrame to JSON
    users_json = df.to_dict(orient="records")  # Convert rows to list of dictionaries
    
    return jsonify(users_json)  # Return JSON response


if __name__ == "__main__":
    app.run(debug=True)