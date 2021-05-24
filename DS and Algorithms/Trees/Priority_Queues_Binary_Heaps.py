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
