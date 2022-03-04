# link: https://leetcode.com/problems/product-of-array-except-self/
# 238. Product of Array Except Self
# Difficulty: Medium

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
# of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra
# space for space complexity analysis.)

# Solution: 2 passes: one for prefix (in-order), one for postfix (reverse order)
# ex:       1     2     3     4
#             \      \     \
# prefix    1     1     2     6  (prefix starts at 1, then multiply it by the new prefix number: 1, 1*1, 1*2, 2*3)
#           |     |     |     |  (postfix starts at 1, 1*6(result from prefix), next postfixes: 1*4=4, 4*3=12, 12*2)
# postfix   24    12    8     6  (from right to left; 1*6=6, 4(1*4) *2(prefix)=8, 12 (4*3)*1 = 12, 24 (12*2) * 1 = 24)

# Time: O(n)
# Space: O(1)
class Solution:
    def productExceptSelf(self, nums):  # List[int]) -> List[int]
        result = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):  # loop through to get the prefix result: 1, 1, 2, 6
            result[i] = prefix
            prefix *= nums[i]  # previous prefix * new number from nums
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):   # reverse order, starts from the end (to the left)
            result[i] *= postfix
            postfix *= nums[i]
        return result

