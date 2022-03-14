# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder
# is the inorder traversal of the same tree, construct and return the binary tree.
#
# Example 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
# Example 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
# Constraints:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # ex 1: preorder = [3,  9,     20,15,7      ],        inorder = [9,          3,      15,20,7]
    #                  root, left, right subtree                 left (size:1) root,   right subtree (size:3)
    # Logic: recursive calls; first number in preorder is always the root, use this number to find the index of this
    #       value in the inorder, that helps to find the size of sub-arrays (anything to the left of the root is left
    #       sub-array, and anything to the right is the right subarray), the size helps for partition in preorder list
    #       (ex1: left: 1, right: 3), then recursive calls on the sub-arrays
    # Time: O(n^2); due to recursive stack
    # Space: O(N)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:     # base case: if given list is empty
            return None

        root = TreeNode(preorder[0])        # root is always the preorder[0]
        mid = inorder.index(preorder[0])    # index of the root in the inorder list
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
