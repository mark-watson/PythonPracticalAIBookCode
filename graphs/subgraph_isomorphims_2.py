import networkx as nx
from networkx.algorithms import isomorphism as iso
import random

def test_multiple():
    Atlas = nx.graph_atlas_g()[0:100]
    alphabet = list(range(26))
    for graph in Atlas:
        nlist = graph.nodes()
        labels = alphabet[:len(nlist)]
        for s in range(10):
            random.shuffle(labels)
            d = dict(zip(nlist,labels))
            relabel = nx.relabel_nodes(graph, d)
            gm = iso.GraphMatcher(graph, relabel)
            print(gm.is_isomorphic())
test_multiple()