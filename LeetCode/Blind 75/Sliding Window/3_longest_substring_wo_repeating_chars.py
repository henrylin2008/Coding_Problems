# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Difficulty: Medium

# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Constraints:
#
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# Solution: sliding window, if we see same char twice within curr window, shift start position (remove left, move right)
#           use a variable (max_length) to keep track of the max length (of distinct chars) while sliding through str.
# Time: O(n); loop through every char in the string
# Space: O(n); set to store unique characters, potentially every character in the string
def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()    # keep track of unique chars
    max_length = 0
    left = 0            # left pointer of the sliding window
    for right in range(len(s)):         # sliding the right pointer
        while s[right] in char_set:     # if right char is in the char_set
            char_set.remove(s[left])    # remove the leftmost char
            left += 1                   # shift left pointer
        char_set.add(s[right])          # add right char to char_set hashmap
        max_length = max(max_length, right - left + 1)
    return max_length
