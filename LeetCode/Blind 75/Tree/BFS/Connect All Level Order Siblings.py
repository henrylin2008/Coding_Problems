# Connect All Level Order Siblings (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743897497_51Unit

# Problem Statement
#
# Given a binary tree, connect each node with its level order successor. The last node of each level should point to
# the first node of the next level.

# Example 1:
#            1   -->
#         /    \
#  -->  2  -->   3  -->
#     /   \     /  \
# -> 4  --> 5-> 6 -> 7 --> null
#
# Example 2:
#           12  -->
#         /    \
#  -->  7   -->  1 --> null
#     /        /   \
# -> 9  -->  10  ->  5 --> null
#
