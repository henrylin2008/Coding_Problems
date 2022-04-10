# 98. Validate Binary Search Tree
# link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium

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
# Input: root = [2,1,3]
# Output: true
#
# Example 2:
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


# Time: O(n), O(2n) -> O(n); 2 comparisons, one on left, and one on right
# Space: O(1)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):   # (current_node, left boundary, right boundary)
            if not node:      # emtpy node is considered as True
                return True
            if not left < node.val < right:  # False if node.val is not between left and right boundaries
                return False
            # Recursive calls to check on the validations of the left subtree and right subtree, setting the boundaries
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        # validate if the tree is a BST
        return valid(root, float("-inf"), float("inf"))
