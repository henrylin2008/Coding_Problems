# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Medium

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer
# in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
#
#
# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
# Example 2:
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
# Constraints:
#
# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.
from typing import List


class Solution:
    # Time: O(26) -> O(1), only 26 lower letters: a-z
    # Space: O(26); worst case to store every letter
    # Logic: use 2 hashmaps to count characters in the string, and use 2 pointers/sliding window to move along the
    #        string s, while moving the right pointer, get/add the count of new char, and decrease the count of the char
    #        at the left pointer, if count of left pointer char equals 0, pop it out from count_s, then move the left
    #        pointer to the next position; whenever count_s equals count_p, add the left pointer to the res
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):     # edge case
            return []

        count_s, count_p = {}, {}   # hashmaps to store the count of each char in the given str
        for c in range(len(p)):     # loop through the length of p
            count_p[p[c]] = 1 + count_p.get(p[c], 0)    # get count of the char in p
            count_s[s[c]] = 1 + count_s.get(s[c], 0)    # get count of the char in s

        res = [0] if count_p == count_s else []  # add starting/left index of anagram to res if both hashmaps are equal
        l = 0           # left pointer
        for r in range(len(p), len(s)):  # loop through substrings after len(p)
            count_s[s[r]] = 1 + count_s.get(s[r], 0)    # get count of the char in s
            count_s[s[l]] -= 1                          # decrease the count of the char at the left pointer

            if count_s[s[l]] == 0:     # if count of the char == 0, then remove it from count_s
                count_s.pop(s[l])
            l += 1                     # move left pointer
            if count_s == count_p:     # if both hashmaps are the same
                res.append(l)          # add the left pointer to the res
        return res
