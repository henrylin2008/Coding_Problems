# Stack methods:
# Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
# push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
# pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
# peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
# isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items on the stack. It needs no parameters and returns an integer.


# Build a stack with a LinkedList 
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
        """Push (add) a new element onto the top of the stack"""
        self.ll.insert_first(new_element)

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        return self.ll.delete_first()
