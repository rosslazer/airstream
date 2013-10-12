import json
import urllib

data = {}
json_data = open('../resources/us-counties.json')
data = json.load(json_data)

data = data['features']