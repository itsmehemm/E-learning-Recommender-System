import networkx as nx
import numpy as np
import string
import matplotlib.pyplot as plt

dt = [('len', float)]

A = np.array([(0, 0.3, 0.4, 0.7),
               (0.3, 0, 0.9, 0.2),
               (0.4, 0.9, 0, 0.1),
               (0.7, 0.2, 0.1, 0)
               ])*10
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.drawing.nx_agraph.to_agraph(G)

#G.node_attr.update(color="red", style="filled")
#G.edge_attr.update(color="blue", width="2.0")

#G.draw('distances.png', format='png', prog='neato')
