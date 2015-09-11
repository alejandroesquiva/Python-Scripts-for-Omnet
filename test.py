import networkx as nx
import matplotlib.pyplot as plt
import json

# Load init position
with open('init_node_position.json') as position_file:    
    myjson = json.load(position_file)
    positions = myjson['Nodes']
    edges = myjson['Edges']
# Create a set of nodes with their position.
G = nx.DiGraph()
G.add_nodes_from(positions.keys())
#squares = [G.add_edges_from(key,value) for key,value in edges]
myedges = [(key, val) for key in edges for val in edges[key]]
print(myedges)
'''
for key in edges:
	a, b = edges[key]
	G.add_edge(a,b)
'''
G.add_edges_from(myedges)
nx.draw(G,positions)

#nx.draw(G)
plt.show()

