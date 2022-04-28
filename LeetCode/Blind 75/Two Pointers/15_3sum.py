# 15. 3Sum
# Link: https://leetcode.com/problems/3sum/
# Medium

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
# and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#
# Note: sort input, for each first element, find next two where -a = b+c, if a=prevA, skip a, if b=prevB skip b to
# elim duplicates; to find b,c use two pointers, left/right on remaining list;

from typing import List


class Solution:
    # Time: O(nlogn) + O(n^2) => O(n^2); O(nlogn): sorting; O(n^2): 2 nested loops
    # Space: O(1) or O(n); O(1) for only using the pointers; O(n): sorting, for using certain libraries
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:    # not the first value, and current value is same as last value
                continue                            # skip

            l, r = idx + 1, len(nums) - 1
            while l < r:
                three_sum = val + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1      # update only the left pointer; conditions above would update the other pointer
                    # ex: [-2, -2, 0, 0, 2, 2]
                    while nums[l] == nums[l - 1] and l < r:     # current value == last value and left < right
                        l += 1
        return res
