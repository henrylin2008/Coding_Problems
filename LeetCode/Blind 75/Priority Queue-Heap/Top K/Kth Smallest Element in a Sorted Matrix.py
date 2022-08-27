# Kth Smallest Element in a Sorted Matrix
# https://algo.monster/problems/kth_smallest_element_in_a_sorted_matrix

# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element
# in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
# Input:
# matrix = [
#   [ 1,  5,  9],
#   [10, 11, 13],
#   [12, 13, 15]
# ],
# k = 8,
# Output: 13
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n^2. You may also assume that 1 <= n <= 1000.

# Solution
# Brute Force
# A brute force solution would traverse the matrix entirely and insert each element into some type of container (
# array, vector, etc). We then sort the container and index kth element.
#
# The time complexity for this solution would be O((n^2) log(n^2)) because there are a total of n * n = n^2 elements,
# and sorting takes O(N log(N)) in general.
#
# Min Heap
# The brute force solution above is sufficient for the bounds of this problem where n <= 1000. However,
# we can do better by making use of the fact that each row is sorted. The idea is to use to keep a pointer on each
# row. We will move a pointer when said pointer is pointing to the smallest element out of every pointer.
#

# The idea is simple, but how do we efficiently check which pointer is pointing at the smallest element? We can use a
# min heap! However, we can't just store the values themselves, because otherwise we would lose which row the values
# correspond too. We also can't store a value and row pair because then we would lose which column each pointer
# corresponds to per row. So we will store a value, row, and column tuple.

# Note that we only update k once we have popped the top element of the min heap. This helps simplify implementation
# details. Furthermore, once a pointer cannot move anymore (i.e. it has reach the N - 1th column), we remove it
# completely.
#
# For this specific implementation below, the time complexity is O(N + K log(N)) since it takes O(N) to process the
# first row and each of the k iterations take O(log(N)) to process due to the use of the min heap.

from heapq import heappop, heappush
from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    # Keeps track of items in the heap, and their row and column numbers
    heap = [(matrix[0][0], 0, 0)]
    # Keeps track of the top of each row that is not processed
    column_top = [0] * n
    # Keeps track of the first number each row not processed
    row_first = [0] * n
    # Repeat the process k - 1 times.
    while k > 1:
        k -= 1
        min_val, row, column = heappop(heap)
        row_first[row] = column + 1
        # Add the item on the right to the heap if everything above it is processed
        if column + 1 < n and column_top[column + 1] == row:
            heappush(heap, (matrix[row][column + 1], row, column + 1))
        column_top[column] = row + 1
        # Add the item below it to the heap if everything before it is processed
        if row + 1 < n and row_first[row + 1] == column:
            heappush(heap, (matrix[row + 1][column], row + 1, column))
    return heap[0][0]


if __name__ == '__main__':
    matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    k = int(input())
    res = kth_smallest(matrix, k)
    print(res)
