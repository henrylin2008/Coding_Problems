# Reverse a Sub-list (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743790633_39Unit

# Problem Statement
#
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
# Ex:
# Original List:   head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
#  p=2, q=4        head -> 1 -> 4 -> 3 -> 2 -> 5 -> null

# Solution
#
# The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in
# Reverse a LinkedList. Here are the steps we need to follow:
#   1. Skip the first p-1 nodes, to reach the node at position p.
#   2. Remember the node at position p-1 to be used later to connect with the reversed sub-list.
#   3. Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
#   4. Connect the p-1 and q+1 nodes to the reversed sub-list.
