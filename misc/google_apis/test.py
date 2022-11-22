"""Example of Python client calling Knowledge Graph Search API."""
# from example https://developers.google.com/knowledge-graph

import json
import urllib
from urllib.parse import urlencode
import urllib.request as url
from pathlib import Path

api_key = open(str(Path.home()) + "/.google_api_key").read()
query = 'Taylor Swift'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 10,
    'indent': True,
    'key': api_key,
}
url2 = service_url + '?' + urlencode(params)
print(url2)
response = json.loads(url.urlopen(url2).read())
for element in response['itemListElement']:
  print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')
