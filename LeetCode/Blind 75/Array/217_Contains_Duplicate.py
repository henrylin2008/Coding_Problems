# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
#
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
# element is distinct.
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: true
#
# Example 2:
#
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

# Solution:
# use a hashset to get unique values in array to check for duplicates easily; if found return True, otherwise False
# Time: O(n); scan through input array once
# Space: O(n); worse case: store all numbers in nums
def containDuplicate(nums) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

