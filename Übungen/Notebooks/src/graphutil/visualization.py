import networkx as nx
import matplotlib.pyplot as plt


def camel_case():
    print("camel case")


def draw_emphasizing_edge_weight(G):
    pos = nx.drawing.layout.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif')

    for edge in G.edges(data='weight'):
        nx.draw_networkx_edges(G, pos, edgelist=[edge], width=edge[2])


def draw_graph_and_color_groups(G, groups=None, layout="circular"):
    """
    At most 8 different groups supported. If groups is None all nodes belong to the same group
    """
    if groups is None:
        groups = [G.nodes()]

    pos = None
    if (layout == "circular"):
        pos = nx.drawing.layout.circular_layout(G)
    elif (layout == "spring"):
        pos = nx.drawing.layout.spring_layout(G)
    color = ['lightblue', 'lightgreen', 'tan', 'orange', 'lavender', 'grey', 'magenta', 'beige']

    for i, group in enumerate(groups):
        nx.draw_networkx_nodes(G, pos, nodelist=group, node_color=color[i])

    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family='sans-serif')


def draw_graph_with_centralities(G, centrality_map):
    plt.figure()
    pos_nodes = nx.spring_layout(G)
    nx.draw(G, pos_nodes, node_color="lightblue", with_labels=False,
            node_size=[(centrality_map[node] + 1) * 100 for node in G.nodes()])

    labels = {}
    for k, v in centrality_map.items():
        labels[k] = f"{k} ({centrality_map.get(k):.3f})"

    nx.draw_networkx_labels(G, pos_nodes, labels=labels)
    plt.show()

