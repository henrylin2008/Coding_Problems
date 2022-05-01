# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Eazy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
#
#
# Follow up: Could you minimize the total number of operations done?
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time: O(n); loop through the list of nums
        # Space: O(1); using 2 pointers and in-place swap
        # note: use 2 pointers (l,r), both start at index 0, move the right pointer, if it's a non-zero value, swap the
        # values at the 2 pointers, then increment the left pointer, return nums
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums
