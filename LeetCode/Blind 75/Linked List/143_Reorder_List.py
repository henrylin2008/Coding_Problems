# 143. Reorder List
# https://leetcode.com/problems/reorder-list/
# Difficulty: Medium

# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000

# Logic: divide the given list to 2 halves using slow and fast pointers, then reverse (pointers) the second half, and
# adjust the next pointers (first -> second -> first.next -> second.next -> first.next.next -> second.next.next ...)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        second = slow.next      # beginning of the second half
        slow.next = None        # end of the first half
        prev = None             # the pointer for first node of second half
        while second:           # while second half not null
            temp = second.next  # next node
            second.next = prev  # reverse link of beginning node
            prev = second       # move the pointer to the beginning of the second half
            second = temp       # move the pointer of second node of the second half

        # merge two halves
        first, second = head, prev          # prev: beginning of second half in reverse order (last node)
        while second:
            temp1, temp2 = first.next, second.next  # temp1: 2nd node of 1st half; temp2: 2nd node of 2nd half
            first.next = second             # first -> second
            second.next = temp1             # second -> first.next
            first, second = temp1, temp2    # move the pointers to the next nodes
