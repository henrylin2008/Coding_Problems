# 200. Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of
# islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
import collections
from typing import List


# Time: O(v + e); v: vertices; e: edges
# Space: O(v + e); v: vertices; e: edges
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()       # visited nodes
        islands = 0         # count of islands

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))       # mark this position as visited
            q.append((r, c))        # add it to the q

            while q:        # q not empty
                row, col = q.popleft()      # pop left most left item in the q
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # [[right], [left], [above], [below]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and        # if r, c in bound, land ("1"), and not been visited
                            c in range(cols) and
                            grid[r][c] == "1" and
                            (r, c) not in visit):
                        q.append((r, c))        # add node to the q, needs to run bfs
                        visit.add((r, c))       # mark it as visited

        # visit every cell
        for r in range(rows):       # every row
            for c in range(cols):   # every col
                if grid[r][c] == "1" and (r, c) not in visit:   # if node is "1" and not in the visit set
                    bfs(r, c)       # bfs on current node
                    islands += 1    # increment island if the island has not been visited
        return islands

