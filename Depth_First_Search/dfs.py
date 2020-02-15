# Time Complexity on a graph: O(V+E)
# V: Vertices
# E: Edges
####
# Time Complexity on a tree: O(V)
# V is the number of nodes
# Its goal is to search as deeply as possible, connecting as many nodes in the graph as possible and branching
# where necessary, before backtracking.
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
        print(node)
        visited.append(node) # it is appended in the visited array.
        for neighbour in graph[node]: # for each neighbor of the current node,
            dfs(visited, graph, neighbour) #the dfs function is invoked again

# The base case is invoked when all the nodes are visited. The function then returns.
# Driver Code
dfs(visited, graph, 'A') # 'A' is starting node


#########################################################################################################
# The implementation below uses the stack data-structure to build-up and return a set of vertices that are accessible
# within the subjects connected component. Using Python’s overloading of the subtraction operator to remove items from
# a set, we are able to add only the unvisited adjacent vertices.
# Iterative solution:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A')


#########################################################################################################

# The second implementation provides the same functionality as the first, however, this time we are using the more
# succinct recursive form. Due to a common Python gotcha with default parameter values being created only once, we are
# required to create a new visited set on each user invocation. Another Python language detail is that function
# variables are passed by reference, resulting in the visited mutable set not having to reassigned upon each recursive
# call.

# Recursive


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited

dfs(graph, 'A')