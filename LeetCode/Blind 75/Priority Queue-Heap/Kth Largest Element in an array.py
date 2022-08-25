# Kth Largest Element in an Array
# https://algo.monster/problems/kth_largest_element_in_an_array

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
# not necessarily the kth distinct element.
#
# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# Solution
#
# Sorting the array before indexing works fine, but below is a solution that uses a max heap. Heapify is O(n) and
# popping the first k element is O(klog(n)) so combined is O(n + klog(n)).

from heapq import heapify, heappop
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    # max heap
    nums = [-x for x in nums]
    heapify(nums)
    for _ in range(k - 1):
        heappop(nums)
    return -nums[0]


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
