import networkx as nx
from networkx.algorithms import isomorphism as iso

def test_multiple():
    # Verify that we can use the graph matcher multiple times
    edges = [('A','B'),('B','A'),('B','C')]
    for g1,g2 in [(nx.Graph(),nx.Graph()), (nx.DiGraph(),nx.DiGraph())]:
        g1.add_edges_from(edges)
        g2.add_edges_from(edges)
        g3 = nx.subgraph(g2, ['A','B'])
        if not g1.is_directed():
            gmA = iso.GraphMatcher(g1,g2)
            gmB = iso.GraphMatcher(g1,g3)
        else:
            gmA = iso.DiGraphMatcher(g1,g2)
            gmB = iso.DiGraphMatcher(g1,g3)
        print(gmA.subgraph_is_isomorphic())
        g2.remove_node('C')
        print(gmA.subgraph_is_isomorphic())
        print(gmB.subgraph_is_isomorphic())

test_multiple()