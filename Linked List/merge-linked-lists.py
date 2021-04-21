# Link: https://www.algoexpert.io/questions/Merge%20Linked%20Lists
# Merge linked lists
# Difficulty: Hard

# Write a function that takes in the heads of two Singly Linked Lists that are in sorted order, respectively. The
# function should merge the lists in place (i.e., it shouldn't create a brand new list) and return the head of the
# merged list; the merged list should be in sorted order.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail of the list.
# You can assume that the input linked list will always have at least one node; in other words, the heads
# will never be None/null.

# Sample Input:
# headOne = 2 -> 6 -> 7 -> 8  // the head node with value 2
# headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10 // the head node with value 1

# Sample Output:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 // the new head node with value 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Iterative Solution
# Time: O(n + m); n, m: length of both linked lists
# Space: O(1); Only using pointers
# Logic: set 3 pointers: p1 -> headOne, p2 -> headTwo, p1Prev -> the node before p1 (None as starting);
# p1Prev is use to keep track of the original p1/p2 pointer and .next pointer, while p1/p2 moving to the next node;
# Run while loop to compare 2 non-empty nodes between 2 linked lists, if p1.value < p2.value, then move p1Prev node to
# p1, and move p1 to p1.next; elif p1.value > p2.value, move p1Prev(or p1Prev.next) to p2, p2 to p2.next, and point
# p1Prev.next to p1. When reach to the end of a linked list, update p1Prev.next pointer to p2|p1 (depending which linked
# list runs out); lastly, return the head node that has a smaller value.
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne   # pointer 1 points to headOne
    p1Prev = None  # p1 previous node
    p2 = headTwo   # pointer 2 points to headTwo
    while p1 is not None and p2 is not None:  # when p1, p2 nodes are not empty nodes
        if p1.value < p2.value:  # in this case, keep moving p1 from linked list 1
            p1Prev = p1     # must move p1Prev to p1 position first
            p1 = p1.next    # then we can move p1 to p1.next position
        else:   # p1.value > p2.value,
            if p1Prev is not None:  # if p1Prev is not at the very beginning (p1Prev starts as None)
                p1Prev.next = p2    # points p1Prev.next to p2;
            # elif p1Prev is None: p2 is the head of the linked list 2
            p1Prev = p2    # must move p1Prev to p2 position first
            p2 = p2.next   # then we can move p2 to p2.next position
            p1Prev.next = p1    # points p1Prev.next (original p2.next) to p1
    if p1 is None:  # p1 reached the end of linked list 1, then links p1Prev (final node) to linked list 2
        p1Prev.next = p2   # point p1Prev.next (final node on linked list 1) to p2 (linked list 2)
    # if p2 is None: no further actions needed, as every node in linked list 1 are in the correct order
    return headOne if headOne.value < headTwo.value else headTwo  # return the head with the smaller value


# Recursive Solution:
# Time: O(n + m); n, m: length of the both linked list
# Space: O(n + m);
def mergeLinkedList(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo


def recursiveMerge(p1, p2, p1Prev):
    # base cases
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return

    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)
