# pip install networkx

import networkx as nx
from networkx.algorithms.link_analysis.hits_alg import hits

# directed graph
G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D"])
G.add_edges_from([("A", "D"), ("A", "C"), ("B", "A")])

# running hits
h, a = nx.hits(G, max_iter=100)
print ("HUBS scores:", h)
print ("AUTH scores:", a)
