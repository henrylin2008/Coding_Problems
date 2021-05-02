# Link: https://www.algoexpert.io/questions/Cycle%20In%20Graph
# Cycle In Graph
# Difficulty: Medium

# You're given a list of edges representing an unweighted, directed graph with at least one node. Write a function that
# returns a boolean representing whether the given graph contains a cycle.

# For the purpose of this question, a cycle is defined as any number of vertices, including just one vertex, that are
# connected in a closed chain. A cycle can also be defined as a chain of at least one vertex in which the first vertex
# is the same as the last.
# The given list is what's called an adjacency list, and it represents a graph. The number of vertices in the graph is
# equal to the length of edges, where each index i in edges contains vertex i's outbound edges, in no particular order.
# Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list
# that this vertex is connected to. Note that these edges are directed, meaning that you can only travel from a
# particular vertex to its destination, not the other way around (unless the destination vertex itself has an outbound
# edge to the original vertex).
# Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; in
# other words, it's an edge that connects a vertex to itself. For the purpose of this question, a self-loop is
# considered a cycle.

# Sample Input:
# edges = [
#   [1, 3],
#   [2, 3, 4],
#   [0],
#   [],
#   [2, 5],
#   [],
#   ]

# Sample Output:
# true
# // There are multiple cycles in this graph:
# // 1) 0 -> 1 -> 2 -> 0
# // 2) 0 -> 1 -> 4 -> 2 -> 0
# // 3) 1 -> 2 -> 0 -> 1
# There are just 3 examples; there are more.


# Time: O(v + e); v: number of vertices; e: number of edges
# Space: O(v)
# Idea: Traverse a graph with BFS, if a back edge (edge from a node to one of its ancestors) in the DFS tree, then it
#       denotes the presence of a cycle
# Logic: use 2 lists: one is to keep track of visited nodes (started as False); another one to keep track of which
#        nodes have been visited in the current recursive stack; Loop through nodes in the graph, if the node has been
#        visited, then skip it; otherwise, run DFS to check if its children contains a cycle; if its children contains a
#        cycle, then return True, else return False. The helper method (isNodeInCycle) runs DFS on child nodes, first,
#        set current node as True in visited and currentlyInStack, then get current node's outbound neighbors, and loop
#        through neighbor nodes, if it's not a visited node, run recursive calls to check if the neighbor contains a
#        cycle, if it contains a cycle, then return True; if outbound neighbor node is in the currentlyInStack, then
#        it's a cycle, return True. Reset current node in currentlyInStack list to False, and return False if no cycles
#        is found.
def cycleInGraph(edges):
    numOfNodes = len(edges)
    visited = [False for _ in range(numOfNodes)]    # set all values to False (not visited)
    currentlyInStack = [False for _ in range(numOfNodes)]   # non of nodes in stack

    for node in range(numOfNodes):  # loop through nodes in the graph
        if visited[node]:   # if the node has been visited, skip it
            continue

        # Run DFS on unvisited node to find any cycles in the nodes/graph, it returns True or False
        containsCycle = isNodeInCycle(edges, node, visited, currentlyInStack)   # edges, current node, 2 lists
        if containsCycle:   # if a cycle exists, return True
            return True

    return False   # If no cycles found in the graph, return False


# Run DFS on child nodes
def isNodeInCycle(edges, node, visited, currentlyInStack):
    visited[node] = True    # mark current node as visited
    currentlyInStack[node] = True   # mark current node in the recursive stack

    neighbors = edges[node]  # get outbound edges and what nodes it goes out to
    for neighbor in neighbors:  # loop through all neighbors
        if not visited[neighbor]:   # if node is not visited,
            # run DFS on the neighbor
            containsCycle = isNodeInCycle(edges, neighbor, visited, currentlyInStack)
            if containsCycle:   # if a cycle exist, return True
                return True
        elif currentlyInStack[neighbor]:  # if descendant node edge is connected to its ancestor, then a cycle exists
            return True

    currentlyInStack[node] = False  # current node is no longer in the recursive stack
    return False    # after all possible checks for a cycle have been done
