# Post-order Traversal
# Post-order traversal visits the left subtree first, then the right subtree, and finally the current node.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def post_order_traversal(root: Node):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)


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
    post_order_traversal(root)
