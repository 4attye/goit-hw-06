import networkx as nx
import matplotlib.pyplot as plt
from pos import pos
from graph import metro_data


def create_metro_graph():

    G = nx.Graph()

    for station, (neighbors, weights, color) in metro_data.items():
        G.add_node(station, color=color[0])
        for neighbor, weight in zip(neighbors, weights):
            if not G.has_edge(station, neighbor):
                G.add_edge(station, neighbor, weight=weight, color=color[1])
    
    return G


if __name__ == "__main__":

    metro_graph = create_metro_graph()
    node_colors = [metro_graph.nodes[n]['color'] for n in metro_graph.nodes]
    edge_colors = [data['color'] for _, _, data in metro_graph.edges(data=True)]
 
    print(f"Кількість станцій (вершин): {metro_graph.number_of_nodes()}")
    print(f"Кількість з'єднань (ребер): {metro_graph.number_of_edges()}")

    print("\nСтупінь вершин:")
    for node, degree in metro_graph.degree():
        print(f"{node}: {degree}")

    plt.figure(figsize=(16, 9))
    nx.draw(metro_graph, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=400, font_size=10
            , font_color='black', font_weight='bold', width=4)
    plt.title("Київське метро")
    plt.show()
