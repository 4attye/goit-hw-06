from HW_1 import create_metro_graph


def dijkstra(graph, start, end=None):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes} 
    unvisited = set(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        if current_vertex == end:
            break 

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get('weight', 1)
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    # Відновлення шляху якщо вказана кінцева точка
    path = []
    if end is not None and distances[end] != float('inf'):
        node = end
        while node is not None:
            path.insert(0, node)
            node = previous_nodes[node]

    return distances, path

if __name__ == "__main__":

    G = create_metro_graph()
    start_station = "Червоний хутір"
    end_station = "Оболонь"

    distances, _ = dijkstra(G, start_station)
    print(f"Відстані від станції {start_station} до всіх інших станцій:")
    for vertex, dist in distances.items():
        print(f"{vertex}: {dist}")

    distances, path = dijkstra(G, start_station, end_station)

    print(f"\nВідстані від станції {start_station} до {end_station}:")
    print("Шлях:", "\n → ".join(path))
    print(f"Відстань:, {distances[end_station]} хв.")