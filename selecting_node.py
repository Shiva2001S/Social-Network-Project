import csv

import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
mydict, vis = {}, {}
# Open the CSV file for reading
with open('res.csv', 'r') as file:
    reader = csv.reader(file)

    # Loop over each row in the CSV file
    for row in reader:
        # Do something with the row
        if int(row[1]) > 3:
            mydict[int(row[0])] = True

with open('my2.csv', 'r') as file:
    reader = csv.reader(file)

    # Loop over each row in the CSV file
    for row in reader:
        # Do something with the row
        G.add_node(row[0])
        G.add_node(row[1])
        G.add_edge(row[0], row[1])

    
node_colors = ['red' if int(n) in mydict else 'green' for n in G.nodes()]
edge_colors = 'blue'
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2)
plt.axis('off')
plt.show()