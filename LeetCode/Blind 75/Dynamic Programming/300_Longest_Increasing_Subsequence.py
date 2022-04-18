# 300. Longest Increasing Subsequence
# Link: https://leetcode.com/problems/longest-increasing-subsequence/
# Medium

# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
# order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
from typing import List


# Dynamic programming
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)       # cache to store repeated work; a list with all 1s

        for i in range(len(nums) - 1, -1, -1):  # loop through in the reverse order
            for j in range(i + 1, len(nums)):   # every subsequence after i
                if nums[i] < nums[j]:           # if current num < next num:
                    lis[i] = max(lis[i], 1 + lis[j])    # max of list[i] or 1 + list[i]
        return max(lis)     # return max in the lis
