# Shell sort
# The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking the
# original list into a number of smaller sublists, each of which is sorted using an insertion sort. The unique way that
# these sublists are chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous
# items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that
# are i items apart.

# Logic: divide the original list into a number of smaller sublists, then compare the values at the same index on
#        sublists, and sort sublists; lastly, run a standard insertion sort.
# Worst  time:  O(n^2)
# Average time: O(nLog(n))
# Space: O(1)
def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:

        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)

        print("After increments of size", sublistCount,
              "The list is", alist)

        sublistCount = sublistCount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
