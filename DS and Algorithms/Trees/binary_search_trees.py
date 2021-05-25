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
