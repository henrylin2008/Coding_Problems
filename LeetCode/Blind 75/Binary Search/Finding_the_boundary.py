# Finding the Boundary with Binary Search
# https://algo.monster/problems/binary_search_boundary

# An array of boolean values is divided into two sections; the left section consists of all false and the right
# section consists of all true. Find the boundary of the right section, i.e. the index of the first true element. If
# there is no true element, return -1.
#
# Input: arr = [false, false, true, true, true]
#
# Output: 2
#
# Explanation: first true's index is 2.

from typing import List


def find_boundary(arr: List[bool]) -> int:
    l, r = 0, len(arr) - 1
    boundary = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid]:
            boundary = mid
            r = mid - 1
        else:
            l = mid + 1

    return boundary


if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)


# Input:
# test #1: false false true true true
# test #2: true
# test #3: false false false
# test #4: true true true true true
# test #5: false true
