# Reverse a Sub-list (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743790633_39Unit

# Problem Statement
#
# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
# Ex:
# Original List:   head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
#  p=2, q=4        head -> 1 -> 4 -> 3 -> 2 -> 5 -> null

# Solution
#
# The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in
# Reverse a LinkedList. Here are the steps we need to follow:
#   1. Skip the first p-1 nodes, to reach the node at position p.
#   2. Remember the node at position p-1 to be used later to connect with the reversed sub-list.
#   3. Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
#   4. Connect the p-1 and q+1 nodes to the reversed sub-list.

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    # after skipping 'p-1' nodes, current will point to 'p'th node
    current, previous = head, None
    i = 0
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1

    # we are interested in three parts of the LinkedList, the part before index 'p',
    # the part between 'p' and 'q', and the part after index 'q'
    last_node_of_first_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node

    i = 0
    # reverse nodes between 'p' and 'q'
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    # connect with the first part
    if last_node_of_first_part is not None:
        # 'previous' is now the first node of the sub-list
        last_node_of_first_part.next = previous
    # this means p == 1 i.e., we are changing the first node (head) of the LinkedList
    else:
        head = previous

    # connect with the last part
    last_node_of_sub_list.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

# Time Complexity
# The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
#
# Space Complexity
# We only used constant space, therefore, the space complexity of our algorithm is O(1).


# Similar Questions
#
# Problem 1: Reverse the first ‘k’ elements of a given LinkedList.
#
# Solution: This problem can be easily converted to our parent problem; to reverse the first ‘k’ nodes of the list,
# we need to pass p=1 and q=k.
