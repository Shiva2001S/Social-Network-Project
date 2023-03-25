import networkx as nx
import matplotlib.pyplot as plt
import csv

# Load data as a NetworkX graph
G = nx.read_edgelist('my2.csv', delimiter=',')

# Calculate the degree of each node
degree_dict = dict(G.degree())

with open('res.csv', 'w', newline='') as file:
    writer = csv.writer(file)
# Print the degree of each node
    for node in degree_dict:
        print(f"Node {node} has degree {degree_dict[node]}.")
        # nx.write_edgelist(node, 'res.csv', delimiter=',')
        writer.writerow(f"{node}{degree_dict[node]}")


