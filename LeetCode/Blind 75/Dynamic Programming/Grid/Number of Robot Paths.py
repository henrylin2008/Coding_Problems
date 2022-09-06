# Number of Unique Paths to Go from Top Left to Bottom Right
# https://algo.monster/problems/robot_unique_path

# A robot is located at the top-left corner of a m x n grid.
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
# corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Example 1:
# Input: m = 2, n = 3
# Output: 3
#
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
#
#   1. Right -> Right -> Down
#   2. Right -> Down -> Right
#   3. Down -> Right -> Right
#
# Example 2:
# Input: m = 5, n = 3
# Output: 15

# Solution

# This is a "Grid DP" problem. It's an extension of the "Sequence DP" where dp[i] normally represents the max/min/best
# value for sequence ending at index i.
#
# The key is that the robot can move to the right or down only. This translates to "the robot could only reach a cell
# from top or left". Hence the number of paths to reach a cell = number of paths to reach the cell to the left +
# number of paths to reach the cell at the top.
#
# Let dp[r][c] represent the number of unique paths to reach cell (r, c). (r stands for row, and c stands for column.
# I found it more intuitive than i, j)
#
# dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
#
# where (r - 1, c) is the cell on the left and (r, c - 1) is the cell at the top.
#
# Time Complexity: O(n*m)

# Note that since for the top row, there's only one way to reach each cell - from the left. And for the leftmost
# column, there's only one way to reach each cell - from the top. We pre-populate them before moving to the internal
# cells.
