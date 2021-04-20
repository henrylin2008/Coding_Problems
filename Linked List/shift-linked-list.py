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


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Time: O(n); n is the length of the linked list
# Space: O(1); b/c we are just updating the pointer/s
# position of new tail = length - k  # k: given value
# 4 nodes that we care about:
#   - original tail node: traverse the entire linked list
#   - original head node: given
#   - new tail node: kth position from the original tail; length - k if k > 0, else k position
#   - new head node: new_tail.next
# 2 operations:
#   1. point tail node to the head node; tail.next = head
#   2. point new tail node to null node (tail); new_tail.next = None
# edge cases:
#   1. k = 0; return the original head
#   2. k is a large positive number: k % length = reminder = number of node/s to shift forward
#         ex: 0 -> 1 -> 2 -> 3 -> 4 -> 5    8 % 6 = 2 (shift 2 nodes forward)
#     result: 4 -> 5 -> 0 -> 1 -> 2 -> 3
#   3. k is negative; move kth position of node/s from the beginning of the linked list to the end; use % to get the
#      number of the nodes to shift; position of new tail = abs(k)
# Logic: four nodes that we care about: the original head, original tail, new head, and new tail; Using a While loop
#        to get the original list tail and the length, then Use a formula (offset = abs(k) % listLength) to find out
#        the new tail position; then update/get the positions of the following nodes: new head, new tail.next (None),
#        the original tail points to the original head, then return the new head
def shiftLinkedList(head, k):
    # Iterate through entire linked list to get its tail and its length
    listLength = 1     # initialize the length of the list
    listTail = head    # to get the tail of the list
    while listTail.next is not None:  # while not at the tail
        listTail = listTail.next      # get the new tail
        listLength += 1               # increment the length
    # formula to get the number of offset nodes from the beginning (k<0) or the end of the linked list (k>0)
    offset = abs(k) % listLength
    if offset == 0:     # either k == 0 or abs(k) % length == 0: return the head of the list
        return head

    newTailPosition = listLength - offset if k > 0 else offset  # if k > 0: newTail = length-offset (from the tail)
    # elif k < 0: newTail = offset (from beginning of list)
    newTail = head      # start from the head
    for i in range(1, newTailPosition):  # To get the new tail
        newTail = newTail.next  # move newTail to the next node
    # set new head, remove reference of newTail.next, then points the originalTail
    # to the original head, then return new head; sequence must be as follow
    newHead = newTail.next      # reference to the new head
    newTail.next = None         # set new tail next node; safely remove reference of newTail.next
    listTail.next = head        # original tail links to the original head
    return newHead              # return new head list
