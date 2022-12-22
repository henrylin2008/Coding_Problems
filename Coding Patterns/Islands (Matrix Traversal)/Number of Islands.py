# Number of Islands (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1654828199398_262Unit

# Problem Statement
#
# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.
# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is
# considered connected to other cells horizontally or vertically (not diagonally).
#
# Example 1
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
# Output: 1
# Explanation: The matrix has only one island. See the highlighted cells below.
#      -------------------------------
#      |  0  |  1*  | 1* |  1* |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  1* |  1* |
#      -------------------------------
#      |  0  |  1* |  1* |  1* |  0  |
#      -------------------------------
#      |  0  |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  0  |  0  |  0  |

# Example 2
#
# Input: matrix =
#      -------------------------------
#      |  1  |  1  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  1  |  0  |  0  |  1  |
#      -------------------------------
#      |  0  |  0  |  1  |  1  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1  |  0  |  0  |
#
# Output: 3
# Explanation: The matrix has three islands. See the highlighted cells below.
#      -------------------------------
#      |  1* |  1* |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  1* |  0  |  0  |  1* |
#      -------------------------------
#      |  0  |  0  |  1* |  1* |  0  |
#      -------------------------------
#      |  0  |  0  |  1* |  0  |  0  |
#      -------------------------------
#      |  0  |  0  |  1*  |  0  |  0  |

# Solution
#
# We can traverse the matrix linearly to find islands.
#
# Whenever we find a cell with the value '1' (i.e., land), we have found an island. Using that cell as the root node,
# we will perform a Depth First Search (DFS) or Breadth First Search (BFS) to find all of its connected land cells.
# During our DFS or BFS traversal, we will find and mark all the horizontally and vertically connected land cells.
#
# We need to have a mechanism to mark each land cell to ensure that each land cell is visited only once. To mark a
# cell visited, we have two options:
#   1. We can update the given input matrix. Whenever we see a '1', we will make it '0'.
#   2. A separate boolean matrix can be used to record whether or not each cell has been visited.

# Following is the DFS or BFS traversal of the example-2 mentioned above:

# By following the above algorithm, every time DFS or BFS is triggered, we are sure that we have found an island. We
# will keep a running count to calculate the total number of islands.
#
# Bellow, we will see three solutions based on:
#   1. DFS
#   2. BFS
#   3. BFS with visited matrix
