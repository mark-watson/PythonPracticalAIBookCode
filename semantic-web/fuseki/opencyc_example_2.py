## Test client for Apache Jena Fuselki server on localhost

import rdflib
from SPARQLWrapper import SPARQLWrapper, JSON
from pprint import pprint

queryString = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT *
WHERE {
    <http://sw.opencyc.org/concept/Mx4rvV7SqpwpEbGdrcN5Y29ycA>  rdfs:label ?label
    FILTER (lang(?label) = 'en') .
    <http://sw.opencyc.org/concept/Mx4rvV7SqpwpEbGdrcN5Y29ycA>
      <http://www.w3.org/2002/07/owl#sameAs> ?dbpedia_uri filter(strstarts(str(?dbpedia_uri), "http://dbpedia.org/resource")) .
  SERVICE <http://dbpedia.org/sparql?timeout=30000> {
      ?dbpedia_uri  ?dbpedia_property ?dbpedia_object  .
  }
}
LIMIT 4
"""

sparql = SPARQLWrapper("http://localhost:3030/opencyc")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
sparql.setMethod('POST')
ret = sparql.queryAndConvert()
for r in ret["results"]["bindings"]:
    pprint(r)
