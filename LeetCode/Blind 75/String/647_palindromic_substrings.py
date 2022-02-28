# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Difficulty: Medium

# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
#
# Example 1:
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

# Time: O(n^2); odd length, O(n) for all chars, expanding outward is O(n), -> O(n*n) = O(n^2); same for even length
#               O(n^2) + O(n^2) ==> O(2n^2) => O(n^2)
# Space: O(n); result to store the count of palindromic
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:   # while within the range, and left letter == right letter
                res += 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res
