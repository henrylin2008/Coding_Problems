# 94. Binary Tree Inorder Traversal
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Difficulty: Easy

# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
# Example 1:
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]
#
# Example 2:
#
# Input: root = []
# Output: []
#
# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    # iterative solution: use a pointer for current position and stack to store/pop nodes while traverse the tree, keep
    # moving to the left subtree until it reaches a null node, then pop most recently added the node, store its value
    # to the result list, then move the right subtree and repeat the same process, until there's no more in stack/cur
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root                  # pointer for current location
        stack = []                  # stack to keep track of the nodes
        while stack or cur:         # while stack and cur not empty
            while cur:              # while cur is not null
                stack.append(cur)   # add cur to the stack
                cur = cur.left      # move the pointer to the left subtree
            cur = stack.pop()       # pop recently added node/value
            res.append(cur.val)     # add popped item into the res
            cur = cur.right         # move to the right subtree
        return res
