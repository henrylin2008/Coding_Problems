# Reverse a LinkedList (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743784192_38Unit

# Problem Statement
#
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the
# reversed LinkedList.
# Ex:
#
# Original List: head -> 2 -> 4 -> 6 -> 8 -> 10 -> null
# Reversed list: null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

# Solution
#
# To reverse a LinkedList, we need to reverse one node at a time. We will start with a variable current which will
# initially point to the head of the LinkedList and a variable previous which will point to the previous node that we
# have processed; initially previous will point to null.
#
# In a stepwise manner, we will reverse the current node by pointing it to the previous before moving on to the next
# node. Also, we will update the previous to always point to the previous node that we have processed. Here is the
# visual representation of our algorithm:
#
# previous = null   current -> 2 -> 4 -> 6 -> 8 -> 10 -> null
#                  current = head, previous = null
# null <- 2 <- previous  current -> 4 -> 6 -> 8 -> 10 -> null
# null <- 2 <- 4 <- previous  current -> 6 -> 8 -> 10 -> null
# null <- 2 <- 4 <- 6 <- previous  current -> 8 -> 10 -> null
# null <- 2 <- 4 <- 6 <- 8 <- previous  current -> 10 -> null
# null <- 2 <- 4 <- 6 <- 8 <- 10 <- previous  current -> null
# null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

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


def reverse(head):
    previous, current, next = None, head, None
    while current is not None:
        next = current.next  # temporarily store the next node
        current.next = previous  # reverse the current node
        # before we move to the next node, point previous to the current node
        previous = current
        current = next  # move on the next node
    return previous


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
