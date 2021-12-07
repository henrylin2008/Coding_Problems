# Link: https://leetcode.com/problems/maximum-subarray/
# Maximum Subarray
# Category: Easy

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer
# approach, which is more subtle.

# Solution: sliding window; remove negative prefix (before left pointer), and keep sliding the right pointer, then
# compare the current max subarray and new max subarray (after adding new value from the right pointer), and return the
# max subarray
class Solution:
    def maxSubArray(self, nums) -> int:    # List[int] -> int:
        max_subarray = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:     # if prefix sum is less than 0, then reset the current sum to 0
                current_sum = 0
            current_sum += n        # adding new number to the current sum
            max_subarray = max(max_subarray, current_sum)   # max between current max_subarray and the new sum
        return max_subarray

