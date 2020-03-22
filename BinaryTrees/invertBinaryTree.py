# Invert Binary Tree
# Level: Medium
# https://www.algoexpert.io/questions/Invert%20Binary%20Tree
# Write a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node
# in the tree for its corresponding (mirrored) right node. Each Binary Tree node has a value stored in a property called
# "value" and two children nodes stored in properties called "left" and "right," respectively. Children nodes can either
# be Binary Tree nodes themselves or the None (null) value.
#
# Sample Input:
#           1
#          / \
#         2   3
#        / \ / \
#       4  5 6  7
#      / \
#     8   9
#
# Sample Output:
#           1
#          / \
#         3   2
#        / \ / \
#       7  6 5  4
#              / \
#             9   8

# Method 1: iterative | Breadth first search, go through nodes level by level, swap left and right nodes, then append it
# to the queue
# Time: O(n)
# Space: O(n)

def invertBinaryTree(tree):
    queue = [tree]  # using queue to store nodes
    while len[queue]:   # if there's still node/s in the queue
        current = queue.pop(0)  # current is first node in the queue
        if current is None:     # skip if the node is null node
            continue
        swapLeftAndRight(current)   # call helper function to swap left and right nodes
        queue.append(current.left)  # add left node to the queue
        queue.append(current.right) # add right node to the queue

def swapLeftAndRight(tree):     # helper function that swap left and right nodes
    tree.left, tree.right = tree.right, tree.left


