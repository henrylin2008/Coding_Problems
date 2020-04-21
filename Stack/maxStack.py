# Max Stack:
# 716: https://leetcode-cn.com/problems/max-stack/
# Difficulty: Easy
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements,
#             only remove the top-most one.
# Example 1:
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# Note:
# -1e7 <= x <= 1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.

# Time: O(n) | Space: O(n)
class MaxStack(list):
    def push(self, x):
        m = max(x, self[-1][1] if self else None)
        self.append((x, m))

    def pop(self):
        return list.pop(self)[0]

    def top(self):
        return self[-1][0]

    def peekMax(self):
        return self[-1][1]

    def popMax(self):
        m = self[-1][1]
        b = []
        while self[-1][0] != m:
            b.append(self.pop())

        self.pop()
        map(self.push, reversed(b))
        return m