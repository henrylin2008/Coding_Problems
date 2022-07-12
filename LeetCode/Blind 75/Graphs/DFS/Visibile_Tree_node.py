# Visible Tree Node | Number of Visible Nodes

# In a binary tree, we define a node "visible" when no node on the root-to-itself path (inclusive) has a greater
# value. The root is always "visible" since there are no other nodes between the root and itself. Given a binary
# tree, count the number of "visible" nodes.
#
# Input:
#               5
#             /    \
#            4      6
#           / \
#         3    8
#
#       Visible nodes: 5, 6, 8
# Output: 3
#
# For example: Node 4 is not visible since 5>4, similarly Node 3 is not visible since both 5>3 and 4>3. Node 8 is
# visible since all 5<=8, 4<=8, and 8<=8.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def visible_tree_node(root: Node) -> int:
    def dfs(root, max_sofar):
        if not root:
            return 0

        total = 0
        if root.val >= max_sofar:
            total += 1

        total += dfs(root.left, max(max_sofar, root.val))
        # max_sofar for child node is the larger of previous max and current node val
        total += dfs(root.right, max(max_sofar, root.val))

        return total

    # start max_sofar with the smallest number possible so any value root has is smaller than it
    return dfs(root, -float('inf'))


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
    res = visible_tree_node(root)
    print(res)
