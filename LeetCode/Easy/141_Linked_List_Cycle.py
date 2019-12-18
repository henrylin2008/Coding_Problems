# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
# linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
#
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.
#
#
# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
#
# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
#
# Follow up:
# Can you solve it using O(1) (i.e. constant) memory?

def hasCycle(head):
    fast, slow = head, head # fast = 2x node (jump every other node); slow = 1x node
    # Idea: fast and slow will eventually meet at some point if it has a cycle
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next # fast = 2 steps; slow = 1 step
        if fast == slow: # when fast and slow met at some point, then return True (it has a cycle) 
            return True
    return False
