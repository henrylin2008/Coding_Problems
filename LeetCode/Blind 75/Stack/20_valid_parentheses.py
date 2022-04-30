# 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in hashmap:  # if char in hashmap (close to open)
                if stack and stack[-1] == hashmap[c]:  #stack not empty and last value (top of stack) matches in hashmap
                    stack.pop()  # pop the top item
                else:  # if stack is empty, or they don't match each other: return False
                    return False
            else:  # else if it's open parentheses: (, {, [
                stack.append(c)  # add it to the stack
        return True if not stack else False
