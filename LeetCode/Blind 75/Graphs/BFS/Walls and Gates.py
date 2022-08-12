# Walls and Gates / Zombie in Matrix
# https://algo.monster/problems/walls_and_gates

# ou are given an m by n grid of integers representing a map of a dungeon. In this map:
#   *-1 represents a wall or an obstacle of some kind.
#   *0 represents a gate out of the dungeon.
#   *INF represents empty space.
#
# For this question, let INF be 2^31 - 1 == 2147483647, which is the max value of the integer type in many programming
# languages.
#
# Venturing into the dungeon is very dangerous, so you would like to know how close you are at each point in the
# dungeon to the exit. Given the map of the dungeon, return the same map, but for each empty space, that space is
# replaced by the number of steps it takes to reach any exit. If a space cannot reach the exit, that space remains INF.
#
# Note that each step, you can move horizontally or vertically, but you cannot move pass a wall or an obstacle.
#
# Input
# dungeon_map: a matrix of integer representing the dungeon map.
# Output
# A matrix of integer representing the dungeon map with the addition of distance to an exit for each empty space.
#
# Examples
# Example 1:
# Input:
# dungeon_map = [
#   [INF, -1, 0, INF],
#   [INF, INF, INF, -1],
#   [INF, -1, INF, -1],
#   [0, -1, INF, INF],
# ]
# Output: [ [3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4], ]
#
# Explanation:
#
# Constraints
# 1 <= n, m <= 500

# Solution
# This is a classical breadth-first search problem, as it asks for the distance from each point to some location.
# Simply initialize the queue with a list of gate locations, and each cycle, when we process the location at the
# front of the queue, we add all the adjacent locations into the queue if their value is INF (meaning it is empty and
# unprocessed) and mark the distances on the cells by adding the value of the current cell by 1. This way each empty
# space is only in the queue once.
#
# The time complexity is O(n * m).

from collections import deque
from typing import List

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INF = 2147483647


def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    queue = deque()
    n = len(dungeon_map)
    m = len(dungeon_map[0])
    for i, row in enumerate(dungeon_map):
        for j, entry in enumerate(row):
            if entry == 0:
                queue.append((i, j))
    while queue:
        row, col = queue.popleft()
        for delta_row, delta_col in directions:
            total_row, total_col = row + delta_row, col + delta_col
            if 0 <= total_row < n and 0 <= total_col < m:
                if dungeon_map[total_row][total_col] == INF:
                    dungeon_map[total_row][total_col] = dungeon_map[row][col] + 1
                    queue.append((total_row, total_col))
    return dungeon_map


if __name__ == '__main__':
    dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(' '.join(map(str, row)))
