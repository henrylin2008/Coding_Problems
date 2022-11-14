# Start of LinkedList Cycle (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743554403_14Unit

# Problem Statement

# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
# Ex: 
#               Cycle start
#                     |
# head -> 1 --> 2 --> 3 --> 4 --> 5 --> 6
#                     ^                 |
#                     | --------------- |
#                       
#                      Cycle start
#                           |
# head -> 1 --> 2 --> 3 --> 4 --> 5 --> 6
#                           ^           |
#                           | --------- |
#
#     Cycle start
#         |
# head -> 1 --> 2 --> 3 --> 4 --> 5 --> 6
#         ^                             |
#         | --------------------------- |