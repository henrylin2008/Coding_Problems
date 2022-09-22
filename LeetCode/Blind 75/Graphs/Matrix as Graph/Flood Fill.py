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
