# 136. Single Number
# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

def singleNumber(nums):
    output = 0  # set a output value

    for num in nums:
        output ^= num  # ex: [2,2,1], see below for concept
        # loop 1: output=2
        # loop 2: output=0
        # loop 3: output=1

    return output
s
# https://leetcode.com/problems/single-number/solution/
# Bit Manipulation
# Concept
#
# - If we take XOR of zero and some bit, it will return that bit
#     * a ^ 0 = a
# - If we take XOR of two same bits, it will return 0
#     * a ^ a = 0
#
# - a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

# Time complexity : O(n). We only iterate through nums, so the time complexity is the number of elements in nums.
#
# Space complexity : O(1).


# Approach 1: List operation
# Algorithm
#
# Iterate over all the elements in nums
# If some number in nums is new to array, append it
# If some number is already in the array, remove it

# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         no_duplicate_list = []
#         for i in nums:
#             if i not in no_duplicate_list:
#                 no_duplicate_list.append(i)
#             else:
#                 no_duplicate_list.remove(i)
#         return no_duplicate_list.pop()

# Complexity Analysis
#
# Time complexity : O(n^2). We iterate through nums, taking O(n) time. We search the whole list to find whether
# there is duplicate number, taking O(n) time. Because search is in the for loop, so we have to multiply both time
# complexities which is O(n^2).
#
# Space complexity : O(n). We need a list of size nn to contain elements in nums.
