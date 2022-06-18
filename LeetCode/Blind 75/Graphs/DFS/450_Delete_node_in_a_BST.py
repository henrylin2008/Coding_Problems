# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/
# Medium

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node
# reference (possibly updated) of the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
# Example 1:
#               5                         5
#             /   \                     /    \
#           3      6      ===>        4        6
#        /    \      \              /            \
#       2      4      7            2                7
#
#
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
#               5
#             /   \
#           2      6
#             \      \
#              4      7
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
#
#
# Example 3:
#
# Input: root = [], key = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:    # if empty: return None
            return None

        if root.val == key:
            # 4 possibilities
            if not root.left and not root.right:    # if no children: return None
                return None
            if not root.left and root.right:    # if only right children: return root.right
                return root.right
            if not root.right and root.left:    # if only left children: return root.left
                return root.left
            pointer = root.right
            while pointer.left:
                pointer = pointer.left
            root.val = pointer.val
            root.right = self.deleteNode(root.right, root.val)

        elif root.val > key:    # if root.val > key: key is on left subtree, recursive call on left subtree
            root.left = self.deleteNode(root.left, key)
        else:   # if root.val < key: key is on right subtree, recursive call on right subtree
            root.right = self.deleteNode(root.right, key)

        return root
