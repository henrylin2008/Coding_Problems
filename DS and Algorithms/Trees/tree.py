# Binary List implementation of a tree
# Recursive view:  [ key, left subtree, right subtree ]
# Each tree or sub tree (t) consist of a list with three elements:
#    t[0] is the node key
#    t[1] is the left sub tree or [] for no child on left
#    t[2] is the right sub tree or [] for no child on right
# Ex: (list representation)
# myTree = ['a',  # root
#           ['b',  # left subtree
#            ['d', [], []],
#            ['e', [], []]
#            ],
#           ['c',  # right subtree
#            ['f', [], []],
#            []
#            ]
#           ]
def BinaryTree(r):
    """constructs a list with a root node and two empty sublists for the children"""
    return [r, [], []]  # [root, left subtree, right subtree]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]

# r = BinaryTree(3)
# insertLeft(r,4)
# insertLeft(r,5)
# insertRight(r,6)
# insertRight(r,7)
# l = getLeftChild(r)
# print(l)      # [5, [4, [], []], []]
#
# setRootVal(l,9)
# print(r)      # [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
# insertLeft(l,11)
# print(r)      # [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
# print(getRightChild(getRightChild(r)))    # [6, [], []]
