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

