# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/
# Medium

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The
# robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
# right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
# bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.
#
#
# Example 1:
# Input: m = 3, n = 7
# Output: 28
#
# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Note: work backwards from solution, store paths for each position in grid, to further optimize, we don’t store
# whole grid, only need to store prev row;

# Ex1: m = 3, n = 7
# starting from the end, and backtracking to the starting point
# start 28 | 21 (15+6) | 15 (10+5) | 10 (6+4) | 6 (3+3) | 3 (2+1) |   1   |   0
#  7 (6+1) | 6 (5+1)   | 5 (4+1)   | 4 (3+1)  | 3 (2+1) | 2 (1+1) |   1   |   0
#  1 ->    |  1 ->     |  1 ->     |  1 ->    |  1 ->   |  1 ->   | end 1 |   0
#   0          0           0           0          0         0

class Solution:
    # Time: O(n * m)
    # Space: O(n); length of the row
    def uniquePaths(self, m: int, n: int) -> int:       # m: columns, n: rows
        row = [1] * n  # bottom row
        for i in range(m - 1):  # loop through all other rows except the last row
            new_row = [1] * n  # row above the bottom row
            for j in range(n - 2, -1, -1):  # loop from 2nd to (right) last column to the left, last column are all 1s
                new_row[j] = new_row[j + 1] + row[j]  # current cell = right cell + bottom cell
            row = new_row  # update old row to the new row
        return row[0]
