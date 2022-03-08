# 100. Same Tree
# link: https://leetcode.com/problems/same-tree/
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
#
# Example 1:
#
#
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:
#
#
# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:
#
#
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#
#
# Constraints:
#
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# note: recursive dfs on both trees at the same time; iterative bfs compare each level of both trees
#
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(p+q); size of p and q together
# Space: O(1)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:     # if both trees are empty
            return True
        if not p or not q or p.val != q.val:    # if one of the tree is not empty, or values of the node are not equal
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)    # recursive comparing nodes
