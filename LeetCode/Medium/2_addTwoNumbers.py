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
    dummy = ListNode(0) # set a pointer (staying) at the beginning of the list, and use it to return the result
    p = dummy # pointer will be moving from left to the right (when adding values)

    while l1 and l2: # when l1 and l2 have same length and have value in each digit
        p.next = ListNode((l1.val+l2.val+carry) % 10) # move pointer to next node (ones digit)
        # l1.val+l2.val+carry) % 10 = value in ones digit = reminder
        carry = (l1.val + l2.val + carry) // 10 # calculate carry value = value in tens digit
        l1 = l1.next # move (pointer of) l1 to the next (for next loop)
        l2 = l2.next # move (pointer of) l2 to the next (for next loop)
        p = p.next # move pointer to the next (for next loop) 

    # case where len(l2) > len(l1)
    # l1: 2 -> 4 -> 3
    # l2: 5 -> 6 -> 4 -> 1 (length of l2 is longer than l1; or vice versa)
    if l2: # if l2 still has (next) value (while l1 has no more)
        while l2:
            p.next = ListNode((l2.val + carry) % 10) # move pointer to next node
            carry = (l2.val + carry) // 10
            l2 = l2.next # move (pointer of) l2 to the next
            p = p.next # move pointer to the next

    # case where len(l1) > len(l2)
    # l1: 2 -> 4 -> 3 -> 5
    # l2: 5 -> 6 -> 4
    if l1: # if l1 still have value (and l2 has no more value)
        while l1:
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            l1 = l1.nexts
            p = p.next

    # case where (last) carry value needs to be added to the ListNode
    if carry == 1: # ex: 358, 234 ==> rev(5821)
        p.next = ListNode(1)

    return dummy.next # return the value from the beginning, where dummy (pointer) is sitting at

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# if __name__ == '__main__':
#     main()

# addTwoNumbers([2,4,3], [5,6,4])