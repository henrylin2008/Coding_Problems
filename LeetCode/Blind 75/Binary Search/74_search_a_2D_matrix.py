# 74. Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Medium

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has
# the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
#
# Example 1:
#   ----------------------------------
#   |    1   |   3   |   5   |   7   |
#   ----------------------------------
#   |   10   |   11  |   16  |   20  |
#   ----------------------------------
#   |   23   |   30  |   34  |   60  |
#   ----------------------------------
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
# Example 2:
#   ----------------------------------
#   |    1   |   3   |   5   |   7   |
#   ----------------------------------
#   |   10   |   11  |   16  |   20  |
#   ----------------------------------
#   |   23   |   30  |   34  |   60  |
#   ----------------------------------
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104
from typing import List


class Solution:
    # Time: O(log(m) + log(n)); double binary search: one for searching the row, one for searching with the row
    # Space: O(1); no data structure is being used
    # Solution: 2 binary searches; first binary search: narrow down which row the target is located; second binary
    #           search: if the target is the middle value, update left or right pointer accordingly
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # find out which row the target falls under
        top, bot = 0, ROWS - 1      # top, bottle rows
        while top <= bot:
            row = (top + bot) // 2      # middle row
            if target > matrix[row][-1]:    # target > rightmost value at the current row
                top = row + 1               # row > current row, shift left pointer
            elif target < matrix[row][0]:   # target < leftmost value at the current row
                bot = row - 1               # row < current row, shift right pointer
            else:       # target value falls in the current row
                break
        # if target not fall under any rows
        if not (top <= bot):    # if target not fall into any of the rows that have been checked so far, return False
            return False
        # run binary search on the current row
        row = (top + bot) // 2  # run binary search on the current row
        l, r = 0, COLS - 1      # left, right pointers
        while l <= r:
            m = (l + r) // 2    # middle point
            if target > matrix[row][m]:     # if target > middle value
                l = m + 1       # shift left pointer
            elif target < matrix[row][m]:   # if target < middle value
                r = m - 1       # shift right pointer
            else:           # found the target value, return True
                return True
        return False    # if nothing found after searching through the current row, return False
