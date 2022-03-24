# 19. Remove Nth Node From End of List
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
# Follow up: Could you do this in one pass?

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Idea: set up a dummy node (a node before the head), and use 2 pointers (left, right), dummy --> left --> +n --> right
#       keep shifting the 2 pointers to the right until it reaches the end, then left.next = left.next.next, return
#       dummy.next

# Time: O(n);
# Space: O(1); using 2 pointers technique
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # find the right pointer: right = head + n
        while n > 0 and right:
            right = right.next  # keep shift right
            n -= 1
        # move both pointers until right pointer reaches the end
        while right:
            left = left.next
            right = right.next
        # delete (left.next) node
        left.next = left.next.next      # remove the next node
        return dummy.next
