# Time Complexity (average/worst):
# Access: O(n)
# Search: O(n)
# Insertion: O(1)
# Deletion: O(1)

class Element(object):
    """Single unit in a linked list"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head    # set head element, default to None

    def append(self, new_element):
        current = self.head
        if self.head:   # If the LinkedList already has a head
            while current.next:  # iterate through the next reference in every Element until reach the end of the list.
                current = current.next
            current.next = new_element
        else:   # if no head, set new_element as the head
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position > 1:    # when position it not at first element
            while current and counter < position:   # when there's a head node and counter < position
                if counter == position - 1:  # last position
                    new_element.next = current.next  # point new_element next reference to current.next
                    current.next = new_element  # point current's next reference to the new_element
                current = current.next  # move to next position
                counter += 1
        elif position == 1:   # if position at first element
            new_element.next = self.head    # point new_element.next pointer to the head
            self.head = new_element     # set the new_element as the head

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:  # not at head node and there's next pointer
            previous = current  # move previous to current position
            current = current.next  # move current to current.next position
        if current.value == value:  # if at the head
            if previous:    # if there's previous node
                previous.next = current.next    # direct previous' next pointer to current.next
            else:
                self.head = current.next    # new head at current.next
