# Link: https://www.algoexpert.io/questions/Breadth-first%20Search
# Breadth-First search
# Difficulty: Medium

# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes from an
# acyclic tree-like structure.
# Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
# Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in
# the input array, and returns it.
# If you're unfamiliar with Breadth-first Search, we recommend watching the Conceptual Overview section of this
# question's video explanation before starting to code.

# Sample Input:
#  graph =      A
#            /  |  \
#          B    C    D
#         / \       /  \
#        E   F     G    H
#           / \     \
#          I   J     K
#
# Sample Output:
# ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]


# Time: O(v+e); v: number of vertices/(nodes); e: number of edges connecting nodes
# Space: O(v); v: vertices (nodes), because of return array has length of V; or tree has one recursive branches
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Grab current node's name and add it to the final array; then run a for loop which runs depthFirstSearch function,
    # which it repeats the same process; lastly return the final array
    def depthFirstSearch(self, array):
        array.append(self.name)   # append node's name
        for child in self.children:  # for every child
            child.depthFirstSearch(array)  # recursive call on children
        return array
