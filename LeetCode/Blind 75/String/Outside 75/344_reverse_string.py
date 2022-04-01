# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
# Easy

# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
#
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s[i] is a printable ascii character.
from typing import List


class Solution:
    # Time: O(n)
    # Space: O(1); in-place swap
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0 , len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    # Method 2: using a stack, add strings into a stack, then pop the top item and replace it with s[i]
    # Time: O(n)
    # Space: O(n)
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     stack = []
    #     for c in s:
    #         stack.append(c)
    #     i = 0
    #     while stack:
    #         s[i] = stack.pop()
    #         i += 1

    # Method 3: recursive
    # Time: O(n)
    # Space: O(n)
    #     def reverseString(self, s: List[str]) -> None:
    #         """
    #         Do not return anything, modify s in-place instead.
    #         """
    #         def reverse(l, r):
    #             if l < r:
    #                 s[l], s[r] = s[r], s[l]
    #                 reverse(l + 1, r - 1)
    #         reverse(0, len(s) - 1)
