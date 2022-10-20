# Connect Level Order Siblings (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743890075_50Unit

# Problem Statement
#
# Given a binary tree, connect each node with its level order successor. The last node of each level should point to
# a null node.
#
# Example 1:
#            1   --> null
#         /    \
#       2  -->   3  --> null
#     /   \     /  \
#   4  --> 5-> 6 -> 7 --> null
#
# Example 2:
#           12  --> null
#         /    \
#       7   -->  1 --> null
#     /        /   \
#    9  -->  10  ->  5 --> null
#
# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference is that while traversing a level we will remember the previous node to connect it with the current node.
#

