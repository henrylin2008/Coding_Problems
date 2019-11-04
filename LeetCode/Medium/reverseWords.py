# 151. Reverse Words in a String
# https://leetcode.com/problems/reverse-words-in-a-string/
#
# Given an input string, reverse the string word by word.
#
# Example 1:
#
# Input: "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
#
# Example 3:
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# Note:
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
#
# Follow up:
# For C programmers, try to solve it in-place in O(1) extra space.

def reverseWord(s):
    if s == "":
        return s  # return s if it's empty

    ls = s.split() # split evey word in string

    if ls == []:   # case: "    ", if it's all space
        return ""   # return empty

    result = ""
    for i in range(0, len(ls)-1):  # for word from first to last-1 (second to last)
        result += ls[len(ls)-1-i] + " "  #
    result += ls[0]

    return result
