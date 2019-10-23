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
        output ^= num  # ex: [2,2,1]

    return output
        # loop 1: output=2
        # loop 2: output=0
        # loop 3: output=1

# Bit Manipulation
# Concept
#
# - If we take XOR of zero and some bit, it will return that bit
#     * a ^ 0 = a
# - If we take XOR of two same bits, it will return 0
#     * a ^ a = 0
#
# -a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b

# Time complexity : O(n)O(n). We only iterate through \text{nums}nums, so the time complexity is the number of elements in \text{nums}nums.
#
# Space complexity : O(1)O(1).
