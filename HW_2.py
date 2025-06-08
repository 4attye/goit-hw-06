from HW_1 import metro_map
from collections import deque

metro_map = metro_map()

def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None


def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

if __name__ == "__main__":
    start_station = "Академмістечко"
    end_station = "Теремки"

    dfs_result = dfs_path(metro_map, start_station, end_station)
    bfs_result = bfs_path(metro_map, start_station, end_station)

    print(f"DFS шлях від {start_station} до {end_station}:")
    print(" → ".join(dfs_result))
    print(f"\nBFS шлях від {start_station} до {end_station}:")
    print(" → ".join(bfs_result))
    print(f"Кількість станцій у шляху DFS: {len(dfs_result)}")
    print(f"Кількість станцій у шляху BFS: {len(bfs_result)}")
