# link: https://leetcode.com/problems/majority-element/
# Majority Element: easy
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
class Solution:
    # Time: O(n)
    # Space: O(n)
    def majorityElement(self, nums) -> int:  # nums: List[int]
        """
        solution 1: use hashmap to get count of each value
         """
        count = {}
        result, max_count = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # update/increment count for each value, default value of 0
            result = n if count[n] > max_count else result  # update count when its value is > max_count
            max_count = max(count[n], max_count)
        return result
