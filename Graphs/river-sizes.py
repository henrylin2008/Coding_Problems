# https://www.algoexpert.io/questions/River%20Sizes
# River Sizes
# Difficulty: Medium

# You're given a two-dimensional array(a matrix) of potentially unequal height and width containing only 0s and 1s. Each
# 0 represents land, and each 1 represents part of a river. A river consists of any number of 1s that are either
# horizontally or vertically adjacent(but not diagonally adjacent). The number of adjacent 1s forming a river determine
# its size.
# Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal
# line; it can be L-shaped, for example.
# Write a function that returns an array of the sizes of all rivers represented in the input matrix. The size don't need
# to be in any particular order.

# Sample Input:
# matrix = [
#   [1, 0, 0, 1, 0],
#   [1, 0, 1, 0, 0],
#   [0, 0, 1, 0, 1],
#   [1, 0, 1, 0, 1],
#   [1, 0, 1, 1, 0],
# ]

# Sample Output:
# [1, 2, 2, 2, 5]   // The numbers could be ordered differently.
#
# // The rivers can be clearly seen here:
# // [
# //    [1,  ,  , 1,  ],
# //    [1,  , 1,  ,  ],
# //    [ ,  , 1,  , 1],
# //    [1,  , 1,  , 1],
# //    [1,  , 1, 1,  ],
# // ]