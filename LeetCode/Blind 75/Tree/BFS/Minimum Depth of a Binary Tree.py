# Minimum Depth of a Binary Tree (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743873257_48Unit

# Problem Statement
#
# Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the
# root node to the nearest leaf node.
#
# Example 1:
#           1
#         /   \
#       2       3
#     /   \
#   4     5
# Minimum Depth: 2
#
# Example 2:
#           12
#         /    \
#       7        1
#              /   \
#             10    5
# Minimum Depth: 2
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
#            |
#            11
# Minimum Depth: 3