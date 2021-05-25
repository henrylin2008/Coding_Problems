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
    # In a heap, for every node x with parent p, the key in p is smaller than or equal to the key in x. (or for every
    # parent there are no children that are smaller than them

    # Insert
    # i's left child: 2 * i
    # i's right child: 2 * i + 1
    # i's parent: i // 2
    # Percolates a new item as far up in the tree as it needs to go to maintain the heap property
    def percUp(self, i):
        while i // 2 > 0:  # while has a parent
            if self.heapList[i] < self.heapList[i // 2]:  # if out of order
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2  # lop with new position

    def insert(self, k):
        self.heapList.append(k)  # insert at end of the list
        self.currentSize = self.currentSize + 1  # update size
        self.percUp(self.currentSize)  # adjust to be in heap order

    # Delete smallest item (root)
    # First, we will restore the root item by taking the last item in the list and moving it to the root position.
    # Moving the last item maintains our heap structure property. However, we have probably destroyed the heap order
    # property of our binary heap. Second, we will restore the heap order property by pushing the new root node down the
    # tree to its proper position, swap the root with its smallest child less than the root.
    # Percolating down: swap the root with its smallest child less than the root, until it is on the proper position
    def percDown(self, i):
        while (i * 2) <= self.currentSize:  # while it has child
            mc = self.minChild(i)  # get minChild value
            if self.heapList[i] > self.heapList[mc]:  # if needs to go down further (current value > child node value)
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc  # swap i and min child

    def minChild(self, i):
        """Look at the two children, and return index of which children node has the smaller value"""
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]  # top of the list
        self.heapList[1] = self.heapList[self.currentSize]  # swap first (currently emtpy) and last item
        self.currentSize = self.currentSize - 1  # reduce the size
        self.heapList.pop()  # pop end of the list
        self.percDown(1)
        return retval

    # Trick to build a min heap from a list in O(n) time
    # -You can just use the original list and reorder it to make a heap in O(n) time
    # Although we start out in the middle of the tree and work our way back toward the root, the percDown method ensures
    # that the largest child is always moved down the tree.
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

    # i = 2  [0, 9, 5, 6, 2, 3]
    # i = 1  [0, 9, 2, 6, 5, 3]
    # i = 0  [0, 2, 3, 6, 5, 9]


bh = BinHeap()
bh.buildHeap([9, 5, 6, 2, 3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
