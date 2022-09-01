# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
from typing import List


class Solution:
    # Time: O(n); would need to go through the entire list
    # Space: O(1); using Hashmap to store difference between target and num that has seen so far
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}      # dictionary to store nums; val: index
        for i, v in enumerate(nums):
            if target - v in d:             # diff = target - v
                return [d[target-v], i]     # index of diff and current index
            else:
                d[v] = i        # store value as the key in the dictionary, and index as the value
