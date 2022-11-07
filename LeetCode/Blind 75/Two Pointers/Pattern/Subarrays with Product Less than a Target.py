# Subarrays with Product Less than a Target (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743479436_7Unit

# Problem Statement
#
# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose
# product is less than the target number.
#
# Example 1:
#
# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:
#
# Input: [8, 2, 6, 5], target=50
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5]
# Explanation: There are seven contiguous subarrays whose product is less than the target.

# Solution
#
# This problem follows the Sliding Window and the Two Pointers pattern and shares similarities with Triplets with
# Smaller Sum with two differences:
#   1. In this problem, the input array is not sorted.
#   2. Instead of finding triplets with sum less than a target, we need to find all subarrays having a product less than
#      the target.
# The implementation will be quite similar to Triplets with Smaller Sum.
