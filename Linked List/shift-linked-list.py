# link: https://www.algoexpert.io/questions/Shift%20Linked%20List
# Shift Linked List
# Difficulty: Hard

# Write a function that takes in the head of a Singly Linked List and an integer k, shifts the list in place (i.e.,
# doesn't create a brand new list) by k positions, and returns its new head.
# Shifting a Linked List means moving its nodes forward or backward and wrapping them around the list where appropriate.
# For example, shifting a Linked List forward by one position would make its tail become the new head of the linked
# list.
# Whether nodes are moved forward or backward is determined by whether k is positive or negative.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail of the list.
# You can assume that the input Linked List will always have at least one node; in other words, the head will never be
# None/null.

# Sample Input:
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5   // the head node with value 0
# k = 2

# Sample Output:
# 4 -> 5 -> 0 -> 1 -> 2 -> 3  // the new head node with value 4


# Time: O(n); n is the length of the linked list
# Space: O(1); b/c we are just updating the pointer/s
# position of tail = length - k  # k: given value
# 4 nodes that we care about:
#   - original tail node: traverse the entire linked list
#   - original head node: given
#   - new tail node: kth position from the original tail (length - k)
#   - new head node: new_tail.next
# 2 operations:
#   1. point tail node to the head node; tail.next = head
#   2. point new tail node to null node (tail); new_tail.next = None
# edge cases:
#   1. k = 0; return the original head
#   2. k is a large positive number: length % k = number of node/s to shift (forward)
#   3. k is negative; move kth position of node/s from the beginning of the linked list to the end; use % to get the
#      number of the nodes to shift
def shiftLinkedList(head, k):
    listLength = 1
    listTail = head
    while listTail is not None:
        listTail = listTail.next
        listLength += 1

    offset = abs(k) % listLength
    if offset == 0:
        return head

    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next

    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead
