# First Element Not Smaller Than Target
# Link: https://algo.monster/problems/binary_search_first_element_not_smaller_than_target

# Given an array of integers sorted in increasing order and a target, find the index of the first element in the
# array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.
#
# Input:
#   arr = [1, 3, 3, 5, 8, 8, 10]
#   target = 2
# Output: 1
# Explanation: the first element larger than 2 is 3 which has index 1.
#
# Input:
#   arr = [2, 3, 5, 7, 11, 13, 17, 19]
#   target = 6
# Output: 3
# Explanation: the first element larger than 6 is 7 which has index 3.

from typing import List


# Time Complexity: O(log(n))
# The problem is equivalent to finding the boundary of elements < 3 and elements >=3. Now the problem is reduced to
# finding the first true element in a boolean array.

def first_not_smaller(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    boundary = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] >= target:
            boundary = mid
            r = mid - 1
        else:
            l = mid + 1
    return boundary


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
