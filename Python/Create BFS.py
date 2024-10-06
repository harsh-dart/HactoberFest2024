graph = {
   '1' : ['2','3','4'],
    '2' : ['5', '6'],
    '3' : ['7','8'],
    '4' : ['9'],
    '5' : ['10','11'],
    '6' : [],
    '7' : ['12'],
    '8' : [],
    '9' : ['13'],
    '10' : [],
    '11' : ['14'],
    '12' : [],
    '13' : [],
    '14' : []
}

visited = [] # this line is for visited list
queue = []   # Initializing queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]: # here s is already popped out
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '1')
