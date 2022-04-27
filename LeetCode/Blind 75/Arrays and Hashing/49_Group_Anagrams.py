# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams - Medium
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
#
# Constraints:
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

# Solution:
# use Hashmap to count number of time that each character appearance; ex: "eat", key would be # of occurrence of each
# letter (1e, 1a, 1t), values are the list of anagrams (which string has the pattern from the key)
from collections import defaultdict

# time: O(m*n*26) -> O(mn); m: number of input strings; n: length (chars) of a string
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)  # mapping charCount to list of anagrams; defaultdict to deal with non-existing char

        for str in strs:
            count = [0] * 26  # [0....0] = [a....z]

            for char in str:
                count[ord(char) - ord("a")] += 1    # count of each character

            res[tuple(count)].append(str)   # group anagrams together; tuple(count): b/c count is a list and it can't be
            # the key in Python.
        return res.values()  # return a list of anagrams
