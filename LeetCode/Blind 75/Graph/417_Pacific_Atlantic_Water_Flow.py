# 417. Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
# touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[
# r][c] represents the height above sea level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east,
# and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from
# any cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (
# ri, ci) to both the Pacific and Atlantic oceans.
#
#
#
# Example 1:
#   1   |   2   |   2   |   3   |   5   |
#   3   |   2   |   3   |   4   |   4   |
#   2   |   4   |   5   |   3   |   1   |
#   6   |   7   |   1   |   4   |   5   |
#   5   |   1   |   1   |   2   |   4   |
#
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Example 2:
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
# Constraints:
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

# Note: dfs each cell, keep track of visited, and track which reach pac, atl; dfs on cells adjacent to pac, atl,
# find overlap of cells that are visited by both pac and atl cells;

# Note: starting from first row/col and last row/col, run dfs on its adjacent cells (into the center), use 2 hashsets to
# keep track of the visited cells that can reach Pacific/Atlantic respectively; if cell is in the visited set, or out of
# bounds, or the height of current cell < the height of previous cell (water flows from high (in) to low (out)), then
# skip; else add the cell to the visited set. result would be any intersect cells (in a list).
from typing import List


# Time: O(n*m); n: rows, m: columns
# Space: O(n*m)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()            # hashset that can reach either Pacific or Atlantic ocean

        def dfs(row, col, visit, prev_height):  # (row, column, visit_set, previous_height)
            # going from ocean into the cells
            if ((row, col) in visit or  # if row, column already in visit set, then skip
                    row < 0 or col < 0 or row == rows or col == cols or  # if out of bounds
                    heights[row][col] < prev_height):  # water only flow if curr_height >= prev_height
                return
            visit.add((row, col))  # add it to the visit set
            dfs(row + 1, col, visit, heights[row][col])  # down neighbor
            dfs(row - 1, col, visit, heights[row][col])  # up neighbor
            dfs(row, col + 1, visit, heights[row][col])  # right neighbor
            dfs(row, col - 1, visit, heights[row][col])  # left neighbor

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])  # dfs on first row; (row, column, visit_set, prev_height); reach Pacific
            dfs(rows - 1, c, atl, heights[rows - 1][c])  # dfs on last row; reach Atlantic

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])  # dfs on first column; reach Pacific
            dfs(r, cols - 1, atl, heights[r][cols - 1])  # dfs on last column; reach Atlantic

        res = []
        for r in range(rows):  # every cell in the rows
            for c in range(cols):  # every cell in the columns
                if (r, c) in pac and (r, c) in atl:  # if the cell in both of pac set and atl set
                    res.append([r, c])  # add the cell to the result
        return res
