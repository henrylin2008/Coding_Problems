# Priority Queue
# -The front of the queue has the highest priority
# -The back of the queue has the lowest priority
# -The queue items are arranged so that for any item, all the items in front of that item are equal or higher in
#  priority and all items in the back of that item are lower or equal priority.
# -Any new item wil be inserted into a position that maintains the order of the queue

# Use Binary Heap to implement a priority queue
# A Binary Heap will allow us to enqueue and dequeue items both with O(log n) performance which is very fast.
# -Max Heap: priority is given to the biggest value
# -Min Heap: priority is given to the smallest value

# Binary Heap Operations:
# -BinaryHeap() creates a new, empty, binary heap.
# -insert(item) adds a new item to the heap. O(log n)
# -findMin() returns the item with the minimum key value, leaving item in the heap.
# -delMin() returns the item with the minimum key value, removing the item from the heap. O(log n)
# -isEmpty() returns true if the heap is empty, false otherwise.
# -size() returns the number of items in the heap.
# -buildHeap(list) builds a new heap from a list of keys.
from pythonds.trees import BinHeap

bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)

print(bh.delMin())  # 3

print(bh.delMin())  # 5

print(bh.delMin())  # 7

print(bh.delMin())  # 11


# A complete binary tree is a tree in which each level has all of its nodes. The exception to this is the bottom level
# of the tree, which we fill in from left to right.
# -Left child of node p is 2p
# -right child of node p is 2p+1
# -The parent of child node c is c/2
# index: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
# value: 0 | 5 | 9 | 11| 14| 18| 19| 21| 33| 17| 27 |
#                  (1)5
#               /         \
#            (2)9          (3)11
#          /     \         /    \
#      (4)14    (5)18    (6)19 (7)21
#      /  \      /
#   (8)33 (9)17 (10)27

class BinHeap:
    def __init__(self):
        self.heapList = [0]  # first index set to 0
        self.currentSize = 0


# Heap Order Property
# In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x. (or for every parent
# there are no children that are smaller than them


# Insert
# i's left child: 2 * i
# i's right child: 2 * i + 1
# i's parent: i // 2
def percUp(self, i):
    while i // 2 > 0:   # while has a parent
        if self.heapList[i] < self.heapList[i // 2]:  # if out of order
            tmp = self.heapList[i // 2]
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2  # lop with new position


def insert(self, k):
    self.heapList.append(k)  # insert at end of the list
    self.currentSize = self.currentSize + 1  # update size
    self.percUp(self.currentSize)  # adjust to be in heap order
