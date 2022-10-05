# Longest Substring with Distinct Characters (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541027921_3Unit

# Problem Statement
# Given a string, find the length of the longest substring, which has all distinct characters.
#
# Example 1:
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".
#
# Example 2:
# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring with distinct characters is "ab".
#
# Example 3:
# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings with distinct characters are "abc" & "cde".

# Solution
#
# This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as
# discussed in Longest Substring with K Distinct Characters. We can use a HashMap to remember the last index of each
# character we have processed. Whenever we get a duplicate character, we will shrink our sliding window to ensure
# that we always have distinct characters in the sliding window.
