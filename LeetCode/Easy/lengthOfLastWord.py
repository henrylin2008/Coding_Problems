# 58. Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


def lengthOfLastWord(s):
    count = 0
    local_count = 0

    for i in range(len(s)):
        # if the letter is blank, then reset local count to 0
        if s[i] == ' ':
            local_count = 0
        # increment local count if it is not a letter, and set local count to global count
        else:
            local_count += 1
            count = local_count
    # return global count
    return count




lengthOfLastWord("sweet dream")

