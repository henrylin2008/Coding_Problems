# link: https://www.algoexpert.io/questions/Find%20Loop
# Find Loop
# Difficulty: Hard

# Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail
# node points to some node in the list instead of None/null). The function should return the node (the actual node-not
# just its value) from which the loop originates in constant space.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

# Sample Input:
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6    // the head node with value 0
#                            ^         v
#                            9 <- 8 <- 7

# Sample Output:
# 4 -> 5 -> 6   // the node with value 4
# ^         v
# 9 <- 8 <- 7


# Time: O(n)
# Space: O(1); since we are using 2 pointers, and not storing anything.
# Logic: set 2 pointers, first pointer (F) walks one node each time, while second pointer (S) walks two nodes each time;
# S = 2F; when 2 pointers meet at some point in the linked list, reset first pointer back to the head, then walk one
# node each time simultaneously for both pointers, until both pointers meet again; then that's the node that we want to
# return (either first pointer or second pointer).
def findLoop(head):
    first = head.next   # first node (after head)
    second = head.next.next  # To ensure it enters the following While loop
    while first != second:   # when two nodes are not the same
        first = first.next   # move one node
        second = second.next.next   # move two nodes
    first = head        # reset first pointer
    while first != second:
        first = first.next      # move to next node
        second = second.next    # move to next node
    return first    # return either first or second (where 2 nodes meet) would work
