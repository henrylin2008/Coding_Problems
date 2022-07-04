# Find Minimum in Rotated Sorted Array
# link: https://algo.monster/problems/min_in_rotated_sorted_array

# A sorted array of unique integers was rotated at an unknown pivot. For example, [10, 20, 30, 40, 50] becomes [30,
# 40, 50, 10, 20]. Find the index of the minimum element in this array. All the numbers are unique.
#
# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: the smallest element is 10 and its index is 3.
#
# Input: [3, 5, 7, 11, 13, 17, 19, 2]
# Output: 7
# Explanation: the smallest element is 2 and its index is 7.

from typing import List


def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[-1]:     # if <= last element, then belongs to lower half
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
