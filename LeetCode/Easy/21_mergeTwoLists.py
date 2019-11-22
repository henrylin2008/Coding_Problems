# 21. Merge Two Sorted Lists
#
# link: https://leetcode.com/problems/merge-two-sorted-lists/
#
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes
# of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:

    def mergeTwoLists(self, l1, l2):
        curr = dummy = ListNode(0)
        # curr: current pointer
        # dummy: a dummy node, the goal is move the pointer from the end (when finished comparing) to the beginning of node
        # ListNode(0): beginning of the node

        while l1 and l2:
            if l1.val < l2.val: # when l1 value is less than l2 value
                curr.next = l1 # insert the smaller value (l1)
                l1 = l1.next # move the pointer to next l1 value, since the current value has been inserted into the list
            else:  # when l1 >= l2
                curr.next = l2 # insert l2
                l2 = l2.next # move the pointer to next (l2) value
            curr = curr.next # move the pointer of output to next node
        curr.next = l1 or l2 # for case: input: l1=[1,2,3,],l2=[4,5,6] or vice versa; as while loop (above) does not cover this case
        # append l2 into the end of l1 or vice versa

        return dummy.next

