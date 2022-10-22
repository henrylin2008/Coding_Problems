# Right View of a Binary Tree (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743902403_52Unit

# Problem Statement
#
# Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set
# of nodes visible when the tree is seen from the right side.

# Example 1:
#           1
#         /   \
#       2       3
#     /   \    /  \
#   4     5   6    7
# Right view: [1, 3, 7]
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
#    |
#    3
# Right view: [12, 1, 5, 3]

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# additional thing we will be doing is to append the last node of each level to the result array.

from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(0, levelSize):
            currentNode = queue.popleft()
            # if it is the last node of this level, add it to the result
            if i == levelSize - 1:
                result.append(currentNode)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()

# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is
# due to the fact that we traverse each node once.
#
# Space Complexity
# The space complexity of the above algorithm will be O(N) needed for the return list. We will also need O(N)
# space for the queue. Since we can have a maximum of N/2 nodes at any level (this could happen only at the lowest
# level), therefore we will need O(N) space to store them in the queue.
