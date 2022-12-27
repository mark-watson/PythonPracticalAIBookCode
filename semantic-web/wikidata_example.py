import requests
import json

url = 'https://query.wikidata.org/sparql'
query = """
SELECT 
  ?countryLabel ?population ?area ?medianIncome ?age
WHERE {
  ?country wdt:P463 wd:Q458.
  OPTIONAL { ?country wdt:P1082 ?population }
  OPTIONAL { ?country wdt:P2046 ?area }
  OPTIONAL { ?country wdt:P3529 ?medianIncome }
  OPTIONAL { ?country wdt:P571 ?inception. 
    BIND(year(now()) - year(?inception) AS ?age)
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
"""
r = requests.get(url, params = {'format': 'json', 'query': query})
data = r.json()
#print(data)
print(json.dumps(data, indent=4, sort_keys=True))

