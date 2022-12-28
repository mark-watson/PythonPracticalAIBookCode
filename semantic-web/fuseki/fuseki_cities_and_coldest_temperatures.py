## Get Cityty names and coldest yearly temperature
## from Apache Jena Fuselki server on localhost
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
    ?city_uri
        <http://dbpedia.org/ontology/type>
        <http://dbpedia.org/resource/City> .
    ?city_uri
        <http://dbpedia.org/property/yearRecordLowF>
        ?record_year_low_temperature .
    ?city_uri
        <http://dbpedia.org/property/populationEst>
        ?population .
    ?city_uri
         <http://www.w3.org/2000/01/rdf-schema#label>
         ?dbpedia_label FILTER (lang(?dbpedia_label) = 'en') .        
}
LIMIT 20
"""

sparql = SPARQLWrapper("http://localhost:3030/news")
sparql.setQuery(queryString)
sparql.setReturnFormat(JSON)
sparql.setMethod('POST')
ret = sparql.queryAndConvert()
for r in ret["results"]["bindings"]:
    pprint(r)
