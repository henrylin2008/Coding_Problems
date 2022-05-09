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

# Note: need is num of unique char in T, HAVE is num of char we have valid count for, sliding window, move right
# until valid, if valid, increment left until invalid, to check validity keep track if the count of each unique char
# is satisfied;


class Solution:
    # Time: O(n); sliding window loop through the string once
    # Space: O(1); using hashmaps and 2 pointers
    # Idea: use 2 hashmaps to get the count of each char (window, count_t), and 2 variables to keep track of unique char
    #       (need: len(count_t), have: so far in the window), use 2 pointers to find the window; as the right pointer
    #       sliding through the string s, find the window and make sure the need (count) and have (count) are equal,
    #       and shift the left pointer, then find the minimum window/length.
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""  # edge case

        count_t, window = {}, {}  # hashmaps keep track of count of each char; window: current window
        for c in t:  # count of each char and store it in the count_t hashmap
            count_t[c] = 1 + count_t.get(c, 0)

        have, need = 0, len(count_t)  # need: count of unique char in t; have: count of unique char so far
        res, res_len = [-1, -1], float("infinity")  # res: possible window [l, r]; res_len: length of the window
        l = 0  # left pointer
        for r in range(len(s)):  # loop through the string s
            c = s[r]  # char at the right pointer
            window[c] = 1 + window.get(c, 0)  # get the count of the char

            if c in count_t and window[c] == count_t[c]:  # if c in count_t, and count of c matches in both hashmaps
                have += 1  # increase the have count

            while have == need:  # while loop when both hashmaps are same, while b/c it could have some windows match
                # update result
                if (r - l + 1) < res_len:  # if the length of the current window < res_len
                    res = [l, r]  # update the window
                    res_len = (r - l + 1)  # update the size of the window
                # pop from the left of the window
                window[s[l]] -= 1  # remove char at the left pointer
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:  # if this char (req) in count_t and the count of
                    # this char < need of this char in count_t
                    have -= 1  # decrease the have count
                l += 1  # shift left pointer
        l, r = res  # res left, right pointers
        return s[l:r + 1] if res_len != float("infinity") else ""  # return if res_len has been changed else empty str
