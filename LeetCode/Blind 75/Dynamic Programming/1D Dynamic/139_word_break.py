# 139. Word Break
# https://leetcode.com/problems/word-break/
# Medium

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
from typing import List


class Solution:
    # Dynamic - Button up + cache
    # Note: set up a dp array with length of s + 1, (+1) last item is the base case (True); going through every index of
    # s in the reverse order, if current idx (i) + len(w) within the len(s) AND s[i: i + len(w)] matches the word,
    # then shift the pointer (i + len(w)) => True; or if there's a single way to word break at index i, then skip the
    # current loop (move to next index); dp[0] (last value in the reverse loop) is the value to return

    # ex: Input: s = "leetcode", wordDict = ["leet","code"]
    # dp = len(s) + 1: [False, False, False, False, False, False, False, False, False]
    # base case: dp[8] = True
    # dp[7] = dp[6] = dp[5] = False
    # dp[4] = True
    # dp[3] = dp[2] = dp[1] = False
    # dp[0] = dp[0 + len(w)] = dp[0+4] = dp[4] (cached) = True
    # return True (based off dp[0])

    # Time: O(n*m*n); n: length of s; m: words in wordDict
    # Space: O(n); dp, cache to store length of s.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)     # cache: 1-Dimensional array; +1 for base case (last position)
        dp[len(s)] = True               # base case (last position = True)
        for i in range(len(s) - 1, -1, -1):     # reverse order
            for w in wordDict:                  # check every word in wordDict
                # if i+len(w) within range of s and characters in range of the length of word within s == word
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]     # shift pointer after length of current word, dp[4] = dp[8], from cache
                if dp[i]:       # if single way to word break, then stop the loop, no need to check every word
                    break
        return dp[0]        # last value in the loop and first value in the cache (dp)
