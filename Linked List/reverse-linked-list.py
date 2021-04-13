# link: https://www.algoexpert.io/questions/Reverse%20Linked%20List
# Reverse Linked List
# Difficulty: Hard

# Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a
# brand new list), and returns its new head.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail fo the list.
# You can assume that the input Linked List will always have at least one node; in other words, the head will never be
# None/null.

# Sample Input:
# head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0

# Sample Output:
# 5 -> 4 -> 3 -> 2 -> 1 -> 0  // the new head node with value 5


# Time: O(n); n is the length of the linked list
# Space: O(1); 3 pointers = O(3) -> O(1)
# Logic: set 3 pointers, place P2 at the beginning of the list, and P3 as P2.next; then reverse p2 pointer to P1
# (previous node), then shift all pointers to next node (P1, P2, P3 => P2, P3, P3.next)
# P3 = P2.next
# P2.next = P1  # reverse the P2 Pointer
# P1 = P2   # move P1 to P2
# P2 = P3   # move P2 to P3
def reverseLinkedList(head):
    previousNode, currentNode = None, head  # currentNode as the head of the list
    while currentNode is not None:
        nextNode = currentNode.next        # 3rd pointer, cleaner code with variable setup inside this loop
        currentNode.next = previousNode    # reverse the currentNode pointer
        previousNode = currentNode         # shift previousNode to currentNode
        currentNode = nextNode             # shift currentNode to nextNode
    return previousNode                    # return first pointer
