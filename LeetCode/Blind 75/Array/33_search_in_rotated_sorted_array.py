# 33. Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
#
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (
# 0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in
# nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
# *1 <= nums.length <= 5000
# *-104 <= nums[i] <= 104
# *All values of nums are unique.
# *nums is an ascending array that is possibly rotated.
# *-104 <= target <= 104

# Note: at most two sorted halfs, mid will be apart of left sorted or right sorted, if target is in range of sorted
# portion then search it, otherwise search other half

# Time: O(log n); binary search
# Space: O(1)
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1     # left, right pointer

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:  # search right portion; mid < target < nums[l]
                    l = mid + 1
                else:       # left < target < mid
                    r = mid - 1

            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:  # nums[r] < target < mid
                    r = mid - 1
                else:   # mid < target < r
                    l = mid + 1
        return -1
