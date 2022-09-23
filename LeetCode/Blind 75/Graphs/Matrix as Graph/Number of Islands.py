# Find the Number of Islands
# https://algo.monster/problems/number_of_islands

# Given a 2-dimensional matrix of values with 0 and 1, count the number of islands of 1. An island consists of all
# value 1 cells and is surrounded by either an edge or all 0 cells. A cell can only be adjacent to each other
# horizontally or vertically, not diagonally.

# Explanation
# Intuition
# The 2D grid (matrix) is a graph as discussed in the matrix as graph module. To find an island, we can do BFS/DFS on
# a node and expand our search if the neighboring cell is also 1, like how we find cells with the same color in Flood
# Fill.
#
# However, since there might be multiple islands, we have to do flood fill on every cell. Wouldn't that blow up the
# time complexity though? Remember that we store the visited cells, and we can skip cells that have already been
# visited. So overall, each cell is visited only once.
#
# Applying the BFS for matrix graph template:
#
# Time Complexity: O(r*c)
#
# Similar to before, the time complexity is equal to the size of the matrix itself in the worst case. The size of the
# matrix is denoted by the number of rows times the number of columns so therefore we have r*c nodes in our graph.
# The number of edges for a given cell is 4 (except boundary cells whose edges are < 4). And constants are dropped in
# the time complexity notation.

from collections import deque
from typing import List


def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coord):
        res = []
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            r = row + delta_row[i]
            c = col + delta_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))
        return res

    def bfs(start):
        queue = deque([start])
        r, c = start
        grid[r][c] = 0
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                r, c = neighbor
                if grid[r][c] == 0:
                    continue
                queue.append(neighbor)
                grid[r][c] = 0

    count = 0
    # bfs starting from each unvisited land cell
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == 0:
                continue
            bfs((r, c))
            count += 1  # bfs would find 1 connected island, increment count
    return count


if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
