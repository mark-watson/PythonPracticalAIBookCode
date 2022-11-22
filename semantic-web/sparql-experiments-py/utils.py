from SPARQLWrapper import SPARQLWrapper, N3
from pprint import pprint

# from rdflib import Graph


def query(sparql_query, endpoint, return_format):
    #print("sparql_query = ", sparql_query)
    #print("return_format = ", return_format)
    #print("endpoint = ", endpoint)
    sparql = SPARQLWrapper(endpoint)
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(return_format)
    return sparql.query().convert()


def slurp(fpath):
    s = ""
    with open(fpath) as f:
        s = f.read()
    # print("slurp:", s)
    return s


def query_from_template(
    template_path, *args, endpoint="http://dbpedia.org/sparql", return_format="n3"):
    args = list(args)
    #print("args:", args)
    template = slurp(template_path)
    #print("template:", template)
    for index in range(len(args)):
        var = "<arg" + str(index) + ">"
        template = template.replace(var, args[index])
    #print(template)
    return query(template, endpoint, return_format)


# r = query_from_template('templates/select1.sparql', '<http://dbpedia.org/resource/Steve_Jobs>')
# pprint(r)
