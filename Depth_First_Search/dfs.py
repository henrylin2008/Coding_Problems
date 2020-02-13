# Time Complexity on a graph: O(V+E)
# V: Vertices
# E: Edges
####
# Time Complexity on a tree: O(V)
# V is the number of nodes
# Its goal is to search as deeply as possible, connecting as many nodes in the graph as possible and branching
# # where necessary

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

def dfs(visited, graph, node):
    if node not in visited:
        print node,
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')