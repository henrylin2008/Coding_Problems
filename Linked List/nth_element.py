# N-th element of a Linked list
# Implement a function that finds and returns the nth node in a linked list, counting from the end.
# Your function should take a linked list (its head element) and n, a positive integer as its arguments.

# ex:
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (null/None)
# the third element of head counting from the end is 3.

# head2 = 1 -> 2 -> 3 -> 4 -> (null/None)
# the fourth element of head2 counting from the end is 1.

# If the given n is larger than the number of nodes in the list, return null/None.

# Use this class to create linked lists.
class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)


# Main function: set 2 pointers (left & right) initially, move right pointer of nth position, if right pointer reaches
# null, then return null; else move left and right pointer with given nth distance at the same time, until the right
# pointer reaches the null, then return the left pointer
def nth_from_last(head, n):
    left = head
    right = head
    for i in range(n):
        if right is None:
            # print("None")
            return None
        right = right.child
    while right:
        left = left.child
        right = right.child
    # print("left:", left)
    return left


# It converts the given linked list into an easy-to-read string format.
# Example: 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)


# NOTE: The following input values will be used for testing your solution.
current = Node(1)
for i in range(2, 8):
    current = Node(i, current)
head = current
# head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

current2 = Node(4)
for i in range(3, 0, -1):
    current2 = Node(i, current2)
head2 = current2
# head2 = 1 -> 2 -> 3 -> 4 -> (None)


nth_from_last(head, 1)  # should return 1.
nth_from_last(head, 5)  # should return 5.
nth_from_last(head2, 2)   # should return 3.
nth_from_last(head2, 4)   # should return 1.
# nth_from_last(head2, 5)   # should return None.
# nth_from_last(None, 1)    # should return None.
