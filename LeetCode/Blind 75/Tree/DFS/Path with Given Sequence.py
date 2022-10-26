# Path With Given Sequence (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743947562_57Unit

# Problem Statement
#
# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
# Example 1:
#           1
#         /   \
#       7       9
#              /  \
#             2    9
# Sequence: [1, 9, 9]
# Output: true
# Explanation: the tree has a path 1 -> 9 -> 9
#
# Example 2:
#           1
#         /    \
#       0        1
#     /        /   \
#    1        6     5
# Sequence: [1, 0, 7]
# Output: false
# Explanation: the tree does not have a path 1 -> 0 -> 7
#
# Sequence: [1, 1, 6]
# Output: true
# Explanation: the tree does not have a path 1 -> 1 -> 6

# Solution
#
# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach and additionally,
# track the element of the given sequence that we should match with the current node. Also, we can return false as
# soon as we find a mismatch between the sequence and the node value.
