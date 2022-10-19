# Level Order Successor (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743880609_49Unit

# Problem Statement
# Given a binary tree and a node, find the level order successor of the given node in the tree. The level order
# successor is the node that appears right after the given node in the level order traversal.


# Example 1:
#           1
#         /   \
#       2       3
#     /   \
#   4     5
# Given Node: 3
# Level Order Successor: 4

# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# Given Node: 9
# Level Order Successor: 10

# Example 3:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# Given Node: 12
# Level Order Successor: 7

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that we will not keep track of all the levels. Instead, we will keep inserting child nodes to the
# queue. As soon as we find the given node, we will return the next node from the queue as the level order successor.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        # break if we have found the key
        if currentNode.val == key:
            break

    return queue[0] if queue else None


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.val)

    result = find_successor(root, 12)
    if result:
        print(result.val)


main()