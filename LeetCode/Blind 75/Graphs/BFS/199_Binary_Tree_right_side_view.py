# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
# https://algo.monster/problems/binary_tree_right_side_view
# Medium

# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
# you can see ordered from top to bottom.

# Example 1:
#               1
#            /     \
#          2         3
#           \          \
#             5          4
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#
# Example 2:
# Input: root = [1,null,3]
# Output: [1,3]
#
# Example 3:
# Input: root = []
# Output: []

# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# We can do a level order traversal and add the last node to return the result.
#
# Time Complexity: O(n)
#
# We traverse every edge and node once but since the number of edges is n - 1, then this simply becomes O(n).

def binary_tree_right_side_view(root):
    if not root:    # edge case
        return None

    res = []
    queue = deque([root])  # at least one element in the queue to kick start bfs
    while len(queue) > 0:  # as long as there is element in the queue
        n = len(queue)  # number of nodes in current level
        res.append(queue[0].val)  # only append the first node we encounter since it's the rightmost
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            for child in [node.right, node.left]:  # we add right children first, so it'll pop out of the queue first
                if child is not None:
                    queue.append(child)
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
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))
