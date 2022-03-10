# 572. Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same
# structure and node values of subRoot and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The
# tree tree could also be considered as a subtree of itself.
#
#
# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
#
# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false

#
# Constraints:
#
# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:     # if subRoot is empty -> subtree of root
            return True
        if not root:        # if root is not emtpy and subRoot is empty
            return False
        if self.sameTree(root, subRoot):    # if both trees are the same
            return True
        # if subRoot is a subtree of either left or right of the root tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s, t):
        if not s and not t:  # if both trees empty
            return True
        if s and t and s.val == t.val:  # if both trees are not empty and values are the same
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False  # at least one tree is empty and another is not empty
