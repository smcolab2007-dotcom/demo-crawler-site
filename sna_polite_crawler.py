#Run this code after crawler collects the data and saves results in csv

!pip install networkx matplotlib --quiet
import networkx as nx
import matplotlib.pyplot as plt

# Ensure crawl results exist
if "results" not in locals() or not results:
    raise ValueError("⚠️ 'results' not found. Run the crawler first!")

# Create directed graph
G = nx.DiGraph()

# Add nodes only (since links are not stored by crawler)
for page_url, page_title in results.items():
    G.add_node(page_url, title=page_title)

# Draw the graph (only nodes, no arrows yet)
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightgreen',
        node_size=800, font_size=8, font_weight='bold')
plt.title("Web Pages Crawled (Nodes Only – No Link Data Yet)")
plt.show()

print(f"✅ Total Pages Crawled: {len(G.nodes())}")
print("\nInterpretation:")
print("• Each node represents a crawled webpage from your demo site.")
print("• Since the crawler doesn’t store links between pages, this shows page coverage only.")
print("• In Social Network Analysis (SNA), this is like mapping isolated individuals before studying their connections.")
