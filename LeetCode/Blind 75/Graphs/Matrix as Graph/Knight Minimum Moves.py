# Knight Minimum Moves
# https://algo.monster/problems/knight_shortest_path

# On an infinitely large chessboard, a knight is located on [0, 0].
#
# A knight can move in eight directions.

# Given a destination coordinate [x, y], determine the minimum number of moves from [0, 0] to [x, y].

# Explanation
# Intuition
# The problem asks for the minimum moves so BFS is our choice here. The chessboard being infinite is totally fine
# with BFS since we build the graph as we go.
#
# The get_neighbors function now returns cells in 8 directions.

# And since the chessboard is infinite, we no longer have to worry about bound checking.
#
# Time Complexity: O(r*c)
#
# The computational time is equal to the size of the grid which is r*c in the worst case. Edges in the graph are
# constant at 8 since the knight can move at most to 8 squares from a given cell.

def get_neighbors(coord):
    res = []
    row, col = coord
    delta_row = [-2, -2, -1, 1, 2, 2, 1, -1]
    delta_col = [-1, 1, 2, 2, 1, -1, -2, -2]
    for i in range(len(delta_row)):
        r = row + delta_row[i]
        c = col + delta_col[i]
        res.append((r, c))
    return res