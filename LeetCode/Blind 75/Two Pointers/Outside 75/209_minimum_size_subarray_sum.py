# 209. Minimum Size Subarray Sum
# Link: https://leetcode.com/problems/minimum-size-subarray-sum/
# Medium

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
# subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
# such subarray, return 0 instead.
#
#
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
#
# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1
#
# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#
# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
#
#
# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is
# O(n log(n)).
from typing import List


class Solution:
    # Time: O(n); loop through entire list
    # Time: O(1); only using the pointers, no data structure were used
    # Note: using 2 pointers, keep shifting the right pointer and find the sum of the current window, until the
    # sum >= target, calculate the size of the current window, deduct value at left pointer from the current sum, and
    # shift the left pointer to the next position; return min window that matches the target, else return 0
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')      # default value: inf, could also be -1 or len(nums) + 1
        left, total = 0, 0
        for right in range(len(nums)):
            total += nums[right]    # adding right value to the total
            while total >= target:
                res = min(right - left + 1, res)    # min size of current window, or previous calculated res
                total -= nums[left]                 # remove left pointer from the total
                left += 1                           # shift left pointer
        return 0 if res == float('inf') else res    # 0 if not matching else return res
