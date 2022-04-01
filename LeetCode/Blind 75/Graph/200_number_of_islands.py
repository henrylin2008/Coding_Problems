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

# Note: for each cell, if it's == "1" and not visited, then run bfs and increment the islands; in bfs function, use a
# queue/deque to store info about the node, mark current cell as visited and add it to the queue, run a while on queue,
# as long as it's not empty, pop the leftmost node from the queue, then check on its adjacent nodes, if r, c within the
# range and is a land ("1") and it has not been visited, then add the node to the queue and visited set
#
# -visited set: keep track of visited nodes
# -Queue: keep track of adjacent nodes, and pop the leftmost node from the queue and add it to the visited set, and add
#        the new adjacent nodes to the back of the queue
#
# dfs algorithm:
# 1.Start by putting any one of the graph's vertices at the back of a queue.
# 2.Take the front item of the queue and add it to the visited list.
# 3.Create a list of that vertex's adjacent nodes. Add the ones which aren't in the visited list to the back of the
#   queue.
# 4. Keep repeating steps 2 and 3 until the queue is empty.
import collections
from typing import List


# Time: O(v + e); v: vertices; e: edges
# Space: O(v + e); v: vertices; e: edges
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()  # visited nodes
        islands = 0  # count of islands

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))  # mark this position as visited
            q.append((r, c))  # add it to the q

            while q:  # q not empty, expanding the island
                row, col = q.popleft()  # pop left most item from the q
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # adjacent nodes: [[right], [left], [above], [below]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # if r, c are inbound, current node is a land ("1"), and it has not been visited
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit:
                        q.append((r, c))  # add node to the q, and run bfs on this cell/node
                        visit.add((r, c))  # mark it as visited, avoid visit twice

        # visit every cell
        for r in range(rows):  # every row
            for c in range(cols):  # every col
                if grid[r][c] == "1" and (r, c) not in visit:  # if node is "1" and not in the visit set
                    bfs(r, c)  # bfs on current node
                    islands += 1  # increment island if the island has not been visited
        return islands
