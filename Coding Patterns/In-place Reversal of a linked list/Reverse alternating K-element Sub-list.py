# Problem Challenge 1: Reverse alternating K-element Sub-list (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743804225_41Unit

# Problem Statement
#
# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# Ex:
# k = 2
# Original List:        head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null
# Reversed Sub-list:    head -> 2 -> 1 -> 3 -> 4 -> 6 -> 5 -> 7 -> 8 -> null

# Solution
#
# The problem follows the In-place Reversal of a LinkedList pattern and is quite similar to Reverse every K-element
# Sub-list. The only difference is that we have to skip ‘k’ alternating elements. We can follow a similar approach,
# and in each iteration after reversing ‘k’ elements, we will skip the next ‘k’ elements.
