class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        """Insert new element as the head of the LinkedList"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """Delete the first (head) element in the LinkedList as return it"""
        if self.head:
            deleted_item = self.head
            temp = deleted_item.next
            self.head = temp
            return deleted_item
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        pass
