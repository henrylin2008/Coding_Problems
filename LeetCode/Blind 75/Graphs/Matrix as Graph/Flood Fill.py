# Flood Fill
# https://algo.monster/problems/flood_fill

# In computer graphics, an uncompressed raster image is presented as a matrix of numbers. Each entry of the matrix
# represents the color of a pixel. A flood fill algorithm takes a coordinate r, c and a replacement color,
# and replaces all pixels connected to r, c that have the same color (i.e., the pixels connected to the given
# coordinate with of same color and all the other pixels connected to the those pixels of the same color) with the
# replacement color. (e.g. MS-Paint's paint bucket tool).
#
# Input
#   r: row
#   c: column
#   replacement: replacement color
#   image: an 2D array of integers representing the image
# Output
# the replaced image
#
# Examples
# Example 1:
# Input:
#   r = 2
#   c = 2
#   replacement = 9
#   arr = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
#
# Output: [[0,1,3,4,1],[3,9,9,3,3],[6,7,9,9,3],[12,2,9,9,1],[12,3,1,3,2]]
#
# Explanation:
# From
#   0 1 3 4 1
#   3 8 8 3 3
#   6 7 8 8 3
#   12 2 8 9 1
#   12 3 1 3 2
#
# to
#   0 1 3 4 1
#   3 9 9 3 3
#   6 7 9 9 3
#   12 2 9 9 1
#   12 3 1 3 2

# Solution
from collections import deque
from typing import List


def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:
    num_rows, num_cols = len(image), len(image[0])

    def get_neighbors(coord, color):
        row, col = coord
        delta_row = [-1, 0, 1, 0]
        delta_col = [0, 1, 0, -1]
        for i in range(len(delta_row)):
            neighbor_row = row + delta_row[i]
            neighbor_col = col + delta_col[i]
            if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                if image[neighbor_row][neighbor_col] == color:
                    yield neighbor_row, neighbor_col

    def bfs(root):
        queue = deque([root])
        visited = [[False for c in range(num_cols)] for r in range(num_rows)]
        r, c = root
        color = image[r][c]
        image[r][c] = replacement  # replace root color
        visited[r][c] = True
        while len(queue) > 0:
            node = queue.popleft()
            for neighbor in get_neighbors(node, color):
                r, c = neighbor
                if visited[r][c]:
                    continue
                image[r][c] = replacement  # replace color
                queue.append(neighbor)
                visited[r][c] = True

    bfs((r, c))
    return image
