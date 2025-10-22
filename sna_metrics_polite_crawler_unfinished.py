import json
import networkx as nx
import matplotlib.pyplot as plt

# Load saved crawl data
with open("results.json") as f:
    data = json.load(f)

G = nx.DiGraph()

# Build graph: each page = node; each link = edge
for src, info in data.items():
    G.add_node(src, title=info["title"])
    for tgt in info["links"]:
        if tgt in data:  # only internal links
            G.add_edge(src, tgt)

# --- SNA Metrics ---
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Degree Centrality
deg = nx.degree_centrality(G)
print("Top central nodes:", sorted(deg.items(), key=lambda x: -x[1])[:3])

# Draw simple network
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color="lightblue", node_size=800, font_size=7)
plt.title("Web Page Link Network")
plt.show()
