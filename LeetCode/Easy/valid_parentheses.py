# 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

# case 1: ()[]{}
# case 2: ([)]
# case 3: {

# time: O(n)
# Space: O(n)

def isValid(s):
    lookup = {"(":")", "{":"}", "[":"]"}
    stack = []
    for c in s:
        if c in lookup:
            stack.append(c)  # add c to stack if it's in lookup table
        elif len(stack) == 0 or lookup[stack.pop()] != c: # if stack is empty or top of stack does not pair with closing parenthesis
            # pop will pair matched parenthesis and move it out of stack 
            #ex: )(; [(])
            return False
    return len(s)