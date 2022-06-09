# 113. Path Sum II
# Link: https://leetcode.com/problems/path-sum-ii/
# Medium

# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node
# values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.
#
# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.
#
# Example 1:
#                       5
#                   /       \
#                 4            8
#               /            /    \
#             11           13      4
#           /     \              /   \
#          7       2           5       1
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
#
# Example 2:
#               1
#            /     \
#          2         3
#
# Input: root = [1,2,3], targetSum = 5
# Output: []
#
# Example 3:
#
# Input: root = [1,2], targetSum = 0
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n)
    # Space: O(1)
    # Idea: run a dfs on subtrees, base case: if it's an empty tree: return False; else add current node value to the
    #       current sum; if it's a leaf node and cur_sum == target_sum: add current node value to the current path and
    #       append it to the final res list; recursive calls on the subtrees that are not empty (until it reaches the
    #       base case)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, cur_sum):
            if not node:    # empty Tree: False
                return False

            cur_sum += node.val     # add current node's value to the cur_sum
            if not node.left and not node.right and cur_sum == targetSum:  # if it's a leaf node and cur_sum==targetSum
                res.append(path + [node.val])   # add path + current node's value to the res list
            # recursive dfs calls on left/right subtrees if it's not the leaf node
            return dfs(node.left, path + [node.val], cur_sum) or dfs(node.right, path + [node.val], cur_sum)

        dfs(root, [], 0)    # dfs starts from the root node
        return res
