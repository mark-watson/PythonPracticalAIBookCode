from utils import query_from_template
from pprint import pprint

# Possible values: data:`json`,: data:`xml`,: data:`turtle`,: data:`n3`,: data:`rdf`,: data:`rdfxml`,: data:`csv`,: data:`tsv`,: data:`json-ld`

r_json = query_from_template(
    "templates/select1.sparql",
    "<http://dbpedia.org/resource/Steve_Jobs>",
    endpoint="http://dbpedia.org/sparql",
    return_format="json",
)

pprint(r_json)

r_csv = query_from_template(
    "templates/select1.sparql",
    "<http://dbpedia.org/resource/Steve_Jobs>",
    endpoint="http://dbpedia.org/sparql",
    return_format="csv",
)

print(r_csv.decode("utf-8"))
