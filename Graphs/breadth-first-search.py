# Link: https://www.algoexpert.io/questions/Breadth-first%20Search
# Breadth-First search
# Difficulty: Medium

# You're given a Node class that has a name and an array of optional children nodes. When put together, nodes from an
# acyclic tree-like structure.
# Implement the breadthFirstSearch method on the Node class, which takes in an empty array, traverses the tree using the
# Breadth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in
# the input array, and returns it.

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


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Time: O(v+e); v: number of vertices/(nodes); e: number of edges connecting nodes
    # Space: O(v); v: vertices (nodes); we're storing nodes in the array; or worse case when all children nodes are
    #              under one root node
    def breadthFirstSearch(self, array):
        queue = [self]  # self node
        while len(queue) > 0:   # while there's node/s in the queue
            current = queue.pop(0)  # pop first item from the queue and set it to current node
            array.append(current.name)   # append current node's name into the final array
            for child in current.children:  # for every child
                queue.append(child)   # append the child to the end of the queue
        return array
