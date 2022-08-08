# Matrix as Graph
# https://algo.monster/problems/matrix_as_graph

# A matrix translates to a graph (adjacency list):
#   0   |   1   |   2   |
#   3   |   4   |   5   |
#   6   |   7   |   8   |
#           ||
#           ||
#           vv

# { 0: [1, 3],
#   1: [0, 2, 4],
#   2: [1, 5],
#   3: [0, 4, 6],
#   4: [1, 3, 5, 7],
#   5: [2, 4, 8],
#   6: [3, 7],
#   7: [4, 6, 8],
#   8: [5, 7]
#   }
#
# When we code the problem, we have to build the graph as we go. Nodes/vertices are represented by coordinates of matrix
# entries.

#           0           1          2
#      -----------------------------------
#   0  |   0,0     |    0,1    |   0,2   |
#      -----------------------------------
#   1  |   1,0     |    1,1    |   1,2   |
#      -----------------------------------
#   2  |   2,0     |    2,1    |   2,2   |
#      -----------------------------------