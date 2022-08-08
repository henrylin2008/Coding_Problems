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


# Getting neighboring node's coordinates
# The core of BFS/DFS is to add neighbors of the current vertex to a queue/stack. The get_neighbors function returns all
# 4 (or 8 if you are allowed to go diagonal) coordinates of neighboring nodes.

#      -------------------------------------
#      |           |   r-1, c  |           |
#      -------------------------------------
#      |  r, c-1   |   r, c    |   r, c+1  |
#      -------------------------------------
#      |           |   r+1, c  |           |
#      -------------------------------------

# One way to get each neighbor's coordinates is to keep each neighbor's horizontal and vertical offsets (i.e. delta) in
# a list and adding them to each vertex's coordinates.

#  delta_row
#      -------------------------------------
#  -1  |           |   r - 1   |           |
#      -------------------------------------
#   0  |   r + 0   |     r     |   r + 0   |
#      -------------------------------------
#   1  |           |   r + 1   |           |
#      -------------------------------------

# delta_col
#           -1          0           1
#      -------------------------------------
#      |           |   c + 0   |           |
#      -------------------------------------
#      |   c - 1   |     c     |   c + 1   |
#      -------------------------------------
#      |           |   c + 0   |           |
#      -------------------------------------

# Starting from north, clockwise
#      delta_row = [-1, 0, 1, 0]
#      delta_col = [0, 1, 0, -1]


# BFS template

num_rows, num_cols = len(grid), len(grid[0])


def get_neighbors(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res


from collections import deque


def bfs(starting_node):
    queue = deque([starting_node])
    visited = set([starting_node])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            # Do stuff with the node if required
            # ...
            queue.append(neighbor)
            visited.add(neighbor)
