# Problem Challenge 2: Path with Maximum Sum (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743967658_60Unit

# Problem Statement
#
# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
#
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
# The path must contain at least one node.
# Example 1:
#           1
#         /   \
#       2      3
#       |     /  \
#       4    5    6
# Output: 16
# Explanation: the path with maximum sum is: [4, 2, 1, 3, 6]
#
# Example 2:
#           1
#         /    \
#       2        3
#     /  \     /   \
#    1    3   5     6
#            / \    |
#           7   8   9
# Output: 31
# Explanation: The path with maximum sum is: [8, 5, 3, 6, 9]
#