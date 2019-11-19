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
    pos = 0  # index of swapped integer
    # go through the array, and move ordered integers to the front of the array and move zeros to the back
    # Ex: [0,1,0,3,12]

    for i in range(len(nums)):
        if nums[i]:   # if i (every non-zero integer) exist
            nums[pos] = nums[i]  # swap pos and i
            pos += 1 # increment by 1
    # After Loop1: [1, 1, 0, 3, 12]; pos: 1
    # After Loop2: [1, 3, 0, 3, 12]; pos: 2
    # After Loop3: [1, 3, 12, 3, 12]; pos: 3

    for i in range(pos, len(nums)):  # from pos to len(nums)
        nums[i] = 0     # set rest value after pos to 0
    # Loop4: [1, 3, 12, 0, 12]
    # Loop5: [1, 3, 12, 0, 0]
