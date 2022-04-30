# Link: https://leetcode.com/problems/longest-palindromic-substring/
# Longest Palindromic Substring
# Difficultly: Medium
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Solution: foreach char in str, consider it were the middle, consider if pali was odd or even
# Time: O(n^2); loop through each character: O(n), and expand it out takes is another O(n), thus O(n^2)
# Space: O(n); worst case: need to store every character in s.
def longestPalindrome(self, s: str) -> str:
    result = ""
    result_len = 0

    for i in range(len(s)):
        # odd length (ex:'babad' --> 'bab')
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > result_len:
                result = s[left:right+1]
                result_len = right - left + 1
            left -= 1
            right += 1

        # even length (ex: 'cbbd' --> 'bb')
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > result_len:
                result = s[left:right+1]
                result_len = right - left + 1
            left -= 1
            right += 1

    return result
