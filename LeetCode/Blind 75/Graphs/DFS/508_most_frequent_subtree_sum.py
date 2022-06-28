# 508. Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/
# Medium

# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values
# with the highest frequency in any order.
#
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (
# including the node itself).
#
#
# Example 1:
#           5
#        /     \
#      2        -3
#
# Input: root = [5,2,-3]
# Output: [2,-3,4]
#
# Example 2:
#           5
#        /    \
#      2       -5
# Input: root = [5,2,-5]
# Output: [2]
#
#
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105


# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def dfs(node):
            if node is None:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            count[s] += 1
            return s

        count = collections.Counter()
        dfs(root)
        maxCount = max(count.values())
        return [s for s in count if count[s] == maxCount]
