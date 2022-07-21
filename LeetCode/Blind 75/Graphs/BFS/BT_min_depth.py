# Binary Tree Min Depth
# https://algo.monster/problems/binary_tree_min_depth

# Given a binary tree, find the depth of the shallowest leaf node.
#                  1                --- Level 0
#               /     \
#             2         3           --- Level 1
#           /   \         \
#         4      5          6       --- Level 2
#           \      \
#            7      8               --- Level 3

# 6 is the shallowest leaf, with depth of 2


from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# With BFS, since we search level by level we are guaranteed to find shallowest leaf node earlier than other leaf nodes.
# Use a deque to pop node and add child node/s to the queue, as long as there's node in the queue, we add 1 to the
# depth, while removing the current node (popleft), and add its children node/s to the queue if it's not None node.

# Time: O(n)
# We traverse every edge and node once but since the number of edges is n - 1, then this simply becomes O(n).
def binary_tree_min_depth(root: Node) -> int:
    queue = deque([root])  # at least one element in the queue to kick start bfs
    depth = -1  # we start from -1 because popping root will add 1 depth
    while len(queue) > 0:  # as long as there is element in the queue
        depth += 1
        n = len(queue)  # number of nodes in current level
        for _ in range(n):  # dequeue each node in the current level
            node = queue.popleft()
            if node.left is None and node.right is None:  # found leaf node, early return
                return depth
            for child in [node.left, node.right]:
                if child is not None:
                    queue.append(child)
    return depth


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
    res = binary_tree_min_depth(root)
    print(res)


# test #1
# Input: 1 2 4 x 7 x x 5 x x 3 x 6 x x
# Output: 2

# Test #2
# Input: 0 x x
# Output: 0
