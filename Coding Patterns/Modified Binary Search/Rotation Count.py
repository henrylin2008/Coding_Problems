# Problem Challenge 3: Rotation Count (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744200311_86Unit

# Problem Statement
# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.
#
# Example 1:
# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.
#           Original array:     1   |   3   |   8   |   10   |   15   |
#  Array after 2 rotations:     10  |   15  |   1   |   3    |   8    |
#
# Example 2:
# Input: [4, 5, 7, 9, 10, -1, 2]
# Output: 5
# Explanation: The array has been rotated 5 times.
#           Original array:     -1   |   2   |   4   |   5   |   7   |   9   |   10   |
#  Array after 2 rotations:      4   |   5   |   7   |   9   |   10  |  -1   |    2   |
#
# Example 3:
# Input: [1, 3, 8, 10]
# Output: 0
# Explanation: The array has not been rotated.
