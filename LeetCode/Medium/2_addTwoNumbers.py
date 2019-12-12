# 2. Add Two Numbers
# link: https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
# and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

def addTwoNumbers(l1, l2):

    if l1 == None: # if l1 is empty; then return l2
        return l2

    if l2 == None: # if l2 is empty, then return l1
        return l1

    carry = 0 # carry = carryover number (ex: 9+2 ==> carry 1)
    dummy = ListNode(0) # set a pointer (staying) at the beginning of the list, and set to use for returning result
    p = dummy # pointer will be moving from left to the right (when adding values)

    while l1 and l2: # when l1 and l2 have same length and have value in each digit
        p.next = ListNode((l1.val+l2.val+carry) % 10) # return the reminder (ones digit)
        carry = (l1.val + l2.val + carry) // 10 # return the value in tens digit
        l1 = l1.next
        l2 = l2.next
        p = p.next

    # l1: 2 -> 4 -> 3
    # l2: 5 -> 6 -> 4 -> 1 (length of l2 is longer than l1; or vice versa)
    if l2: # if l2 still have extra value (while no more value at l1)
        while l2:
            p.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            l2 = l2.next
            p = p.next

    if l1: # if l1 still has value (and l2 has no more value)
        while l1:
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.next
            p = p.next

    if carry == 1: # if there's still carry value in last digit (ex: 358, 234 ==> rev(5821))
        p.next = ListNode(1)

    return dummy.next