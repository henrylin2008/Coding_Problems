# Flood Fill (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d52d75d7964Unit

# Problem Statement
#
# Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of
# the image.
#
# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all
# horizontally and vertically connected cells with the same color as that of the starting cell. Recursively,
# the algorithm fills cells with the new color until it encounters a cell with a different color than the starting
# cell.
#
# Given a matrix, a starting cell, and a color, flood fill the matrix.
#
# Example 1
#
# Input: matrix =
#      -------------------------------
#      |  0  |  1  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  1  |  1  |
#      -------------------------------
#      |  0  |  1  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      starting cell = (1, 3)
#      new color = 2

# Output:
#      -------------------------------
#      |  0  |  2  |  2  |  2  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  2  |  2  |
#      -------------------------------
#      |  0  |  2  |  2  |  2  |  0  |
#      -------------------------------
#      |  0  |  2  |  2  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------

# Example 2
#
# Input: matrix =
##      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#      -------------------------------
#      starting cell = (3, 2)
#      new color = 5
# Output:
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  5  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  0  |  0  |
#      -------------------------------

# Solution
#
# The question follows the Island pattern and is quite similar to Number of Islands problem.
#
# From the given starting cell, we can perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all
# of its connected cells with the same color. During our DFS or BFS traversal, we will update the cells with the new
# color.
#
# Following is the DFS or BFS traversal of the example-2 mentioned above:
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  5  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  5  |  0  |  0  |
#      -------------------------------


# Code  (DFS)
#
# Here is what our DFS algorithm will look like:
def floodFill(matrix, x, y, newColor):
    if matrix[x][y] != newColor:
        fillDFS(matrix, x, y, matrix[x][y], newColor)
    return matrix


def fillDFS(matrix,  x,  y, oldColor, newColor):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return  # return, if it is not a valid cell
    if matrix[x][y] != oldColor:
        return  # return, if it is not the required color

    matrix[x][y] = newColor  # // update the cell to the new color

    # recursively visit all neighboring cells (horizontally & vertically)
    fillDFS(matrix, x + 1, y, oldColor, newColor)  # lower cell
    fillDFS(matrix, x - 1, y, oldColor, newColor)  # upper cell
    fillDFS(matrix, x, y + 1, oldColor, newColor)  # right cell
    fillDFS(matrix, x, y - 1, oldColor, newColor)  # left cell


def main():
    print(floodFill([[0, 1, 1, 1, 0], [0, 0, 0, 1, 1], [
          0, 1, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]], 1, 3, 2))
    print(floodFill([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [
          0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]], 3, 2, 5))


main()