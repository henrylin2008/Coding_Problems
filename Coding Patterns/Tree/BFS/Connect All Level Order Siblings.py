# Connect All Level Order Siblings (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743897497_51Unit

# Problem Statement
#
# Given a binary tree, connect each node with its level order successor. The last node of each level should point to
# the first node of the next level.

# Example 1:
#            1   -->
#         /    \
#  -->  2  -->   3  -->
#     /   \     /  \
# -> 4  --> 5-> 6 -> 7 --> null
#
# Example 2:
#           12  -->
#         /    \
#  -->  7   -->  1 --> null
#     /        /   \
# -> 9  -->  10  ->  5 --> null
#
#
# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that while traversing we will remember (irrespective of the level) the previous node to connect
# it with the current node.

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    currentNode, previousNode = None, None
    while queue:
        currentNode = queue.popleft()
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()

# Time Complexity
#
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is
# due to the fact that we traverse each node once.
#
# Space Complexity
#
# The space complexity of the above algorithm will be O(N) which is required for the queue. Since we can have a
# maximum of N/2 nodes at any level (this could happen only at the lowest level), therefore we will need O(N)
# space to store them in the queue.
