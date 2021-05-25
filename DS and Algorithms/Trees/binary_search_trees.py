# Binary Search Trees
# Search Tree Operations
# -Map() Create a new, empty map.
# -put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with
#  the new value.
# -get(key) Given a key, return the value stored in the map or None otherwise.
# -del Delete the key-value pair from the map using a statement of the form del map[key].
# -len() Return the number of key-value pairs stored in the map.
# -in Return True for a statement of the form key in map, if the given key is in the map.

class BinarySearchTree:

    def __init__(self):  # construct empty BST
        self.root = None  # point to a TreeNode
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):  # implement len(tree) operator
        return self.size

    def __iter__(self):  # provide iteration over nodes
        return self.root.__iter__()


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):  # root node if no parent node
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

