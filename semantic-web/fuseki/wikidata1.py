## Test client for Wikidata SPARQL endpoint

from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint

queryString = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT *
WHERE {
  ?subject skos:altLabel "International Business Machines"@en .
}
LIMIT 4
"""

uris = []

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
ret = sparql.query().convert()
for r in ret["results"]["bindings"]:
  pprint(r)
  if 'subject' in r:
    if 'value' in r['subject']:
      uri = r['subject']['value']
      print(uri)
      uris.append(uri)

queryString2 = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT *
WHERE {
  <A_URI> wdt:P31 ?entity_label . # wdt:P31 is instanceOf
  ?entity_label skos:altLabel ?entity_human_readable_label
    FILTER (lang(?entity_human_readable_label) = 'en') .
}
LIMIT 5
"""

def wd_helper(an_ibm_uri):
    print(f"\n *** {an_ibm_uri} ***\n")
    query = queryString2.replace("A_URI", an_ibm_uri)
    #print(query)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    ret = sparql.query().convert()['results']['bindings']
    for r in ret:
      print(r['entity_human_readable_label']['value'])

for uri in uris:
  wd_helper(uri)
