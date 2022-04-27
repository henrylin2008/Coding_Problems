# 153. Find Minimum in Rotated Sorted Arrays and Hashing
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
# the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1],
# a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
#
# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
#
#
# Constraints:
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.

# solution: check if half of array is sorted in order to find pivot, arr is guaranteed to be in at most two sorted
#           subarrays
# Time: O(log n)
# Space: O(1); only use a couple of pointers and a variable for result.

class Solution:
    def findMin(self, nums) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:   # sub-array already sorted
                res = min(res, nums[l])     # update result by comparing current result and most left pointer value
                break       # exit

            # binary search when array is not sorted
            m = (l + r) // 2        # mid pointer
            res = min(res, nums[m])     # update result
            if nums[m] >= nums[l]:  # if left sub-array is sorted, search right side
                l = m + 1   # move left pointer
            else:       # search left side
                r = m - 1   # move right pointer
        return res
