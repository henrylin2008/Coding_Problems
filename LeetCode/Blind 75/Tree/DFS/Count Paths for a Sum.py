# Count Paths for a Sum (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743955693_58Unit

# Problem Statement
#
# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each
# path equals ‘S’. Please note that the paths can start or end at any node but all paths must follow direction from
# parent to child (top to bottom).
#
# Example 1:
#           1
#         /   \
#       7       9
#     /   \    /  \
#   6     5   2    3
# S: 12
# Output: 3
# Explanation: There are three paths with sum '12': 7 -> 5, 1 -> 9 -> 2, and 9 -> 3
#
# Example 2:
#           12
#         /    \
#       7        1
#     /        /   \
#    4       10     5
# S: 11
# Output: 2
# Explanation: Here are the two paths with sum '11': 7 -> 4 and 1 -> 10
#
#
# Solution
#
# This problem follows the Binary Tree Path Sum pattern. We can follow the same DFS approach. But there will be four
# differences:
#   1. We will keep track of the current path in a list which will be passed to every recursive call.
#   2. Whenever we traverse a node we will do two things:
#       - Add the current node to the current path.
#       - As we added a new node to the current path, we should find the sums of all sub-paths ending at the current
#         node. If the sum of any sub-path is equal to ‘S’ we will increment our path count.
#   3. We will traverse all paths and will not stop processing after finding the first path.
#   4. Remove the current node from the current path before returning from the function. This is needed to Backtrack
#      while we are going up the recursive call stack to process other paths.


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    return count_paths_recursive(root, S, [])


def count_paths_recursive(currentNode, S, currentPath):
    if currentNode is None:
        return 0

    # add the current node to the path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sums of all sub-paths in the current path list
    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        # if the sum of any sub-path is equal to 'S' we increment our path count.
        if pathSum == S:
            pathCount += 1

    # traverse the left sub-tree
    pathCount += count_paths_recursive(currentNode.left, S, currentPath)
    # traverse the right sub-tree
    pathCount += count_paths_recursive(currentNode.right, S, currentPath)

    # remove the current node from the path to backtrack
    # we need to remove the current node while we are going up the recursive call stack
    del currentPath[-1]

    return pathCount


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
