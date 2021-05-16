# Selection Sort
# a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the
# proper location.

# Worst-case: O(n^2)
# Best-case: O(n^2)
# Space: O(1)
# Logic: find the largest value each loop, then swap current largest value to the end of the list and current position;
# Repeat the process until entire list is sorted
def selectionSort(alist):
    for fillSlot in range(len(alist) - 1, 0, -1):   # find fill slot from right to the left
        positionOfMax = 0
        for location in range(1, fillSlot + 1):  # loop through the list
            if alist[location] > alist[positionOfMax]:  # if given index has a greater value,
                positionOfMax = location        # set new position of the max value

        # swap out the positions: current fill slot and position of max value
        temp = alist[fillSlot]
        alist[fillSlot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
