!pip install networkx matplotlib --quiet
import json, networkx as nx, matplotlib.pyplot as plt

# Load crawler results
with open("results.json") as f:
    results = json.load(f)

# Create directed graph (just nodes)
G = nx.DiGraph()
for page_url, page_title in results.items():
    G.add_node(page_url, title=page_title)

plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen',
        node_size=800, font_size=8, font_weight='bold')
plt.title("Web Pages Crawled (Nodes Only – No Link Data Yet)")
plt.show()

print(f"✅ Total Pages Crawled: {len(G.nodes())}")
