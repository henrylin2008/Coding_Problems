# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

# solution #1
# def longestCommonPrefix(strs):
#
#     if not strs: # when no string
#         return "" # return empty string
#
#     for i in range(len(strs[0])): # for every char in first word
#         for string in strs[1:]: # for words after index 0 (first word)
#             if i >= len(string) or string[i] != strs[0][i]: # when i is greater or equal to length of string (must be first condition)
#                 # or when string in index i not equal to the string in same position of first word
#                 return strs[0][:i] #return matched string/s before index i (not including i) in first word
#
#     return strs[0] # strs[0] == [""]; string exist as an empty str([""])

#Solution #2
def longestCommonPrefix(strs):
    result = "" # set a result variable
    i = 0

    while True:
        try:
            sets = set(string[i] for string in strs) # unique value of each index of each string;
            # Ex 1: ["flower","flow","flight"]
            # {'f'}
            # {'l'}
            # {'o', 'i'}, etc..
            if len(sets) == 1: # when only one character is matching through each string
                result += sets.pop() # append (matched) character into sets
                i += 1 # move on to next index
            else: break # break/stop  when no more matching character
        except Exception as e:
            break

    return result           