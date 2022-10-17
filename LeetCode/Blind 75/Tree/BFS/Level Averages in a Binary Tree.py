# Level Averages in a Binary Tree (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743864804_47Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent the averages of all of its levels.

# Example 1:
#           1
#         /   \
#       2       3
#     /   \    /  \
#   4     5   6    7
#   Level Averages: [1, 2.5, 5.5]
#
# Example 2:
#           12
#         /    \
#       7        1
#     /   \    /   \
#    9     2  10    5

# Solution
#
# This problem follows the Binary Tree Level Order Traversal pattern. We can follow the same BFS approach. The only
# difference will be that instead of keeping track of all nodes of a level, we will only track the running sum of the
# values of all nodes in each level. In the end, we will append the average of the current level to the result array.

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        level_sum = 0.0
        for i in range(level_size):
            current_node = queue.popleft()
            # add the node's value to the running sum
            level_sum += current_node.val
            # insert the children of current node to the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        # append the current level's average to the result array
        result.append(level_sum / level_size)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
