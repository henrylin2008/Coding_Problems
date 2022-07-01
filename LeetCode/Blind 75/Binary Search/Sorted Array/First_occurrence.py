# Find Element in Sorted Array with Duplicates
# https://algo.monster/problems/binary_search_duplicates

# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its
# index. Return -1 if the target is not in the array.
#
# Input:
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
#
# Output: 1
# Explanation: First occurrence of 3 is at index 1.
#
# Input:
# arr = [2, 3, 5, 7, 11, 13, 17, 19]
# target = 6
#
# Output: -1
# Explanation: 6 does not exists in the array.


from typing import List


# Time Complexity: O(log(n))
# The problem is equivalent to finding the boundary of elements < 3 and elements >= 3. Now the problem is reduced to
# finding the first true element in a boolean array.
def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            ans = mid       # update the answer if the current value == target, and shift the right pointer
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:       # need to shift the right pointer if current value (arr[mid]) > target
            r = mid - 1
    return ans


if __name__ == '__main__':
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)


# Test #1:
# Input
# 1 3 3 3 3 6 10 10 10 100
# 3
# Output
# 1

# Test #2:
# Input
# 1 1 1 1 1 1 1 1 1 1 1 1
# 1
# Output
# 0

# Test #3:
# Input
# 1 22 22 33 50 100 20000
# 33
# Output
# 3

# Test #4:
# Input
# 4 6 7 7 7 20
# 8
# Output
# -1


