# Find all Duplicate Numbers (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743734011_33Unit

# Problem Statement
#
# We are given an unsorted array containing n numbers taken from the range 1 to n. The array has some numbers
# appearing twice, find all these duplicate numbers using constant space.
#
# Example 1:
# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
#
# Example 2:
# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

# Solution
#
# This problem follows the Cyclic Sort pattern and shares similarities with Find the Duplicate Number. Following a
# similar approach, we will place each number at its correct index. After that, we will iterate through the array to
# find all numbers that are not at the correct indices. All these numbers are duplicates.

