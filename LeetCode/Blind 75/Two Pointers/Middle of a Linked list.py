# Middle of a Linked List
# https://algo.monster/problems/middle_of_linked_list

# Find the middle node of a linked list.
#
# Input: 0 1 2 3 4
#
# Output: 2
#
# If the number of nodes is even, then return the second middle node.
#
# Input: 0 1 2 3 4 5
#
# Output: 3

# Intuition

# If it was an array, then we can get its length and middle element trivially. For a linked list, we have to traverse
# it to find its length l. We can find l by traversing the list once and then find the middle element by traversing
# it again and stop on the l/2th element.
#
# Is there any way to traverse only once? We can use two pointers
#
#   -a fast pointer that moves 2 nodes at a time and
#   -a slow pointer that moves 1 node at a time
#
# Since the speed of the fast pointer is 2x of the slow pointer, by the time the fast pointer reaches the end the
# slow pointer should be at the eexact middle of the list.
#
# Time Complexity: O(n)
#
# Technically O(n/2) but again constants are cut out from the time complexity and so we are left with just O(n).

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def middle_of_linked_list(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow.val


def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)


if __name__ == '__main__':
    head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(head)
    print(res)
