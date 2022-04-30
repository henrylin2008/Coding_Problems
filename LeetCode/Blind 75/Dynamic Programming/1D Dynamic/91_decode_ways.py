# 91. Decode Ways
# Link: https://leetcode.com/problems/decode-ways/
# Medium

# A message containing letters from A-Z can be encoded into numbers using the following mapping:
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
# mapping above (there may be multiple ways). For example, "11106" can be mapped into:
#
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).

# Note: can cur char be decoded in one or two ways? Recursion -> cache -> iterative dp solution, a lot of edge cases
# to determine, 52, 31, 29, 10, 20 only decoded one way, 11, 26 decoded two ways

class Solution:
    # recursive + cache solution
    # Time: O(n)
    # Space: O(n)
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # cache; empty string = 1

        def dfs(i):  # recursive func, i: current position
            if i in dp:  # i is already cached or i is the last position of s
                return dp[i]
            if s[i] == "0":  # base case, if char starts with "0", return 0 (no way to decode it)
                return 0
            res = dfs(i + 1)  # sub-problem: next position
            # condition for following char: i+1 is inbound, and next char is 1 or 2 and the following char in "0123456"
            # if next char inbound, and the following 2 strs/digs is between 10 and 26:
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)  # add the following str
            dp[i] = res     # cached it; dp[i] = dp[i+1] + dp[i+2]
            return res

        return dfs(0)

    # Dynamic: bottom-up solution
    # Time: O(n)
    # Space: O(n)
    # def numDecodings(self, s: str) -> int:
    #     dp = {len(s): 1}  # cache; base case: len(s): 1 if it's an empty str
    #
    #     for i in range(len(s) - 1, -1, -1):     # iterate through in the reverse order
    #         if s[i] == "0":     # base case
    #             dp[i] = 0
    #         else:
    #             dp[i] = dp[i + 1]
    #         if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
    #             dp[i] += dp[i + 2]  # add the following str
    #     return dp[0]
