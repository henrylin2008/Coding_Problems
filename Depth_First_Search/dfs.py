# Time Complexity on a graph: O(V+E)
# V: Vertices
# E: Edges
####
# Time Complexity on a tree: O(V)
# V is the number of nodes
# Its goal is to search as deeply as possible, connecting as many nodes in the graph as possible and branching
# where necessary
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# The Algorithm
# Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
# Repeat until all the nodes are visited, or the node to be searched is found.

# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [] # Array to keep track of visited nodes.

def dfs(visited, graph, node): #graph in the form of a dictionary, and A, which is the starting node.
    if node not in visited: #It first checks if the current node is unvisited - if yes,
        print node,
        visited.append(node) # it is appended in the visited array.
        for neighbour in graph[node]: # for each neighbor of the current node,
            dfs(visited, graph, neighbour) #the dfs function is invoked again

# The base case is invoked when all the nodes are visited. The function then returns.
# Driver Code
dfs(visited, graph, 'A') # 'A' is starting node