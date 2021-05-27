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

    # _put to search the tree according to the following algorithm:
    # -Starting at the root of the tree, search the binary tree comparing the new key to the key in the current node.
    #  If the new key is less than the current node, search the left subtree. If the new key is greater than the current
    #  node,search the right subtree.
    # -When there is no left (or right) child to search, we have found the position in the tree where the new node
    #  should be installed.
    # -To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the
    #  previous step.
    # Note: following code does not work correctly if you put a key value that is already in the tree
    def put(self, key, val):
        if self.root:  # if root exist
            self._put(key, val, self.root)  # recursive method _put(key, value, node) to insert the key in the subtree
        else:  # else if the tree does not have a root
            self.root = TreeNode(key, val)  # just add TreeNode(key, value) as root
        self.size = self.size + 1  # increment size

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():  # if it has left child, recursive call _put() method to insert the key/value
                self._put(key, val, currentNode.leftChild)
            else:  # if no left child, just add the new node with (key, value) as the left child
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():  # if it has right child,
                self._put(key, val, currentNode.rightChild)  # recursive call _put() method to insert the key/value
            else:  # if no right child, just add the new node with (key, value) as the right child
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)  # find node with key, resource
            if res:
                return res.payload
            else:
                return None
        else:  # no root, empty tree
            return None

    def _get(self, key, currentNode):
        """ recursive find key from currentNode or return None"""
        if not currentNode:  # return None if it's None
            return None
        elif currentNode.key == key:  # found the key
            return currentNode  # return current node
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)  # recursive call on left child
        else:
            return self._get(key, currentNode.rightChild)  # recursive call on right child

    def __getitem__(self, key):
        """ define [] operator i.e. g['key']"""
        return self.get(key)

    def __contains__(self, key):
        """define in operator; simply call get and return True if get returns a value, or False if it returns None. """
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():  # leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():  # interior
            successor = currentNode.findSuccessor()
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload

        else:  # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


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
