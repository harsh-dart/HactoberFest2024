from collections import deque
from typing import List, Dict

# Define the graph as an adjacency list
graph: Dict[str, List[str]] = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '3': ['7', '8'],
    '4': ['9'],
    '5': ['10', '11'],
    '6': [],
    '7': ['12'],
    '8': [],
    '9': ['13'],
    '10': [],
    '11': ['14'],
    '12': [],
    '13': [],
    '14': []
}

def bfs(start_node: str) -> None:
    visited = []  # List to keep track of visited nodes
    queue = deque()  # Queue for BFS

    # Start with the initial node
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()  # Efficiently pop from the left
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search:")
bfs('1')
