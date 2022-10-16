# Zigzag Traversal (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743859019_46Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the
# values of all nodes of the first level from left to right, then right to left for the next level and keep
# alternating in the same manner for the following levels.
#
# Example 1:
#           [[1],
#            [3, 2],
#            [4, 5, 6, 7]]
#
# Example 2:
#           [[12],
#            [1, 7],
#            [9, 10, 5],
#            [17, 20]]

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# additional step we have to keep in mind is to alternate the level order traversal, which means that for every other
# level, we will traverse similar to Reverse Level Order Traversal.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    leftToRight = True
    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # add the node to the current level based on the traverse direction
            if leftToRight:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

        result.append(list(currentLevel))
        # reverse the traversal direction
        leftToRight = not leftToRight

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
