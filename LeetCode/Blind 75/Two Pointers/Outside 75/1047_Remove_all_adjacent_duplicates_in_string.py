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
    def removeDuplicates(self, s: str) -> str:
        i = 0
        res = list(s)
        for j in range(len(s)):
            res[i] = res[j]         # swap values at index i and index j
            if i > 0 and res[i - 1] == res[j]:   # if i > 0 and adjacent letters are the same
                i -= 2              # move i to 2 steps back
            i += 1                  # next i to the next position
        return ''.join(res[:i])


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
