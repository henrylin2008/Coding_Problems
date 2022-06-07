# 112. Path Sum
# Link: https://leetcode.com/problems/path-sum/
# Easy

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
# adding up all the values along the path equals targetSum.
#
# A leaf is a node with no children.
#
# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.
#
# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.
#
# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time: O(n), Look through all the nodes in the tree
    # Space: O(h)/O(log(n)); h: height; log(n): balanced tree
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, cur_sum):
            if not node:  # empty tree: False
                return False

            cur_sum += node.val     # add current node's value to the current sum
            if not node.left and not node.right:    # if leaf node (no children)
                return cur_sum == targetSum         # return True if cur_sum == targetSum
            return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)  # run dfs on the subtrees on non-leaf node

        return dfs(root, 0)
