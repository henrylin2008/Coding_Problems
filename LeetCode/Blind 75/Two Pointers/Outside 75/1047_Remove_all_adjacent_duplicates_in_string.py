# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Easy

# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two
# adjacent and equal letters and removing them.
#
# We repeatedly make duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
#
#
#
# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only
# possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
#
# Example 2:
# Input: s = "azxxzy"
# Output: "ay"
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of lowercase English letters.

# Two pointers solution
class Solution:
    # Time: O(n); loop through the entire s
    # Space: O(n); using a list to store the result
    #
    # Note:
    # left refers to the index to set next character in the output string.
    # right refers to the index of current iteration in the input string.
    #
    # Iterate characters of S one by one by increasing right.
    # -If S[right] is same as the current last character S[left - 1], we remove duplicates by doing left -= 2.
    # -If S[right] is different as the current last character S[left - 1], we set S[left] = S[right] and increment
    #   left+=1.
    def removeDuplicates(self, s: str) -> str:
        left = 0
        res = list(s)
        for right in range(len(s)):     # j is the right pointer, to iterate through the s
            res[left] = res[right]         # swap values at index i and index j
            if left > 0 and res[left - 1] == res[right]:   # if i > 0 and adjacent letters are the same
                left -= 2              # move i to 2 steps back
            left += 1                  # next i to the next position
        return ''.join(res[:left])


# Stack solution
# class Solution:
#     # Time: O(n); loop through the entire s
#     # Space: O(n); using list to store items in stack
#     def removeDuplicates(self, s: str) -> str:
#         stack = []
#
#         for c in s:
#             if not stack:
#                 stack.append(c)
#             else:
#                 if c == stack[-1]:
#                     stack.pop()
#                 else:
#                     stack.append(c)
#         return "".join(stack)
