# Shortest Path Between A and B
# https://algo.monster/problems/shortest_path_unweight

# Given an (unweighted) graph, return the length of the shortest path between two nodes A and B, in terms of the number
# of edges.
#
# Input:
# graph: {
#   0: [1, 2],
#   1: [0, 2, 3],
#   2: [0, 1],
#   3: [1]
# }
# A: 0
# B: 3
#
# Output: 2

#                   A
#                   0
#               /       \
#             1    ---    2
#           /
#        B 3



from collections import deque
from typing import List


def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    def get_neighbors(node: int):
        return graph[node]

    # BFS template
    def bfs(root: int, target: int):
        queue = deque([root])
        visited = set([root])
        level = 0
        while len(queue) > 0:
            n = len(queue)
            for n in range(n):
                node = queue.popleft()
                if node == target:
                    return level
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    visited.add(neighbor)
            level += 1

    return bfs(a, b)


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)
