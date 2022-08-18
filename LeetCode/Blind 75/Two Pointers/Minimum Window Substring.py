# Minimum Window Substring
# https://algo.monster/problems/minimum_window_substring

# Given two strings, original and check, return the minimum substring of original such that each character in check,
# including duplicates, are included in this substring. By "minimum", I mean the shortest substring. If two
# substrings that satisfy the condition has the same length, the one that comes lexicographically first are smaller.
#
# Parameters
#   -original: The original string.
#   -check: The string to check if a window contains it.
# Result
#   -The smallest substring of original that satisfy the condition.
#
# Examples
# Example 1
# Input: original = "cdbaebaecd", check = "abc"
# Output: baec
# Explanation: baec is the shortest substring of original that contains all of a, b, and c.
#
# Constraints
#   * 1 <= len(check), len(original) <= 10^5
#   * original and check both contains only upper case and lower case characters in English. The characters are case
#   sensitive.

# Solution
# The solution is similar to Find All Anagrams in a String, except instead of matching exactly, we are to find a
# window that contains all characters in check.
#
# In this case, the comparison for checking valid window is changed to compare that for every character in check,
# see if the window contains more of that character.
#
# In addition, the moving conditions of the window changes as well. Instead of two pointers moving at once,
# maintaining the size of the window, each pointer moves independently. When the window does not contain check,
# we move the end pointer until it does (or it reaches the end), then we move the start pointer until the window no
# longer contains check. In this case, just before moving the window was the local minimal substring. Then it's a
# simple matter of comparing local minimal substrings and find the minimum one.
#
# Time Complexity: O(n)
