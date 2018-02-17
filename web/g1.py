try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

similarity = ([1, 0.2, 2.3], [0.2, 1, 0.4], [2.3, 0.4, 1])

G=nx.Graph()
for i in range(0, 3):
	for j in range(0, 3):
		G.add_edge(i, j, weight=similarity[i][j])
		

elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]

pos=nx.spring_layout(G) # positions for all nodes

# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
nx.draw_networkx_edges(G,pos,edgelist=esmall,
                    width=6,alpha=0.5,edge_color='b',style='dashed')

# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
