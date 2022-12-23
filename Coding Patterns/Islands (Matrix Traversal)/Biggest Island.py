# Biggest Island (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_62d53be009288Unit

# Problem Statement
#
# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a
# function to return the area of the biggest island.
#
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is
# considered connected to other cells horizontally or vertically (not diagonally).
#
# Example 1
# Input: matrix =
#      -------------------------------
#      |  1  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  1  |  0  |  0  |  1  |
#      -------------------------------
#      |  0  |  0  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#
#
# Output: 5
# Explanation: The matrix has three islands. The biggest island has 5 cells .
#      -------------------------------
#      |  1* |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  1* |  0  |  0  |  1* |
#      -------------------------------
#      |  0  |  0  |  1* |  1* |  0  |
#      -------------------------------
#      |  0  |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1* |  0  |  0  |
#
# Solution
#
# The question follows the Island pattern and is quite similar to Number of Islands problem.
#
# We will traverse the matrix linearly to find islands.
#
# Whenever we find a cell with the value '1' (i.e., land), we have found an island. Using that cell as the root node,
# we will perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected land cells.
# During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells.
#
# We will keep a variable to remember the max area of any island.

# Code  (DFS)
#
# Here is what our DFS algorithm will look like. We will update the input matrix to mark nodes visited.
def maxAreaIslandDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggestIslandArea = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:  # only if the cell is a land
                # we have found an island
                biggestIslandArea = max(
                    biggestIslandArea, visitIslandDFS(matrix, i, j))

    return biggestIslandArea


def visitIslandDFS(matrix,  x,  y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return 0  # return, if it is not a valid cell
    if matrix[x][y] == 0:
        return 0  # return, if it is a water cell

    matrix[x][y] = 0  # mark the cell visited by making it a water cell

    area = 1 # counting the current cell
    # recursively visit all neighboring cells (horizontally & vertically)
    area += visitIslandDFS(matrix, x + 1, y)  # lower cell
    area += visitIslandDFS(matrix, x - 1, y)  # upper cell
    area += visitIslandDFS(matrix, x, y + 1)  # right cell
    area += visitIslandDFS(matrix, x, y - 1)  # left cell
    return area


def main():
    print(maxAreaIslandDFS([[1, 1, 1, 0, 0], [0, 1, 0, 0, 1], [
          0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 1, 0, 0]]))


main()

# Time Complexity
# Time complexity of the above algorithm will be O(M*N), where ‘M’ is the number of rows and 'N' is the number of
# columns of the input matrix. This is due to the fact that we have to traverse the whole matrix to find islands.

# Space Complexity
# DFS recursion stack can go M*N deep when the whole matrix is filled with '1's. Hence, the space complexity will be
# O(M*N), where ‘M’ is the number of rows and 'N' is the number of columns of the input matrix.
