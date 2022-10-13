# Binary Tree Level Order Traversal (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743844952_44Unit

# Problem Statement
#
# Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of
# all nodes of each level from left to right in separate sub-arrays.

# Example 1:
#       level order traversal: [[1],
#                               [2,3],
#                               [4,5,6,7]]

# Example 2:
#       level order traversal: [[12],
#                               [7,1],
#                               [9,10,5]]
#
# Solution
#
# Since we need to traverse all nodes of each level before moving onto the next level, we can use the Breadth First
# Search (BFS) technique to solve this problem.
#
# We can use a Queue to efficiently traverse in BFS fashion. Here are the steps of our algorithm:
#   1. Start by pushing the root node to the queue.
#   2. Keep iterating until the queue is empty.
#   3. In each iteration, first count the elements in the queue (let’s call it levelSize). We will have these many nodes
#      in the current level.
#   4. Next, remove levelSize nodes from the queue and push their value in an array to represent the current level.
#   5. After removing each node from the queue, insert both of its children into the queue.
#   6. If the queue is not empty, repeat from step 3 for the next level.
# Let’s take the example-2 mentioned above to visually represent our algorithm:
