# Minimal Path Sum
# https://algo.monster/problems/minimal_path_sum

# Suppose we have a m by n matrix filled with non-negative integers, find a path from top left corner to bottom right
# corner which minimizes the sum of all numbers along its path.
#
# Note: Movements can only be either down or right at any point in time.

# Example:
# Input:
#   [
#     [1,3,1],
#     [1,5,1],
#     [4,2,1]
#   ]
# Output: 7
# Explanation:
# Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


# Solution
# This problem is similar to Robot Unique Paths. We can only move right or down from a cell. The difference is the
# cells now have weights and we want to choose the path with the minimal weight. The keyword "minimal" and the grid
# is a good sign to use dynamic programming.
#
# The equivalent of "only able to move right or down" is "can only reach a cell from top or left". Since top and left
# are the only two ways to reach a cell, the minimal path sum to reach a cell is the minimum sum of top and left +
# value of the current cell.
#
# Let dp[r][c] represent the minimal path sum to reach cell (r, c).
#
# dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
#
# where dp[r - 1][c] is the minimal path sum to reach the cell at the top of the current cell and dp[r][c - 1] is the
# minimal path sum to reach the cell to the left of the current cell
#
# We fill the dp matrix row by row from left to right.
#
# Time Complexity: O(m*n)
