# 103. Binary Tree Zigzag Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Link: https://algo.monster/problems/binary_tree_zig_zag_traversal
# Medium

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to
# right, then right to left for the next level and alternate between).

# For example:
#               1          -------- Level 0         [ [1],
#             /   \
#            2     3       -------- Level 1           [3, 2],
#          /  \      \
#         4     5     6    -------- Level 2           [4, 5, 6],
#          \     \
#           7     8        -------- Level 3           [8, 7] ]

# Example 2:
# Input: root = [1]
# Output: [[1]]
#
# Example 3:
# Input: root = []
# Output: []

from collections import deque
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This problem is almost the same as level order traversal. We just have to keep a flag to track if we are currently
# traversing left-to-right or right-to-left.
#
# Time Complexity: O(n)
# We traverse every edge and node once but since the number of edges is n - 1, then this simply becomes O(n).
def zig_zag_traversal(root: Node) -> List[List[int]]:
    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    left_to_right = True    # flag to track traversing direction (left-to-right, right-to-left)
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level, see explanation above
        new_level = []
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            if node:
                new_level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if not left_to_right:
            new_level.reverse()  # reverse current level
        if new_level:
            res.append(new_level)
        left_to_right = not left_to_right  # flip flag
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
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))
