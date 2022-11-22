"""Example of Python client calling Knowledge Graph Search API."""

import json
from urllib.parse import urlencode
from urllib.request import urlopen
from pathlib import Path
from pprint import pprint

api_key = open(str(Path.home()) + "/.google_api_key").read()
query = "Taylor Swift"
query = "Mark Louis Watson"
service_url = "https://kgsearch.googleapis.com/v1/entities:search"
params = {
    "query": query,
    "limit": 10,
    "indent": True,
    "key": api_key,
}
url = service_url + "?" + urlencode(params)
response = json.loads(urlopen(url).read())
print(response)
for element in response["itemListElement"]:
    print(element["result"]["name"] + " (" + str(element["resultScore"]) + ")")

pprint(response)

# use Google search API to get information about Bill Clinton
def get_bill_clinton_info():
    query = "Bill Clinton"
    service_url = "https://kgsearch.googleapis.com/v1/entities:search"
    params = {
        "query": query,
        "limit": 10,
        "indent": True,
        "key": api_key,
    }
    url = service_url + "?" + urlencode(params)
    response = json.loads(urlopen(url).read())
    return response


print(get_bill_clinton_info())
