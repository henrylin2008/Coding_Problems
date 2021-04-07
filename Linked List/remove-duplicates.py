# link: https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List
# Remove Duplicates From Linked List
# Difficulty: Easy

# You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values. Write a
# function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values. The
# Linked List should be modified in place (i.e., you shouldn't create a brand new list), and the modified Linked List
# should still have its nodes sorted with respect to their values.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail of the list.

# Sample Input:
# linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 // the head node with value 1

# Sample Output:
# 1 -> 3 -> 4 -> 5 -> 6  // the head node with value 1

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n); one pass through all nodes in linked list
# Space: O(1); only modify the given linked list
# Logic: since the given linked list is sorted, thus we just need to find next distinct value (from current node), then
# set the next pointer of current node to the distinct node, until we reached the end (node with None value)
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList    # first/current node
    while currentNode is not None:  # while current node has a value (not end of linked list)
        nextDistinctNode = currentNode.next  # next distinct node is next node after current node
        # nextDistinctNode is not empty and current node matches next node
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next    # move to the following node
        # now we found a distinct node, set the pointer of next node to nextDistinctNode
        currentNode.next = nextDistinctNode  # point to next node after current node
        currentNode = nextDistinctNode  # update currentNode

    return linkedList
