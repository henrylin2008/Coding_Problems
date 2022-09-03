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
