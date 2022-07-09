# Strictly Increasing or Strictly Decreasing
# Easy
# Given a list of integers nums, return whether the list is strictly increasing or strictly decreasing.
#
# Constraints
# n ≤ 100,000 where n is the length of nums
#
# Example 1
# Input
# nums = [1, 2, 3, 4, 5]
#
# Output
# True
#
# Explanation
# This is strictly increasing.
#
# Example 2
# Input
# nums = [1, 2, 3, 4, 5, 5]
#
# Output
# False
#
# Explanation
# Since there's two duplicate 5 this is not strictly increasing.
#
# Example 3
# Input
# nums = [5, 4, 3, 2, 1]
#
# Output
# True
# Explanation
# This is strictly decreasing.

# Time: O(n); loop through nums a couple of times
# Space: O(1); no space is use
class Solution:
    def solve(self, nums):
        if len(nums) == 1:
            return True
        return all(x > y for x, y in zip(nums, nums[1:])) or all(x < y for x, y in zip(nums, nums[1:]))