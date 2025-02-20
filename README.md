# sam-will-api 
## API Documentation

## Connecting to the API
Run the API by running '''flask —app flask-sam-will-api.py run''' or '''python flask-sam-will-api.py''' in the terminal or by going to the endpoint url here: '''http://127.0.0.1:5000'''

The following routes can be used to access the data.

## Data
- Path: Add '''/data''' to the end of the endpoint url
- Provides the data as a JSON 

## Column
- Method: GET
- Path: Add '''/column?field=(column_name)''' to the end of the endpoint url
- Allows selecting a single column of data from the dataset, the data is returned as JSON
- Example: '''column?field=Date'''

## Records
- Method: GET
- Path: Add '''/records?limit=(desired limit)&offset=(desired offset)'''
- Allows for returning a portion of the data
- Example: '''/records?limit=5&offset=10'''

## Date
- Method: GET
- Path: Add '''/Date?id=(desired date)'''
- The date should be formatted as mm/dd/yyyy 
- Allows for selecting a single part of the data
- Example: '''/Date?id=03/01/2020'''

## Get Data
- Method: GET
- Path: Add '''get_data?format=(json/csv)
- Presents the data as either JSON or csv
- Example: The default is JSON format, either leave the '''?format=''' off completely or type '''?format=json'''
