import networkx as nx
from networkx.algorithms.link_analysis.pagerank_alg import pagerank
# directed graph
G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D", "E"])
G.add_edges_from([("D", "A"), ("C", "A"), ("B", "A"), ("E", "D")])

# running pagerank
p = nx.pagerank(G, max_iter=100)
print ("PR scores:", p)
