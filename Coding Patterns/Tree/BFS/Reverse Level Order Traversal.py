# Reverse Level Order Traversal (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743852073_45Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e.,
# the lowest level comes first. You should populate the values of all nodes in each level from left to right in
# separate sub-arrays.
#
# Example 1:
#           1
#         /   \
#       2       3
#     /   \    /  \
#   4     5   6    7
# Reverse Level Order Traversal:
#           [[4,5,6,7],
#            [2,3],
#            [1]]
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    9       10     5
# Reverse Level Order Traversal:
#           [[9,10,5],
#            [7,1],
#            [12]]
#
# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that instead of appending the current level at the end, we will append the current level at the
# beginning of the result list.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()        # different from Level Order Traversal
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for i in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        if current_level:
            result.appendleft(current_level)        # different from level order traversal
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()

# Time Complexity
#
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is
# due to the fact that we traverse each node once.
#
# Space Complexity
#
# The space complexity of the above algorithm will be O(N) as we need to return a list containing the level order
# traversal. We will also need O(N) space for the queue. Since we can have a maximum of N/2 nodes at any level
# (this could happen only at the lowest level), therefore we will need O(N) space to store them in the queue.
