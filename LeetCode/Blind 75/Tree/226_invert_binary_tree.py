# 226. Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
#
# Given the root of a binary tree, invert the tree, and return its root.
#
# Example 1:
#
#
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:
#
#
# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:
#
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100


# solution: recursive dfs to invert subtrees; bfs to invert levels, use collections.deque; iterative dfs is easy
# with stack if doing pre-order traversal

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:    # if root is empty
            return None
        # swap the children
        root.left, root.right = root.right, root.left

        # recursive invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
