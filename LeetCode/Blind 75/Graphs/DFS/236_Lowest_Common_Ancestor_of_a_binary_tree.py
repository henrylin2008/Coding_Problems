# 236. Lowest Common Ancestor of a Binary Tree
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Medium

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
# as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
#
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA
# definition.

# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the tree.

# DFS + Recursive
# Explanation: When we think as a node, there could be five scenarios of how we are relative to the LCA and two target
# nodes.
# Current node is the LCA
# 1. One target node is on the left subtree, the other target node on the right subtree, so the current node itself is
# the LCA.
#                   LCA  (current node)
#                  /    \
#                A        B
# 2. Current node is one of the target and the other node is in a subtree.
#           LCA/B (current node)
#           /
#         A
#
# Current node is not the LCA
# 3. Current node is not a target node and its subtrees has no target node.
#           LCA
#          /
#      (current node)
# 4. Current node is in the path between the LCA and a target node in case 2.
#                   LCA
#                 /
#            (current node)
#             /
#           A
# 5. LCA is in the subtree of the current node.
#                  (current node)
#                 /
#               LCA
#             /    \
#           A       B

# Time: O(n); n nodes and n - 1 edges: O(2n - 1) --> O(n)

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root, node1, node2):
    if not root:  # Empty node
        return

    # case 2 in above figure
    if root == node1 or root == node2:  # if either node is the root, return root
        return root

    # DFS on left, right subtrees
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    if left and right:  # if nodes are in the left and right subtree
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 4 and 5, report target node or LCA back to parent
    if left:    # if nodes are in left subtree, return left
        return left
    if right:   # if nodes are in right subtree, return right
        return right

    # case 4, not found return null
    return None


# solution #2: recursion
# Base case: if none or root is any of p and q: return root
# recursive calls on left/right subtree
# return root if left and right are True otherwise return left or right
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root in [p, q]:  # base case: if root does not exist or current root is one of node: return root
        return root
    l = self.lowestCommonAncestor(root.left, p, q)  # recursive call on left subtree
    r = self.lowestCommonAncestor(root.right, p, q)  # recursive call on right subtree
    return root if l and r else l or r  # if nodes are found in left (True) and right subtree (True), return root
    # else if lowest common ancestor found in either left or right subtree, return either left or right subtree
