# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
# level by level).
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
# Example 2:
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
# Input: root = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# Note: iterative bfs, add prev level which doesn't have any nulls to the result;
# Create a res list and a level list, and use deque to popleft for the root node, then append child nodes into the
# level list, lastly append the level into the res list

# Time: O(n); visiting every node once
# Space: O(n); biggest tree: O(n/2) --> O(n)
# Definition for a binary tree node.
from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:  # q is not empty
            q_len = len(q)
            level = []      # one level at a time
            for i in range(q_len):
                node = q.popleft()
                if node:  # node is not null
                    level.append(node.val)
                    q.append(node.left)     # left child
                    q.append(node.right)    # right child
            if level:
                res.append(level)  # add each level to the result
        return res
