# Define the graph as a dictionary
graph = {
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

visited = []  # List to keep track of visited nodes
queue = []    # Initialize the queue

def bfs(visited, graph, node):
    # Mark the starting node as visited and enqueue it
    visited.append(node)
    queue.append(node)

    while queue:
        # Dequeue a node from the queue
        s = queue.pop(0)
        print(s, end=" ")  # Print the dequeued node

        # Get all adjacent nodes of the dequeued node
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)  # Mark as visited
                queue.append(neighbour)     # Enqueue the neighbour

print("Following is the Breadth-First Search:")
bfs(visited, graph, '1')

