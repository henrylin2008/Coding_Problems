# K Closest Points
# https://algo.monster/problems/k_closest_points

# Given a list of points on a 2D plane. Find k closest points to origin (0, 0).
#
# Input: [(1, 1), (2, 2), (3, 3)], 1
#
# Output: [(1, 1)]


# Explanation
# Intuition
# First off, some elementary geometry if you don't remember. Distance between two points (x1, y1) and (x2,
# y2) is sqrt((x1 - x2)^2, (y1 - y2)^2). For distance to origin, (x2, y2) is (0, 0) so distance becomes sqrt(x1^2,
# y1^2).
#
# Having just learned the "art of the heap", our first reaction when we see "Closest k" is to use a heap. The key for
# node comparison is a node's distance to origin. We then pop the top 3 smallest off. So simple we don't even have to
# draw a figure this time.
#
# Time Complexity: O(n*log(n))
#
# We add every element into the heap. Heap insertion is O(log(n)) which we do n times.

from heapq import heappop, heappush
from math import sqrt
from typing import List


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []

    for pt in points:
        heappush(heap, (sqrt(pt[0] ** 2 + pt[1] ** 2), pt))

    res = []
    for _ in range(k):
        _, pt = heappop(heap)
        res.append(pt)

    return res


if __name__ == '__main__':
    points = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = k_closest_points(points, k)
    for row in res:
        print(' '.join(map(str, row)))


# Alternative solution using max heap

# It might be counter-intuitive to think that a max heap can solve a problem that asks for minimum distances. Here's
# how to think about it:
#
# If we had the k closest points already and we have to decide whether a new point belongs to top k. The criterion is
# whether the new point is closer than the furthermost point within the current k points. If it is, we want to kick
# the current furthermost point out and add the new point.
#
# We can use a max heap to accomplish this. The root of the max heap is the point with max distance to the origin. If
# the new point has a smaller distance, then we pop the root of the max heap and push the new point in.
