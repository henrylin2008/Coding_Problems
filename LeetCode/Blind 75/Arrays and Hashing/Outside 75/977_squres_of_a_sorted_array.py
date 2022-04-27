# Link: https://leetcode.com/problems/squares-of-a-sorted-array/
# Squares of a Sorted Arrays and Hashing: Easy
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
#
#
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a
# different approach?

# Solution: to solve this problem in O(n), we have to use 2 pointers: left, right; square of each num and compare values
# at left and right pointers, append the larger value in the result array first, then move the pointer to next index;
# then return the reverse order of the result array.
class Solution:
    def sortedSquares(self, nums):  # nums: List[int]) -> List[int]
        result = []
        left, right = 0, len(nums) - 1  # left, right pointer

        while left <= right:    # compare the squared values at left and right pointers and append to the result arr
            if nums[left] * nums[left] > nums[right] * nums[right]:
                result.append(nums[left] * nums[left])
                left += 1
            else:
                result.append(nums[right] * nums[right])
                right -= 1

        return result[::-1]     # reverse the array
