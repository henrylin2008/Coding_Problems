# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
#
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # return valid function; min = -inf; max = inf
        return self.valid(root, float('-inf'), float('inf'))

    def valid(self, root, min, max):
        if not root: # empty BST = BST
            return True
        if root.val >= max or root.val <= min: #if root.val <= min or root.val >= max (out of range), return False
            return False
        #self.valid(root.left,min,root.val): left subtree;
        # root.left: root of left subtree; min=-inf (lower bound); root.val= right node (upper bound<root.val)
        #self.valid(root.right,root.val,max): right subtree;
        # root.right: root of right subtree; root.val: left node(lower bound>root.val), max=inf (upper bound, right node)
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)

Solution.isValidBST([2,1,3])
