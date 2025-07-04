from HW_1 import create_metro_graph
from collections import deque

metro_graph = create_metro_graph()

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


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print("→"+vertex, end='\n')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


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


def bfs_recursive(graph, queue, visited=None):
    
    if visited is None:
        visited = set()
    
    if not queue:
        return
    
    vertex = queue.popleft()
    
    if vertex not in visited:
      
        print("→"+vertex, end="\n")
        
        visited.add(vertex)
        
        queue.extend(set(graph[vertex]) - visited)
    
    bfs_recursive(graph, queue, visited)


if __name__ == "__main__":
    start_station = "Академмістечко"
    end_station = "Теремки"

    dfs_result = dfs_path(metro_graph, start_station, end_station)
    bfs_result = bfs_path(metro_graph, start_station, end_station)

    print(f"DFS шлях від {start_station} до {end_station}:")
    print("\n→ ".join(dfs_result))
    print(f"\nBFS шлях від {start_station} до {end_station}:")
    print(" \n→ ".join(bfs_result))
    print(f"Кількість станцій у шляху DFS: {len(dfs_result)}")
    print(f"Кількість станцій у шляху BFS: {len(bfs_result)}")

    # dfs_recursive(metro_graph, start_station)
    # print("\n")
    # bfs_queue = deque([start_station])
    # bfs_recursive(metro_graph, bfs_queue)
