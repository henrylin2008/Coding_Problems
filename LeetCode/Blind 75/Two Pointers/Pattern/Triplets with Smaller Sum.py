# Triplets with Smaller Sum (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743469029_6Unit

# Problem Statement
#
# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[
# k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
#
# Example 1:
# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# Example 2:
#
# Input: [-1, 4, 2, 1, 3], target=5
# Output: 4
# Explanation: There are four triplets whose sum is less than the target:
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


# Solution
#
# This problem follows the Two Pointers pattern and shares similarities with Triplet Sum to Zero. The only difference
# is that, in this problem, we need to find the triplets whose sum is less than the given target. To meet the
# condition i != j != k we need to make sure that each number is not used more than once.
#
# Following a similar approach, first, we can sort the array and then iterate through it, taking one number at a
# time. Let’s say during our iteration we are at number ‘X’, so we need to find ‘Y’ and ‘Z’ such that X + Y + Z <
# targetX+Y+Z<target. At this stage, our problem translates into finding a pair whose sum is less than “target -
# Xtarget−X” (as from the above equation Y + Z == target - XY+Z==target−X). We can use a similar approach as
# discussed in Triplet Sum to Zero.
