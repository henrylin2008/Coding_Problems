# Link: https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
# Sum of Linked Lists
# Difficulty: Medium
# You're given two Linked Lists of potentially unequal length. Each Linked List represents a non-negative integer,
# where each node in the Linked List is a digit of that integer, and the first node in each Linked List always
# represents the least significant digit of the integer. Write a function that returns the head of a new Linked List
# that represents the sum of the integers represented by the two input Linked Lists.
# Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null
# if it's the tail of the list. The value of each LinkedList node is always in the range of 0-9.
# Note: your function must create and return a new Linked List, and you're not allowed to modify either of the input
# Linked Lists.

# Sample Input:
# linkedListOne = 2 -> 4 -> 7 -> 1
# linkedListTwo = 9 -> 4 -> 5

# Sample Output:
# 1 -> 9 -> 2 -> 2
# // linkedListOne represents 1742
# // linkedListTwo represents  549
# // 1754 + 549 = 2291


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(max(n, m)); n, m: length of 2 nodes; max(n, m): longest length between 2 nodes
# Space: O(max(n, m))
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHead = LinkedList(0)   # new linked list head pointer
    currentNode = newLinkedListHead     # current node
    carry = 0       # carry over value

    nodeOne = linkedListOne  # pointer 1, loop through Linked list one, keep track of node that's currently on
    nodeTwo = linkedListTwo  # pointer 2, loop through linked list Two, keep track of node that's currently on
    # keep looping if we have a nodeOne, or a nodeTwo, or some carry is not equal 0
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0  # get nodeOne value, return 0 if it's a None node
        valueTwo = nodeTwo.value if nodeTwo is not None else 0  # get nodeTwo value, return 0 if it's a None node
        sumOfValues = valueOne + valueTwo + carry   # sum of nodes at same positions

        newValue = sumOfValues % 10  # reminder, get the value on one's position
        newNode = LinkedList(newValue)  # create new linked list node
        currentNode.next = newNode  # set pointer of currentNode to the new node
        currentNode = newNode   # set current node to new node

        carry = sumOfValues // 10   # carry over value;  if sum of 2 nodes > 10
        nodeOne = nodeOne.next if nodeOne is not None else None  # next linked list node
        nodeTwo = nodeTwo.next if nodeTwo is not None else None  # next linked list node

    return newLinkedListHead.next   # return next node after new linked list
