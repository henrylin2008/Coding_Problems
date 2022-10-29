# Tree Diameter (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743963987_59Unit
#
# Problem Statement
#
# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest
# path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
#
# Note: You can always assume that there are at least two leaf nodes in the given tree.
# Example 1:
#           1
#         /    \
#       2        3
#     /        /   \
#    4        5     6
# Output: 5
# Explanation: The diameter of the tree is: [4, 2, 1, 3, 6]
#
# Example 2:
#           1
#         /    \
#       2        3
#              /   \
#             5     6
#           /   \   |
#         7     8   9
#               |   |
#              10  11
# Output: 7
# Explanation: The diameter of the tree is: [10, 8, 5, 3, 6, 9, 11]
