# Reverse every K-element Sub-list (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743796880_40Unit

# Problem Statement
#
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

# Ex:
# k = 3
# Original List:        head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null
#
# Reversed Sub-list:    head -> 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null

# Solution
#
# The problem follows the In-place Reversal of a LinkedList pattern and is quite similar to Reverse a Sub-list. The
# only difference is that we have to reverse all the sub-lists. We can use the same approach, starting with the first
# sub-list (i.e. p=1, q=k) and keep reversing all the sublists of size ‘k’.

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


def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head

    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        # after reversing the LinkedList 'current' will become the last node of the sub-list
        last_node_of_sub_list = current
        next = None  # will be used to temporarily store the next node
        i = 0
        while current is not None and i < k:  # reverse 'k' nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous

        # connect with the next part
        last_node_of_sub_list.next = current

        if current is None:
            break
        previous = last_node_of_sub_list
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()


# Time Complexity
# The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
#
# Space Complexity
# We only used constant space, therefore, the space complexity of our algorithm is O(1).

