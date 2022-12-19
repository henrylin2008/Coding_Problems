# Sliding Window Median (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744001784_63Unit

# Problem Statement
#
# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
#
# Example 1:
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
#   * [1, 2, -1, 3, 5] -> median is 1.5
#   * [1, 2, -1, 3, 5] -> median is 0.5
#   * [1, 2, -1, 3, 5] -> median is 1.0
#   * [1, 2, -1, 3, 5] -> median is 4.0
#
# Example 2:
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
#   * [1, 2, -1, 3, 5] -> median is 1.0
#   * [1, 2, -1, 3, 5] -> median is 2.0
#   * [1, 2, -1, 3, 5] -> median is 3.0

# Solution
#
# This problem follows the Two Heaps pattern and share similarities with Find the Median of a Number Stream. We can
# follow a similar approach of maintaining a max-heap and a min-heap for the list of numbers to find their median.
#
# The only difference is that we need to keep track of a sliding window of ‘k’ numbers. This means,
# in each iteration, when we insert a new number in the heaps, we need to remove one number from the heaps which is
# going out of the sliding window. After the removal, we need to rebalance the heaps in the same way that we did
# while inserting.
