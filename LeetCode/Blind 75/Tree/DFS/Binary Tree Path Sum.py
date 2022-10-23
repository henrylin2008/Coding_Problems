# Binary Tree Path Sum (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743923908_54Unit

# Problem Statement
#
# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the
# node values of that path equals ‘S’.

# Example 1:
#           1
#         /   \
#       2       3
#     /   \    /  \
#   4     5   6    7
# S: 10
# Output: true
# Explanation: The path with Sum '10' is highlighted
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# S: 23
# Output: true
# Explanation: The path wth sum '23' is highlighted (12 -> 1 -> 10)
#
# S: 16
# Output: false
# Explanation: There is no root-to-leaf path with sum '16'.