from sparql import dbpedia_sparql
from colorize import colorize_sparql

def flatten(a_list):
    return [item for items in a_list for item in items]

def dbpedia_get_relationships(s_uri, o_uri):
    query = (
        "SELECT DISTINCT ?p {{  {} ?p {} . FILTER (!regex(str(?p), 'wikiPage', 'i')) }} LIMIT 5"
        .format(s_uri, o_uri))
    results = dbpedia_sparql(query)
    print('Generated SPARQL to get relationships between two entities:')
    print(colorize_sparql(query))
    return [r for r in flatten(results) if not r == 'p']


def entity_results_to_relationship_links(uris):
    uris = [('<' + uri + '>') for uri in uris]
    relationship_statements = []
    for e1 in uris:
        for e2 in uris:
            if not e1 == e2:
                l1 = dbpedia_get_relationships(e1, e2)
                l2 = dbpedia_get_relationships(e2, e1)
                for x in l1:
                    relationship_statements.extend([[e1, e2, x]]) if not [e1,
                        e2, x] in relationship_statements else None
                for x in l2:
                    relationship_statements.extend([[e1, e2, x]]) if not [e1,
                        e2, x] in relationship_statements else None
    return relationship_statements

