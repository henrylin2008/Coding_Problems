# 213. House Robber II
# Link: https://leetcode.com/problems/house-robber-ii/
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if
# two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.
#
#
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#
# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 3:
# Input: nums = [1,2,3]
# Output: 3
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 1000
#
# note: subarr = arr without first & last, get max of subarr, then pick which of first/last should be added to it
from typing import List


# Time: O(n); O(2n) for 2 help functions --> O(n)
# space: O(1); no data structure used
class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(first_num, max except first num, max except last num)
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))

    def help(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
