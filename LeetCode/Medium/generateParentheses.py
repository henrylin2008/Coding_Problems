# 22. Generate Parentheses
# Link: https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# def generateParentheses(n):
#     if n == 0:
#         return []
#
#     result = [] #
#     self.helper(n, n, '', result)
#     return result
#
# def helper(r, item, result):
#     if l < r:
#         return
#     if l == 0 and r == 0:
#         result.append(item)
#     if l > 0:
#         self.helper(l-1, r, item + '(', result)
#     if r > 0:
#         self.helper(l, r-1, item + ')', result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: # return empty array if n == 0
            return []
        result = [] #
        self.helper(n, n, '', result) #recursive calls, n = # of '('; n = # of ')'; ''= temp return value, result = final return list 
        return result

    def helper(self, l, r, item, result): # l = # of "(" left; r = # of ')' left; item = current return value;
        # result = append (current) returned value
        if r < l:  # if r left value less than l left value, that mean [')'] has gone before ['('], which is invalid
            # Ex: ())( : ) [i(2)] put in before (, resulted in invalid, no need to append anything into result
            return
        if l == 0 and r == 0: # if no ['('] and [')'] parentheses left, append the item into the result list
            result.append(item)
        if l > 0: # if any left ['('] parenthesis left
            self.helper(l - 1, r, item + '(', result) # decrease l ['('] by 1, and append '(' into temp item list
        if r > 0: # if any right [')'] parenthesis left
            self.helper(l, r - 1, item + ')', result) # decrease r [')'] by 1, and append ')' into temp item list
