# Ternary Tree Paths
# https://algo.monster/problems/dfs_with_states

# Given a ternary tree (each node of the tree has at most three children), find all root-to-leaf paths.


#               1
#           /   |   \
#         2     4     6
#        /
#       3

# [ 1 -> 2 -> 3,
#   1 -> 4,
#   1 -> 6 ]


from typing import List


class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def ternary_tree_paths(root: Node) -> List[str]:
    def dfs(root, path, res):
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        for child in root.children:
            if child:
                # dfs(child, path + [str(root.val)], res)  # recursive call, additional space with a new list every time
                # use a single list path and push and pop following the call stack
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()

    res = []
    if root: dfs(root, [], res)
    return res


# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)


if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
