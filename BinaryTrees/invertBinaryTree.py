# Invert Binary Tree
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

# Method 1: iterative | Breadth first search,
# Time: O(n)
# Space: O(n)

def invertBinaryTree(tree):
    queue = [tree]
    while len[queue]: # if queue is not empty, continue execute following code
        current = queue.pop(0)
        if current is None:
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left  # swap left and right nodes