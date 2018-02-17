import networkx as nx
DistMatrix =([[0,      0.3,    0.4,    0.7],
			[0.3,    0,      0.9,    0.2],
			[0.4,    0.9,    0,      0.1],
			[0.7,    0.2,    0.1,    0] ])
			
G = G=nx.from_numpy_matrix(DistMatrix)
nx.draw(G)
