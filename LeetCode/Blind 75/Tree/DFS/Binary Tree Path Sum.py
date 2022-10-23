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
# Explanation: The path with Sum '10' is highlighted (1 -> 3 -> 6)
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

# Solution
# As we are trying to search for a root-to-leaf path, we can use the Depth First Search (DFS) technique to solve this
# problem.
#
# To recursively traverse a binary tree in a DFS fashion, we can start from the root and at every step,
# make two recursive calls one for the left and one for the right child.
#
# Here are the steps for our Binary Tree Path Sum problem:
#   1. Start DFS with the root of the tree.
#   2. If the current node is not a leaf node, do two things:
#       -Subtract the value of the current node from the given number to get a new sum => S = S - node.value
#       -Make two recursive calls for both the children of the current node with the new number calculated in the
#        previous step.
#   3. At every step, see if the current node being visited is a leaf node and if its value is equal to the given
#      number ‘S’. If both these conditions are true, we have found the required root-to-leaf path, therefore return
#      true.
#   4. If the current node is a leaf but its value is not equal to the given number ‘S’, return false.

