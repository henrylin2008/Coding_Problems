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
    # Idea: use sliding window technique to shift the window, and use 2 hashmaps to compare the count of needed chars.
    #       while looping through chars in the string s, compare the count of the char at the left/right pointers in the
    #       have and need hashmaps, and update the count of the chars in 2 hashmaps. while the count of the chars >=
    #       count of chars in the need hashmap, then update the res and res_len; return the res (window) that is the
    #       smallest res_len after looping through string s.
    #       - 2 hashmaps to get the count of each char (window, count_t),
    #       - 2 variables to keep track of unique chars;
    #           - need: total count of needed chars in t
    #           - have: total count of unique chars in the current window
    #       - 2 pointers for the window
    #           - left pointer: left side of the window, keep sharding and update the have count and res, res_len
    #           - right pointer: count of the new char and add it to the have count if it matches the char in count_t,
    #                            while have == need, update res and res_len, shift the left pointer, if the removed char
    #                            in count_t and count of char in window < count of char in count_t, decrease the have
    #                            count, then shift left pointer
    #       - left, right (from res) is the range that we are looking for, return it if it has been changed
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""  # edge case

        count_t, window = {}, {}  # hashmaps keep track of count of each char; count_t: needed; window: current window
        for c in t:  # get the count of each char and store it in the count_t hashmap
            count_t[c] = 1 + count_t.get(c, 0)  # add one to the count of c, or return 0 if it doesn't exist in count_t

        have, need = 0, len(count_t)  # need: total count of chars in t; have: count of needed chars in current window
        res, res_len = [-1, -1], float("infinity")  # res: possible window; res_len: length of the window
        left = 0  # left pointer
        for right in range(len(s)):  # loop through the chars in string s
            c = s[right]  # char at the right pointer
            window[c] = 1 + window.get(c, 0)  # add the count of c to the current window

            if c in count_t and window[c] == count_t[c]:  # if c in count_t, and count of c matches in both hashmaps
                have += 1  # increase the have count
            # while have == need, update the window (res and res_len)
            while have == need:  # while count in both hashmaps are the same; possible multiple windows matched
                # update result
                if (right - left + 1) < res_len:  # if the size/length of the current window < res_len
                    res = [left, right]  # update the window
                    res_len = (right - left + 1)  # update the size of the window
                # shift the left pointer and compare the count of this char to count in the need hashmap
                window[s[left]] -= 1  # pop from the left of the window
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:  # if this char (left) is needed char from
                    # count_t, and the count of have (hashmap) < count of need (hashmap)
                    have -= 1  # decrease the have count
                left += 1  # shift left pointer
        left, right = res  # res left, right pointers
        return s[left:right + 1] if res_len != float("infinity") else ""  # return if res_len has changed else return ""
