# We need heapq for priority queue operations
import heapq

# Step 1: Define the graph (adjacency list)
graph = {
    'A': ['B', 'D'],
    'B': ['E', 'G'],
    'D': ['G', 'H'],
    'G': ['I'],
    'H': ['I'],
    'E': [],
    'I': []
}

# Step 2: Define heuristic values (h(n))
heuristic = {
    'A': 999,  # not needed for A* but kept for GBFS
    'B': 5,
    'D': 2,
    'E': 4,
    'G': 6,
    'H': 1,
    'I': 0
}

# Step 3: Uniform edge cost (used in A*)
edge_cost = 1  # all edges are assumed to cost 1

# ==============================
# GREEDY BEST-FIRST SEARCH
# ==============================

# ==============================
# A* SEARCH
# ==============================

start_node = 'A'
goal_node = 'I'

def greedy_bfs(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], [start]))
    print("--- Greedy Best-First Search ---")
    
    while priority_queue:
        _, path = heapq.heappop(priority_queue)
        node = path[-1]
        
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            
            if node == goal:
                print("Path found:", path)
                return
            
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (heuristic[neighbor], new_path))
    
    print("Goal not found in Greedy Best-First Search.")

def a_star(start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], 0, [start]))  # (f(n), g(n), path)
    print("\n--- A* Search ---")
    
    while priority_queue:
        f_cost, g_cost, path = heapq.heappop(priority_queue)
        node = path[-1]
        
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            
            if node == goal:
                print("Path found:", path)
                return
            
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                g_new = g_cost + edge_cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(priority_queue, (f_new, g_new, new_path))
    
    print("Goal not found in A* Search.")



greedy_bfs(start_node, goal_node)
a_star(start_node, goal_node)
