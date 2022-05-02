# Balanced Brackets:
# https://www.algoexpert.io/questions/Balanced%20Brackets
# Difficulty: Medium
#
# Write a function that takes in a string made up brackets ((,[,{,),],and})) and other operational characters. The
# function should return a boolean representing whether the string is balanced with regards to bracket.
#
# A string is said to be balanced if it has as many opening brackets or a certain type as it has closing brackets of
# that type and if no bracket is unmatched. Note that an opening bracket can't match a corresponding closing bracket
# that comes before it, and similarly, a closing bracket can't match a corresponding opening bracket that comes after
# it. Also, brackets can't overlap each other as in [(])

# Sample Input:
# string = "([])(){}(())()()"
#
# Sample Output:
# true

# O(n) time | O(n) space
# 3 cases unbalance:
# 1. if stack is not empty by end of string traversal, the string is unbalance, or there are opening brackets
# 2. traverse the string and a closing bracket left, there's nothing to match against, therefore it's unbalanced
# 3. final opening bracket does not match with the closing bracket

def balancedBrackets(string):
    openingBrackets = "{[("  # string/array of all opening brackets
    closingBrackets = "}])"  # string/array of all closing brackets
    matchingBrackets = {")": "(", "]": "[", "}": "{"}  # use a dictionary to map closing bracket with corresponding
    # opening bracket
    stack = []  # empty array
    for char in string:
        if char in openingBrackets:  # if current char is in openingBrackets, then store it to the stack
            stack.append(char)
        elif char in closingBrackets:  # if current char in closingBrackets:
            if len(stack) == 0:  # if stack is empty: return False
                print("False")
                return False
            elif stack[-1] == matchingBrackets[char]:  # if top item in stack matches corresponding closing bracket
                stack.pop()  # pop top item from the stack
            else:  # otherwise, it's a unbalanced stack, then return False
                # print("False")
                return False
    # print("true")
    return len(stack) == 0  # return True if the stack is empty; otherwise there's unmatched bracket/s

# balancedBrackets("(()[[{{}}]})")
# balancedBrackets("()[]{}{")
