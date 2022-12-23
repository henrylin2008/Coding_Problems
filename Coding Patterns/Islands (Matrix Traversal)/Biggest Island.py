# Biggest Island (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d53be009288Unit

# Problem Statement
#
# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a
# function to return the area of the biggest island.
#
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is
# considered connected to other cells horizontally or vertically (not diagonally).
#
# Example 1
# Input: matrix =
#      -------------------------------
#      |  1  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  1  |  0  |  0  |  1  |
#      -------------------------------
#      |  0  |  0  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#
#
# Output: 5
# Explanation: The matrix has three islands. The biggest island has 5 cells .
#      -------------------------------
#      |  1* |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  1* |  0  |  0  |  1* |
#      -------------------------------
#      |  0  |  0  |  1* |  1* |  0  |
#      -------------------------------
#      |  0  |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1* |  0  |  0  |
#
# Solution
#
# The question follows the Island pattern and is quite similar to Number of Islands problem.
#
# We will traverse the matrix linearly to find islands.
#
# Whenever we find a cell with the value '1' (i.e., land), we have found an island. Using that cell as the root node,
# we will perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected land cells.
# During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells.
#
# We will keep a variable to remember the max area of any island.
