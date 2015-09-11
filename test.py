import networkx as nx
import matplotlib.pyplot as plt
import json

# Load init position
with open('init_node_position.json') as position_file:    
    positions = json.load(position_file)['Nodes']
# Create a set of nodes with their position.
G = nx.Graph()
G.add_nodes_from(positions.keys())
nx.draw(G,positions)
plt.show()

