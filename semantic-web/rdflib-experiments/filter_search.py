from rdflib import Graph
import rdflib

g = Graph()
g.parse("news.nt", format="nt")

print(len(g))  # prints 2

import pprint

for stmt in g:
    pprint.pprint(stmt)


def get_predicate_objects(g, predicate):
    return [o for s, p, o in g.triples((None, predicate, None))]


print(
    "preds:",
    get_predicate_objects(
        g, rdflib.term.URIRef("http://knowledgebooks.com/schema/topicCategory")
    ),
)

# query DBPedia for information on Bill Gates
def dbpedia_get_info_bill_gates(g):
    for s, p, o in g.triples(
        (None, rdflib.term.URIRef("http://dbpedia.org/ontology/birthPlace"), None)
    ):
        print(o)
