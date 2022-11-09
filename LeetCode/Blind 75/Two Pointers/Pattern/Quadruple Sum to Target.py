# Problem Challenge 1: Quadruple Sum to Target (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743502365_9Unit

# Problem Statement
#
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to
# the target number.
#
# Example 1:
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
#
# Example 2:
# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# Solution
#
# This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero.
#
# We can follow a similar approach to iterate through the array, taking one number at a time. At every step during
# the iteration, we will search for the quadruplets similar to Triplet Sum to Zero whose sum is equal to the given
# target.


