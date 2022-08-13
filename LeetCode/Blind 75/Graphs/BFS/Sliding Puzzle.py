# Sliding Puzzle
# https://algo.monster/problems/sliding_puzzle

# You happen upon a puzzle box that unlocks... Something. You aren't quite sure what just yet. The puzzle is a 2 x 3
# box, and there are 5 square sliding bricks labelled conveniently with 1 to 5. It looks something like this:
#            -----------------------
#            |   4   |   1   |   3  |
#            -----------------------
#            |   2   |       |   5  |
#            -----------------------
#
#
# It can be represented as a 2 x 3 matrix containing numbers from 0 to 5, where 0 represents an empty space. For
# example, the pattern above can be represented by [[4, 1, 3], [2, 0, 5]].
#
# The tiles are interlocked with each other, so you cannot take the tiles out. However, the tiles can move freely
# horizontally and vertically, so each turn, you can move a tile to an adjacent empty space. You have a feeling that
# when you move the tiles to the position [[1, 2, 3], [4, 5, 0]], the puzzle will be solved and unlock the
# "something". Like this:
#             -----------------------
#            |   1   |   2   |   3  |
#            -----------------------
#            |   4   |   5   |      |
#            -----------------------
#
#
# You need to be quick about solving this puzzle, though, as you might attract the attention of someone who doesn't
# like you poking around in their dungeon. You wonder whether it is possible to solve this puzzle, and if so,
# how many steps you need to move in order to do so.
#
# Input
#   -init_pos: an integer matrix representing the initial position of the puzzle.
#
# Output
# The number of steps required to solve this puzzle, or -1 if the puzzle is impossible to solve.
#
# Examples
# Example 1:
# Input:
# init_pos = [[4, 1, 3], [2, 0, 5]]
# Output: 5
#
# Constraints
# The input must be a 2 x 3 integer matrix containing exactly one of each from 0 to 5

# Solution
# This is a straightforward BFS problem. However, the biggest difficulty in implementing a solution is finding the
# state adjacent to the current state and being able to store the different states in a hash table for lookup of
# items. The core idea is another state is adjacent to the current state when the entry with the 0 is swapped with
# one of the entries adjacent to it, which is very helpful if we use a mutable structure (like lists). On the other
# hand, we need to store the swapped value in a hash table and in a queue, which is very helpful if we use a hashable
# structure (like tuples), which are usually immutable. Other than that, it's just a standard BFS solution.
#
# A node transition graph might look like this:
#
#
#
# Which side a line comes out of represent which way the puzzle can move, and what happens when you move the puzzle
# that way. Note this graph is two-directional, as you can always move back to return to the original position.
#
# The time complexity is O(n!), where n is the size of the matrix in question. We usually would never reach the worst
# case scenario though.
#
# Below is an implementation.

from collections import deque
from typing import List

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

target = ((1, 2, 3), (4, 5, 0))


def num_steps(init_pos: List[List[int]]) -> int:
    init_pos = tuple(tuple(line) for line in init_pos)
    if init_pos == target:
        return 0
    moves_map = {init_pos: 0}
    moves_queue = deque([init_pos])
    while moves_queue:
        top = moves_queue.popleft()
        row, col = 0, 0
        for i, line in enumerate(top):
            for j, entry in enumerate(line):
                if entry == 0:
                    row, col = i, j
        for delta_row, delta_col in directions:
            new_row, new_col = row + delta_row, col + delta_col
            if 0 <= new_row < 2 and 0 <= new_col < 3:
                new_state = list(list(line) for line in top)
                new_state[new_row][new_col], new_state[row][col] = new_state[row][col], new_state[new_row][new_col]
                new_tuples = tuple(tuple(line) for line in new_state)
                if new_tuples not in moves_map:
                    moves_map[new_tuples] = moves_map[top] + 1
                    moves_queue.append(new_tuples)
                    if new_tuples == target:
                        return moves_map[new_tuples]
    return -1


if __name__ == '__main__':
    init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = num_steps(init_pos)
    print(res)
