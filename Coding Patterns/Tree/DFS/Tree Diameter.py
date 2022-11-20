# Tree Diameter (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743963987_59Unit
#
# Problem Statement
#
# Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest
# path between any two leaf nodes. The diameter of a tree may or may not pass through the root.
#
# Note: You can always assume that there are at least two leaf nodes in the given tree.
# Example 1:
#           1
#         /    \
#       2        3
#     /        /   \
#    4        5     6
# Output: 5
# Explanation: The diameter of the tree is: [4, 2, 1, 3, 6]
#
# Example 2:
#           1
#         /    \
#       2        3
#              /   \
#             5     6
#           /   \   |
#         7     8   9
#               |   |
#              10  11
# Output: 7
# Explanation: The diameter of the tree is: [10, 8, 5, 3, 6, 9, 11]

# Solution
#
# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. There will be a few
# differences:
#   1.At every step, we need to find the height of both children of the current node. For this, we will make two
#     recursive calls similar to DFS.
#   2.The height of the current node will be equal to the maximum of the heights of its left or right children, plus
#     ‘1’ for the current node.
#   3.The tree diameter at the current node will be equal to the height of the left child plus the height of the right
#     child plus ‘1’ for the current node: diameter = leftTreeHeight + rightTreeHeight + 1. To find the overall tree
#     diameter, we will use a class level variable. This variable will store the maximum diameter of all the nodes
#     visited so far, hence, eventually, it will have the final tree diameter.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        # if the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        if leftTreeHeight != 0 and rightTreeHeight != 0:
            # diameter at the current node will be equal to the height of left subtree +
            # the height of right sub-trees + '1' for the current node
            diameter = leftTreeHeight + rightTreeHeight + 1

            # update the global tree diameter
            self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1


def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()

# Time Complexity
# The time complexity of the above algorithm is O(N), where ‘N’ is the total number of nodes in the tree. This is
# due to the fact that we traverse each node once.
#
# Space Complexity
# The space complexity of the above algorithm will be O(N) in the worst case. This space will be used to store
# the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one
# child).

