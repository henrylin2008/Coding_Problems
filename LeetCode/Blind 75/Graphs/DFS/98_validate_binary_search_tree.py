# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Medium

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#           2
#         /    \
#       1        3
# Input: root = [2,1,3]
# Output: true
#
# Example 2:
#               5
#           /       \
#        1             4
#                    /   \
#                  3       6
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(2n) => O(n); each node does 2 comparisons.
    # Note: The fact about a valid BST: left < node.value < right;
    #       Use a recursive function:
    #       base conditions:
    #               -Empty tree is a binary search
    #               -if any node broke the condition: return False
    #       recursive call on the left subtree: left boundary: left, right boundary: node.val
    #       recursive call on the right subtree: left boundary: node.val, right boundary: right
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if node is None:        # empty binary search tree is a binary search tree
                return True
            if not (left < node.val < right):   # if this condition is not true, return False;
                return False                    # found a node broke the binary search tree
            # recursive calls on left/right subtrees
            # (left subtree, left boundary, right boundary), (right subtree, left boundary, right boundary)
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)  # True if both are True
        # call the function (root, left boundary, right boundary)
        return valid(root, float('-inf'), float('inf'))
