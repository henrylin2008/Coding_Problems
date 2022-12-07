# Reverse every K-element Sub-list (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743796880_40Unit

# Problem Statement
#
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# Ex:
# k = 3
# Original List:        head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null
#
# Reversed Sub-list:    head -> 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null

# Solution
#
# The problem follows the In-place Reversal of a LinkedList pattern and is quite similar to Reverse a Sub-list. The
# only difference is that we have to reverse all the sub-lists. We can use the same approach, starting with the first
# sub-list (i.e. p=1, q=k) and keep reversing all the sublists of size ‘k’.

