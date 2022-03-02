# 271. Encode and decode strings
# link: https://www.lintcode.com/problem/659/description
# Difficulty: Medium

# Description
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is
# decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Example1
# Input: ["lint","code","love","you"]
# Output: ["lint","code","love","you"]
# Explanation:
# One possible encode method is: "lint:;code:;love:;you"
#
# Example2
# Input: ["we", "say", ":", "yes"]
# Output: ["we", "say", ":", "yes"]
# Explanation:
# One possible encode method is: "we:;say:;:::;yes"

# Encoding: store length of str before each string and delimiter like '#';
#           ex: # Input: ["lint","code","love","you"] -> 4#lint4#code4#love3#you
# Time: O(n); n is number of characters in given string
# Space: O(n)
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i       # first char (num)
            while str[j] != "#":
                j += 1      # nive ti second char (#)
            length = int(str[i:j])    # length of the string
            res.append(str[j + 1: j + 1 + length])  # append each string to the res
            i = j + 1 + length      # move index to the next num (beg of next string)
        return res


