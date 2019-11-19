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

        if root is None:
            return True

        return Solution.isSymmetricRec(root.left, root.right)

    def isSymmetricRec(self, left, right):

        if left is None and right is None:
            return True

        if left is None or right is None or left.val != right.val:
            return False

        return self.isSymmetricRec(left.left, right.right) and self.isSymmetricRec(left.right, right.left)



# Solution.isSymmetric(1, [1,2,2,3,4,4,3])

