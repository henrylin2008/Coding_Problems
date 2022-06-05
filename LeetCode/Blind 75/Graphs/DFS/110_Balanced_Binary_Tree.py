# 110. Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Easy

# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# Example 3:
# Input: root = []
# Output: true
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n); only visit every node once, use bottom-up DFS
    # Idea: use the bottom-up DFS to calculate the height of the subtrees, then pass on the calculated height of
    #       the subtrees to the parent node, ensure the height difference is no more than 1, and recursive calls until
    #       it reaches the top of the tree
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:    # empty tree
                return [True, 0]    # [True/False, height]

            left, right = dfs(root.left), dfs(root.right)   # dfs on the left, right subtrees
            # tree is balanced if left/right subtrees returns True, and root subtree is balanced (abs(l[1] - r[1] <= 1)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]   # [is tree balanced from the root, height of the tree]
        return dfs(root)[0]    # [True/False], idx: 0
