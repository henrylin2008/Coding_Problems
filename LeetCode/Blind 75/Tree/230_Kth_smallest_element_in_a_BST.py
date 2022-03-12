# 230. Kth Smallest Element in a BST
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium

# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
# values of the nodes in the tree.
#
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
#
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3
#
# Constraints:
#
# The number of nodes in the tree is n.
# 1 <= k <= n <= 104
# 0 <= Node.val <= 104
#
#
# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth
# smallest frequently, how would you optimize?

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solve in iterative; traverse the tree in-order, keep going left child nodes until it reaches the null node, then pop
# the most recently added value in the stack, visit the parent node and then visit the right child, if it reaches the
# null node, then pop the most recently added value; if n == k, then return current node's value
# Time: O(H + k); H: tree height
# Space: O(H); H: tree height; worst case: O(N); average case: O(log n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0       # number of element visited
        stack = []  # stack to store visited node/s
        cur = root  # pointer for current node

        while cur or stack:         # while current node is not null or stack is not empty
            while cur:              # current is not null, keep going left
                stack.append(cur)   # add current to the stack
                cur = cur.left      # visit left child
            # cur is at the null
            cur = stack.pop()       # pop most recently added value
            n += 1                  # update visited node value
            if n == k:
                return cur.val
            cur = cur.right         # visit right subtree
