# Min Max Stack Construction:
# https://www.algoexpert.io/questions/Min%20Max%20Stack%20Construction
# Difficulty: Medium
#
# Write a MinMaxStack class for a Min Max Stack. The class should support:
#     - Pushing and popping values on and off the stack
#     - Peeking at the value at the top of the stack
#     - Getting both the minimum and the maximum values in the stack at any given point in tim
#
# All class methods, when considered independently, should run in constant time and with constant space.

# Sample Usage:
# // All operations below are performed sequentially.
# MinMaxStack(): -
# push(5): -
# getMin(): 5
# getMax(): 5
# peek(): 5
# push(7): -
# getMin(): 5
# getMax(): 7
# peek(): 7
# push(2): 0
# getMin(): 2
# getMax(): 7
# peek(): 2
# pop(): 2
# pop(): 7
# getMin(): 5
# getMax(): 5
# peek(): 5

# O(1) time | O(1) space
# idea: using 2 stacks, one stack is keep track of current stack, the other one (minMaxStack) keeps track of min and max
# at any given point;

class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):  # check last(est) item in the stack
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space
    def pop(self): # remove last item from the stack
        self.minMaxStack.pop() # pop last value from minMaxStack to be in sync with the main stack
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self, number): # adding new item to the stack
        newMinMax = {"min": number, "max": number} # use a directory/Hash table to store min and max values; This is only
                    # true if the first number is pushing to the stack, or number is first item pushing into the stack
        if len(self.minMaxStack): # if minMaxStack is not empty or there're values in the stack
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1] # peeking last value of minMaxStack
            newMinMax["min"] = min(lastMinMax["min"], number) # find min by comparing min of lastMinMax value and the number
            newMinMax["max"] = max(lastMinMax["max"], number) # find max by comparing max of lastMinMax value and the number
        self.minMaxStack.append(newMinMax) # if it's an empty stack, add newMinMax value to the minMaxStack
        self.stack.append(number) # if it's an empty stack, insert the number into the main stack

    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

#
# MinMaxStack.push(1,5)
# MinMaxStack.push(1,10)
# MinMaxStack.push(1,4)
# MinMaxStack.pop(4)
# MinMaxStack.getMin()
# print(MinMaxStack)
# MinMaxStack.getMax()
# print(MinMaxStack)