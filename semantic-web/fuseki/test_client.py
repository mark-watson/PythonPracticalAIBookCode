## Test cleint for Apache Jena Fuselki server on localhost

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

sparql = SPARQLWrapper("http://localhost:3030/opencyc")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
sparql.setMethod('POST')
ret = sparql.queryandconvert()
for r in ret["results"]["bindings"]:
    pprint(r)
