# Triangle
# https://algo.monster/problems/triangle

# The problem is to find the minimum path sum from top to bottom if given a triangle. Each step you may move to
# adjacent numbers on the row below.
#
# Input
#   triangle: see example
# Output
# the minimum path sum
#
# Examples
# Example 1:
# Input:
# triangle = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
# Output: 11
#
# Explanation:
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

# Solution
# The trickiest part of this part is understanding the indexing and which ones correspond to traversing the left
# branch or the right branch.
#
# Once you finish playing around with the examples given to you, you might notice that for any "node" at position
# triangle[i][j], the left branch is triangle[i+1][j] and the right branch is triangle[i+1][j+1].

# Brute Force
# A brute force enumerates through all possibilities such that at each step we try the left branch and right branch,
# then figuring out which branch gives us the minimum sum. This can be done with a recursive combinatorial search
# with a time complexity of O(2^n).
#
# Here is an illustration of this idea as a state-space tree:
def min_path_sum(triangle, row, col):
    if row == len(triangle):
        return 0

    left_sum = min_path_sum(triangle, row + 1, col)
    right_sum = min_path_sum(triangle, row + 1, col + 1)
    return triangle[row][col] + min(left_sum, right_sum)


def minimum_total(triangle):
    return min_path_sum(triangle, 0, 0)


# The runtime is O(2^n) since for each state we have two choices -- go left or go right. The space complexity is O(n)
# since we have at most O(n) function calls in the memory stack at any given time.


# DFS + Memoization
# The idea of memoization for this problem comes from the idea that for certain values in triangle, it may be useful
# for more than one future computation. For example, in the following diagram we see that the nodes labelled A and B
# depend on node C. Thus, both node A and node B depend on node C. So, instead of recomputing the value corresponding
# to node C every time, we can store our result for node C in a memo table.
#
# Since each node can be uniquely identified based on their row and column value, memo will be a 2D array where memo[
# row][col] represents the minimum path sum up to the node corresponding

from functools import lru_cache
from math import inf
from typing import List


# The runtime is O(n^2) since there are O(n^2) states and each state takes O(1) to compute. The space complexity is
# O(n^2) too due to the use of the n by n memo table.
def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)

    @lru_cache(None)
    def dfs(i, level):
        if level == n:
            return 0

        best = inf
        next_level = level + 1
        for nexti in [i, i + 1]:
            if 0 <= nexti <= next_level:
                best = min(best, dfs(nexti, next_level))

        return best + triangle[level][i]

    return dfs(0, 0)


if __name__ == '__main__':
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)


# Bottom-up
# Alternatively, you can use a bottom-up approach. Again, the idea of bottom-up is to build our solution from the
# smallest solutions up to the one we want. So, we can start from the last row and build our way up to the first row.
# Our state and transition remains the same.
#   -State: dp[r][c] is the minimum path sum starting from r-th row and c-th column.
#   -Transition: dp[r][c] = min(dp[r-1][c], dp[r-1][c-1]) + triangle[r][c]

def minimum_total(triangle: List[List[int]]) -> int:
    n = len(triangle)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(0, n):  # first deal with last row
        dp[n - 1][i] = triangle[n - 1][i]

    for i in range(n - 2, -1, -1):  # start from second last row and build up to (0, 0)
        for j in range(0, i + 1):
            dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

    return dp[0][0]
