# Largest Divisible Subset
# https://algo.monster/problems/largest_divisible_subset

# You are given a set of numbers nums consisting of distinct numbers. Find the size of the largest subset that
# satisfies the following condition: for each two number pairings in the set, one number is divisible by the other.
#
# Input
#   nums: a list integers representing the set.
# Output
# An integer representing the size of the largest subset that satisfy the condition.
#
# Examples
# Example 1:
# Input:
# nums = [1, 2, 3]
# Output: 2
#
# Explanation:
# Either [1, 2] or [1, 3] satisfy the condition, because both 2 and 3 are both divisible by 1. Either way,
# the largest set has a size of 2.
#
# Example 2:
# Input:
# nums = [1, 2, 4, 8]
# Output: 4
#
# Explanation:
# In this set, for each pair of numbers, at least one is divisible by the other because they are all powers of 2. As
# such, the max subset has a size of 4, the size of the original set.
#
# Constraints
#   1 <= len(nums) <= 1000
#   1 <= nums[i] <= 10^9
#   Each number in nums is unique
