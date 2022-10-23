# All Paths for a Sum (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743930963_55Unit

# Problem Statement
#
# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of
# each path equals ‘S’.
#
# Example 1:
#           1
#         /   \
#       7       9
#     /   \    /  \
#   4     5   2    7
# S: 12
# Output: [[1,7,4], [1,9,2]
# Explanation: Here are the two paths with sum '12': 1 -> 7 -> 4 and 1 -> 9 -> 2
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    4       10     5
# S: 23
# Output: [[12, 7, 4], [12, 1, 10]]
# Explanation: Here are the two paths with sum '23': 12 -> 7 -> 4 and 12 -> 1 -> 10
