# BST Construction
# link: https://www.algoexpert.io/questions/BST%20Construction
# Difficulty: Medium

# Write a BST class for a Binary Search Tree. The class should support:
#   - Inserting values with the insert method
#   - Removing values with the remove method; this method should only remove the first instance of a given value
#   - Searching for values with the contains method
# Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node
# tree should simply not do anything.
# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node
# if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
# its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST
# nodes themselves or None/null.

# Sample Usage
# assume the following BST has already been created:
#               10
#             /    \
#            5      15
#          /  \    /  \
#         2    5  13   22
#        /          \
#       1            14

# all operations below are performed sequentially
# insert(12):
#               10
#             /    \
#            5      15
#          /  \    /  \
#         2    5  13   22
#        /       /  \
#       1      12    14
#
# remove(10):
#               12
#             /    \
#            5      15
#          /  \    /  \
#         2    5  13   22
#        /          \
#       1            14
#
# contains(15): true

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)
        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # this is a single-node tree; do nothing.
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
