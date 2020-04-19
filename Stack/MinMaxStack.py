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

class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]