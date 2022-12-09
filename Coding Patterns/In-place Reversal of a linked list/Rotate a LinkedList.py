# Problem Challenge 2: Rotate a LinkedList (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743812259_42Unit

# Problem Statement
#
# Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’ nodes.

# Ex 1:
# k = 3
# Original List:        head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Rotated LinkedList:   head -> 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> null

# Ex 2:
# k = 8
# Original List:        head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
# Rotated LinkedList:   head -> 3 -> 4 -> 5 -> 1 -> 2 -> null

# Solution
# Another way of defining the rotation is to take the sub-list of ‘k’ ending nodes of the LinkedList and connect them
# to the beginning. Other than that we have to do three more things:
#   1. Connect the last node of the LinkedList to the head, because the list will have a different tail after the
#      rotation.
#   2. The new head of the LinkedList will be the node at the beginning of the sublist.
#   3. The node right before the start of sub-list will be the new tail of the rotated LinkedList.
