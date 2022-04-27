# https://leetcode.com/problems/valid-anagram/
# Category: Easy
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
#
# Constraints:
#
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# Solution: use hashmap to count each chart; return False if lengths are different or total count are different
# Time: O(s + t); run through every character in each string
# Space: O(s + t); needs to store all characters from each string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # count for each key if a match is found.
            # .get() returns matched key, otherwise return default value of 0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


# Solution #2: use Counter function from the Collections module
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Solution #3: constraint: run in constant space; use the built-in sorted function to sort each string
# Time: O(nLog(n)); best runtime for sorting algorithm is O(nlog(n)).
# Space: O(1); no extra space needed, as it compares each character in each string after sorting takes place
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
