# Level Order Successor (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743880609_49Unit

# Problem Statement
# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order
# successor is the node that appears right after the given node in the level order traversal.


# Example 1:
#           1
#         /   \
#       2       3
#     /   \
#   4     5
# Given Node: 3
# Level Order Successor: 4

# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# Given Node: 9
# Level Order Successor: 10

# Example 3:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# Given Node: 12
# Level Order Successor: 7

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that we will not keep track of all the levels. Instead we will keep inserting child nodes to the
# queue. As soon as we find the given node, we will return the next node from the queue as the level order successor.
