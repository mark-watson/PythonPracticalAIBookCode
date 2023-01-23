import networkx as nx
from networkx.algorithms import isomorphism as iso
import random

def test_multiedge():
    # Simple test for multigraphs
    # Need something much more rigorous
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), 
             (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), 
             (10, 11), (10, 11), (11, 12), (11, 12), 
             (12, 13), (12, 13), (13, 14), (13, 14), 
             (14, 15), (14, 15), (15, 16), (15, 16), 
             (16, 17), (16, 17), (17, 18), (17, 18), 
             (18, 19), (18, 19), (19, 0), (19, 0)]
    nodes = list(range(20))

    for g1 in [nx.MultiGraph(), nx.MultiDiGraph()]:
        g1.add_edges_from(edges)
        for _ in range(10):
            new_nodes = list(nodes)
            random.shuffle(new_nodes)
            d = dict(zip(nodes, new_nodes))
            g2 = nx.relabel_nodes(g1, d)
            if not g1.is_directed():
                gm = iso.GraphMatcher(g1,g2)
            else:
                gm = iso.DiGraphMatcher(g1,g2)
            print(gm.is_isomorphic())

test_multiedge()