# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
# Remove Kth Node from End
# Difficulty: Medium

# Write a function that takes in the head of a Singly Linked List and an integer K and removes the kth node from the end
# of the list.
# The removal should be done in place, meaning that the original data structure should be mutated (no new structure
# should be created).
# Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done,
# even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed
# to be removed, your function should simply mutate its value and next pointer
# Note that your function doesn't need to return anything.
# You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail of the list.

# Sample Input:
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9  // the head node with value 0
# k = 4

# Sample Output
# No output required.
# The 4th node from the end of the list (the node with value 6) is removed.
# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n); n: length of the linked list
# Space: O(1)
# Logic: set 2 pointers; second pointer is k nodes ahead of first pointer; 2 cases for the second node; first case, when
# second pointer reaches the end node, the first pointer is the node to be removed, update the first node value to the
# value of next node, then point head.next to the head.next.next (the following node). second case is second node is
# somewhere in the linked list, then just have to move both pointers simultaneously.
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head    # first pointer
    second = head   # second pointer
    while counter <= k:     # set the second pointer
        second = second.next    # move second pointer to the next
        counter += 1            # increment the counter
    # second pointer: 2 cases; first is at end of linked list, or somewhere in middle of the linked list
    if second is None:  # edge case: when second pointer reaches the null node; first pointer is kth node to be removed
        head.value = head.next.value   # update head node's value to the value of next node
        head.next = head.next.next     # update head's pointer to the following node
        return  # do nothing after
    while second.next is not None:  # when second pointer is middle of linked list, then move both pointers
        second = second.next  # move second pointer to the next
        first = first.next    # move first pointer to the next
    # first is pointing to the node right before the node we want to remove (bc while loop (above), and second is the
    # node right before null node), which mean it is the node before the null node
    # first.next = Node_To_Remove
    # first.next = Node_To_Remove.next  # update the pointer to the node after the node to be removed
    first.next = first.next.next
