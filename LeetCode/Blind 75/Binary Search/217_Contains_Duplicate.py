# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.
#
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
#
# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


# Time: O(n)
# Space: O(n)
# Logic: use a hashset to add unique values, and loop through the list to verify if current num exists in the hashset,
#        then return True/False if the num exist in the hashset
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
