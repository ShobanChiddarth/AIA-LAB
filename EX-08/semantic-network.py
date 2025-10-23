import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from([
    ("Computer", "Machine", {"label": "is-a"}),
    ("Computer", "CPU", {"label": "has-a"}),
    ("CPU", "ALU", {"label": "has-a"}),
    ("CPU", "Control Unit", {"label": "has-a"}),
    ("Computer", "Monitor", {"label": "has-a"}),
    ("Monitor", "Output Device", {"label": "is-a"}),
    ("Computer", "Keyboard", {"label": "has-a"}),
    ("Keyboard", "Input Device", {"label": "is-a"}),
    ("Machine", "Thing", {"label": "is-a"})
])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2500, font_weight="bold", arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'), font_color="blue")

plt.axis("off")
plt.title("Semantic Network")
plt.show()
