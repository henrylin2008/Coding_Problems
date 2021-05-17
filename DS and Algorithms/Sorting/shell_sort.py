# Shell sort
# The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking the
# original list into a number of smaller sublists, each of which is sorted using an insertion sort. The unique way that
# these sublists are chosen is the key to the shell sort. Instead of breaking the list into sublists of contiguous
# items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that
# are i items apart.

# Logic: divide the original list into a number of smaller sublists (half each time until it reaches to 1), then compare
#        the values at the same index of sublists and sort the values sublists; lastly, run a standard insertion sort.
# Worst  time:  O(n^2)
# Average time: O(nLog(n))
# Space: O(1)
def shellSort(alist):
    sublistCount = len(alist) // 2  # sublist in half
    while sublistCount > 0:

        for startPosition in range(sublistCount):   # for each sublist
            gapInsertionSort(alist, startPosition, sublistCount)    # helper method to sort values
            # positions to compare in 4: 0, 4, 8; 1, 5; 2, 6; 3, 7
            # positions to compare in 2: 0, 2, 4, 6, 8; 1, 3, 5, 7
            # positions to compare in 1: 0, 1, 2, 3, 4, 5, 6, 7, 8
        print("After increments of size", sublistCount,
              "The list is", alist)
        # After increments of size 4 The list is [20, 26, 44, 17, 54, 31, 93, 55, 77]
        # After increments of size 2 The list is [20, 17, 44, 26, 54, 31, 77, 55, 93]
        # After increments of size 1 The list is [17, 20, 26, 31, 44, 54, 55, 77, 93]

        sublistCount = sublistCount // 2


def gapInsertionSort(alist, start, gap):
    """implement insertion sort for gap values"""
    for i in range(start + gap, len(alist), gap):

        currentValue = alist[i]     # value at current index
        position = i    # current index

        # while position >= gap and value at last position (previous gap) > currentValue
        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]     # swap current value and last value (at last position)
            position = position - gap   # update the position to the last position

        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)    # [17, 20, 26, 31, 44, 54, 55, 77, 93]
