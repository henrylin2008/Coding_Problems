# average case: O(n^2)
# worst case: O(n^2)
# Best case: O(n^2)
# Space: O(1); in-place solution (swapping nodes)

# Logic: compare 2 values side by side, move the greater value to the right side, then compare the greater value to the
# next value in the array, swap their position if the new value is less than the previous greater value; repeat the
# same process until it reaches to the end of the array. This results the largest value in the list will be at the end
# of the list.
# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of
# order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles”
# up to the location where it belongs.

def bubbleSort(alist):
    for value in range(len(alist) - 1, 0, -1):
        for i in range(value):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)


# Short Bubble:
# set a flag to False, A bubble sort can be modified to stop early if it finds that the list has become sorted.
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)
