# 152. Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Difficulty: Medium
#
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
# and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
# Example 1:
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
# Example 2:
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
# Constraints:
# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Solution: dp: compute max and max-abs-val for each prefix subarray;
#
# Time: O(n)
# Space: O(n)
def maxProduct(self, nums) -> int:
    res = max(nums)
    cur_min, cur_max = 1, 1

    for n in nums:
        temp = n * cur_max
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(temp, n * cur_min, n)
        res = max(res, cur_max)
    return res
