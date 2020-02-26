# link: https://www.algoexpert.io/questions/Depth-first%20Search
# You are given a Node class that has a name and an array of optional children Nodes. When put together, Nodes form a
# simple tree-like structure. Implement the depthFirstSearch method on the Node class, which takes in an empty array,
# traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores
# all the of the Nodes' names in the input array, and returns it.
#
# sample input:
#             A
#            /|\
#           B C D
#          /\   /\
#         E  F G  H
#            /\ \
#           I J  K
#
# Sample output: ["A","B","E","F","I","J","C","D","G","K","H"]
# v: vertice (node)
# e: edge (lines connect between nodes)
# Time: O(v + e): vertices + edges
# Space: O(v): level of depth/height of the tree
# Recursive call, get
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)  # append the name to the array
        for child in self.children: # for each child in children
            child.depthFirstSearch(array) # call depthFirstSearch() function
        return array # useful on first row


#########################################################################################################

# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# Its goal is to search as deeply as possible, connecting as many nodes in the graph as possible and branching
# where necessary, before backtracking.

# Time Complexity on a graph: O(V+E)
# V: Vertices
# E: Edges
####
# Time Complexity on a tree: O(V)
# V is the number of nodes
# Using a Python dictionary to act as an adjacency list

# The Algorithm
# Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
# Repeat until all the nodes are visited, or the node to be searched is found.
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