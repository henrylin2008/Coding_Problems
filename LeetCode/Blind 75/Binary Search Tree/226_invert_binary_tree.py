# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Easy

# Given the root of a binary tree, invert the tree, and return its root.
#
#
# Example 1:
#              4                                        4
#            /    \                                   /    \
#          2        7               ==>             7        2
#        /   \     /  \                            /  \     /  \
#       1     3   6    9                          9    6   3    1
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
#
# Example 2:
#           2                                           2
#        /    \                                       /   \
#       1      3                                    3       1
# Input: root = [2,1,3]
# Output: [2,3,1]
#

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

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n); n is the size of the tree
    # Idea: simply switch the left and right nodes
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
