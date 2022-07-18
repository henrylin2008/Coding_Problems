# 102. Binary Tree Level Order Traversal
# Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# https://algo.monster/problems/binary_tree_level_order_traversal

# Given a binary tree, return its level order traversal. The input is the root node of the tree. The output should be
# a list of lists of integers, with the ith list containing the values of nodes on level i, from left to right.
#
# For example:
#               1          -------- Level 0         [ [1],
#             /   \
#            2     3       -------- Level 1           [2, 3],
#          /  \      \
#         4     5     6    -------- Level 2           [4, 5, 6],
#          \
#           7              -------- Level 3           [7] ]

# Output: [[1], [2,3], [4,5,6], [7]]

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
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time Complexity: O(n); We traverse every edge and node once but since the number of edges is n - 1 ==> O(n).

def level_order_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level
        new_level = []  # store child node/s
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            if node:  # if there's a node, in case of edge case of null node
                new_level.append(node.val)
                for child in [node.left, node.right]:  # enqueue non-null children
                    if child is not None:
                        queue.append(child)
                # for loop can be re-written with 2 append statements
                # queue.append(node.left)
                # queue.append(node.right)
        if new_level:   # if new_level is non-empty
            res.append(new_level)
    return res


# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
