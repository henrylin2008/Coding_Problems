# link: https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement
# Difficult: Medium
#
# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above
# operations.
#
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length

# PAY ATTENTION: limited to chars A-Z; for each capital char, check if it could create the longest repeating substr,
# use sliding window to optimize; check if windowlen=1 works, if yes, increment len, if not, shift window right;

# Time: O(26n) -> O(n)
# Space: O(n)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # count of each character; key=the char, value=count of each char
        res = 0  # longest substring with k replacement
        left = 0  # left pointer
        max_freq = 0  # most frequency of a letter
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)  # increment of the count of s[r]
            max_freq = max(max_freq, count[s[right]])  # max frequency of the hashmap (most freq letter in s)

            while (right - left + 1) - max_freq > k:  # # of replacement > # of replacement allowed
                count[s[left]] -= 1  # decrement of count for letter at the left pointer
                left += 1  # shift left pointer

            res = max(res, right - left + 1)  # update the result
        return res
