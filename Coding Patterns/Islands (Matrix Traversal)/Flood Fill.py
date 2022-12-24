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
