# https://leetcode.com/problems/valid-palindrome/
# Problem 125 - Valid Palindrome
# Category: Easy
#
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Constraints:
# -1 <= s.length <= 2 * 105
# -s consists only of printable ASCII characters.

# Solution: create an empty string to store every character from the given s, then compare it with the reverse string
#           this solution uses the extra memory (an empty string), and uses the built-in functions
# Time: O(n)
# Space: O(n); n is number of characters in s
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""

        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]


# Solution #2: more efficient method; using 2 pointers: left pointer and right pointer, and skip the white space
# Time: O(n)
# Space: O(1), only pointers are used, no extra memory is used
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) -1
        while left < right:
            while left < right and not self.alphaNum(s[left]):  # enable both characters (left and right) are alphaNum
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():     # compare letters at current position in lower case
                return False
            left += 1
            right -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
