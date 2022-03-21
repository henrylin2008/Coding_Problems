# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy

# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2:
# Input: head = [1,2]
# Output: [2,1]
#
# Example 3:
# Input: head = []
# Output: []
#
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative solution: using 2 pointers: prev (Null), current (head), set a temp var as the current.next, then set the
# current.next to prev (null), repeat the process until no more current node
# Time: O(n); it needs to run through the entire linked list
# Space: O(1); only using the pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    # Recursive solution: if there's node at head.next, recursive call on the sub-list, and set the next node as the new
    #                     head, and point the original head to the null
    # Time: O(n)
    # Space: O(n); the solution requires to store every node
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     new_head = head     # new_head: temp var
    #     if head.next:       # if there's a next node/sub-problem (recursive)
    #         new_head = self.reverseList(head.next)  # new_head is the next node (reverse order)
    #         head.next.next = head       # reverse the list
    #     head.next = None   # if head is the first node in the list, then set the head next node to Null
    #
    #     return new_head
