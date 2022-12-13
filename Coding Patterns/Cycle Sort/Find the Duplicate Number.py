# Find the Duplicate Number (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743725641_32Unit

# Problem Statement
#
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one
# duplicate but it can be repeated multiple times. Find that duplicate number without using any extra space. You are,
# however, allowed to modify the input array.
#
# Example 1:
# Input: [1, 4, 4, 3, 2]
# Output: 4
#
# Example 2:
# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
#
# Example 3:
# Input: [2, 4, 1, 4, 4]
# Output: 4

# Solution
#
# This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number. Following a
# similar approach, we will try to place each number on its correct index. Since there is only one duplicate,
# if while swapping the number with its index both the numbers being swapped are same, we have found our duplicate!

