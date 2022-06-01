# 410. Split Array Largest Sum
# Link: https://leetcode.com/problems/split-array-largest-sum/
# Hard

# Given an array nums which consists of non-negative integers and an integer m, you can split the array into m
# non-empty continuous subarrays.
#
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Example 1:
# Input: nums = [7,2,5,10,8], m = 2
# Output: 18
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
# Example 2:
# Input: nums = [1,2,3,4,5], m = 2
# Output: 9
#
# Example 3:
# Input: nums = [1,4,4], m = 3
# Output: 4
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 106
# 1 <= m <= min(50, nums.length)
from typing import List


class Solution:
    # Time: O(n log(s)); log(s): binary search, s=sum(input array); O(n): split into m groups
    # Idea: left boundary: max(nums), right boundary: sum(nums); mid = (left + right) // 2; split nums to m groups, such
    #       group with the largest sum close to mid; start from the beginning of the array, add next value, until the
    #       sum < mid; update right boundary (mid - 1), continue the binary search until we found the smallest result
    #       possible.
    def splitArray(self, nums: List[int], m: int) -> int:
        def can_split(largest):  # split nums into m, and largest sum <= largest/mid
            subarray = 0    # number of subarray
            cur_sum = 0     # current sum
            for n in nums:  # loop through nums
                cur_sum += n    # add n to the current sum
                if cur_sum > largest:   # current_sum > largest
                    subarray += 1   # own group, increase subarray
                    cur_sum = n     # update current sum to n, b/c adding n (above) exceed the sum
            return subarray + 1 <= m

        l, r = max(nums), sum(nums)
        res = r     # assume the worst
        while l <= r:
            mid = l + ((r - l) // 2)    # mid-point
            if can_split(mid):  # split nums into m, and largest sum <= mid; mid: largest
                # if we can split, smaller result is found
                res = mid
                r = mid - 1
            else:  # look on the right side of the mid
                l = mid + 1
        return r
