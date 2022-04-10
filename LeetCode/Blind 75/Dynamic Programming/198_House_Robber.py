# 198. House Robber
# Link: https://leetcode.com/problems/house-robber/
# Medium

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

# Note: for each num, get max of prev subarr, or num + prev subarr not including last element, store results of prev,
# and prev not including last element
# Logic: sliding window, ex: [rob1, rob2, n, n+1, ...]; find the max of (rob1 + n, rob2), then move rob1 to rob2
# position, and rob2 = temp (max((rob1+1), rob2))); return rob2
from typing import List


# Time: O(n)
# Space: O(1); only pointers
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)  # max of first 3 nums, or max upto position n
            rob1 = rob2     # move to next num
            rob2 = temp     # rob2 move to position n
        return rob2
