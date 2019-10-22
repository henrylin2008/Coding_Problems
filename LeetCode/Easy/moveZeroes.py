# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order
# of the non-zero elements.
#
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
#
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

def moveZeroes(nums):
    pos = 0
    # swap 0s with ordered numbers
    # Ex: [0,1,0,3,12]
    # Loop1: [1, 1, 0, 3, 12]
    # Loop2: [1, 3, 0, 3, 12]
    # Loop3: [1, 3, 12, 3, 12]

    for i in range(len(nums)):
        if nums[i]:
            nums[pos] = nums[i]
            pos += 1

    # Loop4: [1, 3, 12, 0, 12]
    # Loop5: [1, 3, 12, 0, 0]
    for i in range(pos, len(nums)):
        nums[i] = 0