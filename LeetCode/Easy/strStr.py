# 28. Implement strStr()
# Link: https://leetcode.com/problems/implement-strstr/
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
# and Java's indexOf().

def strStr(haystack, needle):

    for i in range(len(haystack) - len(needle) + 1): # go through every item in range b/t difference of 2 strings
        # range = difference b/t len(haysatack) and len(needle)
        if haystack[i: i + len(needle)] == needle:  # search if there's a match of string of needle in haystack
            # ex 1 (above): i + len(needle) = 2 + 2 = 4
            # haystack[i: i + len(needle)] = ll
            return i # return the index of first matched letter (of needle)
    return -1  # if no match found 