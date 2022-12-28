## Test client for Apache Jena Fuselki server on localhost
##
## Do git clone https://github.com/mark-watson/fuseki-semantic-web-dev-setup
## and run ./fuseki-server --file RDF/fromdbpedia.ttl /news
## in the cloned directory before running this example.

import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint

queryString = """
SELECT *
WHERE {
    ?s ?p ?o
}
LIMIT 5
"""

sparql = SPARQLWrapper("http://localhost:3030/news")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
sparql.setMethod('POST')
ret = sparql.queryAndConvert()
for r in ret["results"]["bindings"]:
    pprint(r)
