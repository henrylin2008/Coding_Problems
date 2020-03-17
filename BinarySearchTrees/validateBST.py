# https://www.algoexpert.io/questions/Validate%20BST
# Validate BST
# You are given a Binary Tree data structure consisting of Binary Tree nodes. Each Binary Tree node has an integer value
# stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively.
# Children nodes can either be Binary Tree nodes themselves or the None (null) value. Write a function that returns a
# boolean representing whether or not the Binary Tree is a valid BST. A node is said to be a BST node if and only if it
# satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less
# than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves
# or None (null) values.

# hint #1:
# Every node in the BST has a maximum possible value and a minimum possible value. In other words, the value of any
# given node in the BST must be strictly smaller than some value (the value of its closest right parent) and must be
# greater than or equal to some other value (the value of its closest left parent).
#
# Hint #2:
# Validate the BST by recursively calling the validateBst function on every node, passing in the correct maximum and
# minimum possible values to each. Initialize those values to be -Infinity and +Infinity.

# Use recursive calls
# Time: O(n), n = number of nodes
# Space: O(d), d = depth of the tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def validateBst(tree):
        return validateBSTHelper(tree, float('-inf'), float('inf')) # recursive call

    def validateBSTHelper(tree, minValue, maxValue):
        if tree is None: # check if we're at leave node, return true if we are
            return True
        if tree.value < minValue or tree.value >= maxValue: # return false if value is out of the range
            return False
        leftIsValid = validateBSTHelper(tree.left, minValue, tree.value) # check left subtree is valid;
                                        #  maxValue = value of current node
        return leftIsValid and validateBSTHelper(tree.right, tree.value, maxValue) # return True if left and right nodes are valid


# https://www.educative.io/courses/coderust-hacking-the-coding-interview/jqBDy
