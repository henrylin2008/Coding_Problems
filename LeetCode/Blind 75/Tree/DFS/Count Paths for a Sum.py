# Count Paths for a Sum (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743955693_58Unit

# Problem Statement
#
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each
# path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from
# parent to child (top to bottom).
#
# Example 1:
#           1
#         /   \
#       7       9
#     /   \    /  \
#   6     5   2    3
# S: 12
# Output: 3
# Explanation: There are three paths with sum '12': 7 -> 5, 1 -> 9 -> 2, and 9 -> 3
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    4       10     5
# S: 11
# Output: 2
# Explanation: Here are the two paths with sum '11': 7 -> 4 and 1 -> 10
