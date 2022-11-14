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
# 
# Solution

# If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:
#   1. Take two pointers. Let’s call them pointer1 and pointer2.
#   2. Initialize both pointers to point to the start of the LinkedList.
#   3. We can find the length of the LinkedList cycle using the approach discussed in  LinkedList Cycle. Let’s assume that the length of the cycle is ‘K’ nodes.
#   4. Move pointer2 ahead by ‘K’ nodes.
#   5. Now, keep incrementing pointer1 and pointer2 until they both meet.
#   6. As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.
# Let’s visually see this with the above-mentioned Example-1:


# We can use the algorithm discussed in LinkedList Cycle to find the length of the cycle and then follow the above-mentioned steps to find the start of the cycle.