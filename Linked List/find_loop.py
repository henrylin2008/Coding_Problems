# link: https://www.algoexpert.io/questions/Find%20Loop
# Find Loop
# Difficulty: Hard

# Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's tail
# node points to some node int he list instead of None/null). The function should return the node (the actual node-not
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
def findLoop(head):
    first = head.next
    second = head.next.next   # To
    while first != second:
        first = first.next
        second = second.next.next
    first = head        # reset first pointer
    while first != second:
        first = first.next
        second = second.next
    return first    # either first or second (when 2 nodes meet)
