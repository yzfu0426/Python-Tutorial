import json
import requests
from urllib.request import urlopen

#     sourceurl = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"

url = "https://api.themoviedb.org/3/movie/now_playing?api_key=a07e22bc18f5cb106bfe4cc1f83ad8ed"

with urlopen(url) as response:
    source = response.read() #a string

#print(source)

data = json.loads(source)

#print(json.dumps(data, indent=2))
#print(len(data['results']))

popularities = {}

for item in data['results']:
    name = item['title']
    popularity = item['popularity']
    popularities[name] = float(popularity)
    #print(name, popularity)

print(popularities)
