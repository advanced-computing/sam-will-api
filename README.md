#sam-will-api 
##API Documentation

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

## Records
- Method: GET
- Path: Add '''/records?limit=(desired limit)&offset=(desired offset)'''
- Allows for returning a portion of the data




