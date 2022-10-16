# Zigzag Traversal (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743859019_46Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the
# values of all nodes of the first level from left to right, then right to left for the next level and keep
# alternating in the same manner for the following levels.
#
# Example 1:
#           [[1],
#            [3, 2],
#            [4, 5, 6, 7]]
#
# Example 2:
#           [[12],
#            [1, 7],
#            [9, 10, 5],
#            [17, 20]]

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# additional step we have to keep in mind is to alternate the level order traversal, which means that for every other
# level, we will traverse similar to Reverse Level Order Traversal.

