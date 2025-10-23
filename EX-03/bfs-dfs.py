from collections import deque

graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': ['G'],
    'G': []
}

def bfs(start, goal):
    visited = set()
    queue = deque([[start]])
    print("BFS Path:")
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            if node == goal:
                print("Goal found! Path:", ' -> '.join(path))
                return
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    print("Goal not found in BFS.")

def dfs(start, goal):
    visited = set()
    stack = [[start]]
    print("\nDFS Path:")
    while stack:
        path = stack.pop()
        node = path[-1]

        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            if node == goal:
                print("Goal found! Path:", ' -> '.join(path))
                return
            for neighbor in reversed(graph[node]):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
    print("Goal not found in DFS.")

start_node = 'S'
goal_node = 'G'
print("AI Graph Search using BFS and DFS")
bfs(start_node, goal_node)
dfs(start_node, goal_node)
