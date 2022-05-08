# 76. Minimum Window Substring
# Link: https://leetcode.com/problems/minimum-window-substring/
# Hard

# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
# character in t (including duplicates) is included in the window. If there is no such substring, return the empty
# string "".
#
# The testcases will be generated such that the answer is unique.
#
# A substring is a contiguous sequence of characters within the string.
#
#
#
# Example 1:
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
# Constraints:
#
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
#
#
# Follow up: Could you find an algorithm that runs in O(m + n) time?

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""   # edge case

        count_t, window = {}, {}    # hashmaps to keep track of count of each char
        for c in t:     # count of each char and store it in the count_t hashmap
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)    # need: count of unique char in t; have: count of unique char in the window
        res, res_len = [-1, -1], float("infinity")  # res: possible window; res_len: length of the window
        l = 0   # left pointer
        for r in range(len(s)):     # loop through the string s
            c = s[r]    # char at the right pointer
            window[c] = 1 + window.get(c, 0)    # get the count of the char

            if c in count_t and window[c] == count_t[c]:    # c in count_t and
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if res_len != float("infinity") else ""
