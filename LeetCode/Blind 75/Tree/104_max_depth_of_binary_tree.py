# 104. Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy

# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest
# leaf node.
#
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
# Example 2:
# Input: root = [1,null,2]
# Output: 2
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Note: recursive dfs to find max-depth of subtrees; iterative bfs to count number of levels in tree

# Definition for a binary tree node.
from collections import deque
from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive solution
# Time: O(n)
# Space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# BFS solution: use queue to store node/s from each level (top down) until it reaches to an empty node;
#               ex: 1(l1) + 2(l2) + 3(l2) + 4(l3) + 5 (l4) + empty
# Time: O(n)
# Space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level


# Iterative DFS: use a stack to keep track the node and current depth (ex: [3 (node), 1 (depth)]) and return max depth
# Time: O(n)
# Space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]     # initial stack and current depth
        res = 1

        while stack:
            node, depth = stack.pop()   # pop current node (and its depth)

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])    # add left child node and increase the depth
                stack.append([node.right, depth + 1])   # add right child noe and increase the depth
        return res
