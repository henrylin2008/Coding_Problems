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

# Alternatively, we could use quick select for this particular problem. Worst case scenario, it runs on O(n^2),
# but on average, it runs on O(n).
#
# Quick select uses the principle of quick sort, only during each process, we only need to care about the middle
# point compared to k - 1 (because the question uses 1 indexing) and depending on the result, we either stop the
# program, recurse to the left side, or recurse to the right side.
#
# Note that it is easy to get the indices of Quick Select wrong, so in a real coding interview, it's often better to
# implement the heap solution and have less chance of error.
#
# Below is an implementation of Quick Select just for reference.
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    min_pointer = 0
    max_pointer = len(nums) - 1
    while min_pointer < max_pointer:
        pivot = nums[max_pointer]
        swap_left = min_pointer
        swap_right = max_pointer
        while swap_left < swap_right:
            while swap_left < swap_right and nums[swap_left] > pivot:
                swap_left += 1
            while swap_left < swap_right and nums[swap_right] <= pivot:
                swap_right -= 1
            if swap_left < swap_right:
                nums[swap_left], nums[swap_right] = nums[swap_right], nums[swap_left]
        nums[swap_left], nums[max_pointer] = nums[max_pointer], nums[swap_left]
        if swap_left == k - 1:
            return nums[swap_left]
        elif swap_left < k - 1:
            min_pointer = swap_left + 1
        else:
            max_pointer = swap_left - 1
    return nums[min_pointer]


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = find_kth_largest(nums, k)
    print(res)
