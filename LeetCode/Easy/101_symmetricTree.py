# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
#
# Given a binary tree, check whether it is a mirror of itself(ie, symmetric around its center).
#
# For example, this binary tree[1, 2, 2, 3, 4, 4, 3] is symmetric:
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following[1, 2, 2, null, 3, null, 3] is not:
#
#      1
#     / \
#    2   2
#     \   \
#     3    3

class Solution:
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None

    def isSymmetric(self, root):

        if root is None:  # if root is empty, then it's symmetric
            return True

        return self.isSymmetricRec(root.left, root.right)  # recursive call with 2 inputs (left, right)

    def isSymmetricRec(self, left, right): # Recursive function

        if left is None and right is None: # if left and right is empty, then it's symmetric
            return True

        if left is None or right is None or left.val != right.val:
            # False case 1: left is empty but not right;
            # False case 2: right is empty but not left
            # False case 3: left and right value are not equal

            return False

        return self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)
        # return true if:
        # left.left = right.right (ex above, tree[3] = tree[6], most left lower level = most right lower level
        # left.right = right.left (ex above, tree[4] = tree[5], right of lowest level of left subtree = left of lowest level of right subtree


# Solution.isSymmetric(1, [1,2,2,3,4,4,3])

