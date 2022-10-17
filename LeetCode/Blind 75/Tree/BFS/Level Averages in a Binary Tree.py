# Level Averages in a Binary Tree (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743864804_47Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent the averages of all of its levels.

# Example 1:
#           1
#         /   \
#       2       3
#     /   \    /  \
#   4     5   6    7
#   Level Averages: [1, 2.5, 5.5]
#
# Example 2:
#           12
#         /    \
#       7        1
#     /   \    /   \
#    9     2  10    5

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that instead of keeping track of all nodes of a level, we will only track the running sum of the
# values of all nodes in each level. In the end, we will append the average of the current level to the result array.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None