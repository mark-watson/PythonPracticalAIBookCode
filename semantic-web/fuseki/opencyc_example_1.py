## Test client for Apache Jena Fuselki server on localhost

import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint

queryString = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT *
WHERE {
    <http://sw.opencyc.org/concept/Mx4rvV7SqpwpEbGdrcN5Y29ycA>  rdfs:label ?label
    FILTER (lang(?label) = 'en')
}
limit 20
"""

sparql = SPARQLWrapper("http://localhost:3030/opencyc")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
sparql.setMethod('POST')
ret = sparql.queryAndConvert()
for r in ret["results"]["bindings"]:
    pprint(r)
