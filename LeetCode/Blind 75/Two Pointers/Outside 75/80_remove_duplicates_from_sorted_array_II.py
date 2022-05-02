# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Medium

# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique
# element appears at most twice. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you must instead have the result be
# placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first
# k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1)
# extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
#
# int k = removeDuplicates(nums); // Calls your implementation
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2,
# 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2,
# 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
from typing import List


class Solution:
    # Time: O(n); loop through the entire nums list
    # Space: O(1); using 2 pointers and in-place swaps
    # Note: using 2 pointers: left, and right, while looping through the nums, if right pointer not equal to value at
    # left - 2 (ensure last 2 values are the same), swap the values at the left pointer and the right pointer, and
    # increment the left pointer, then return left pointer
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) < 3:
            return len(nums)

        left = 2  # Pointer from where we need to replace elements
        for right in range(2, len(nums)):
            if nums[right] != nums[left - 2]:   # if right pointer != left pointer (left -2)
                nums[left] = nums[right]        # swap values at left and right pointer
                left += 1                       # increment left pointer
        return left                             # left pointer is the length for this problem
