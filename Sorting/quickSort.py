# Quick Sort:
#
# Recursive
# QuickSort(Data(), left, righ):
#     if Left < Right Then
#         PivotPoistion = Partition(Data, Left, Right)
#         QuickSort(Data, LEft, PivotPoistion -1)
#         QuickSort(Data, PivotPostion + 1, Right)
#     End if
#
#==============================================================
# Alternative:
# WHILE LeftPointer <> RightPointer:
#     While (Data(LeftPointer) < Data(RigthPointer)) AND (LeftPointer <> RightPointer)
#         LeftPointer = LeftPointer + 1
#     End While
#     Temp = Data(LeftPointer)
#     Data(LeftPointer) = Data(RightPointer)
#     Data(RightPointer) = Temp
#     WHILE (Data(LeftPointer) < Data(RightPointer)) And (LeftPointer <> RightPointer)
#         RightPointer = RightPointer - 1
#     End While
#     Emp = Data(LeftPointer)
#     Data(LeftPointer) = Data(RightPointer)
#     Data(RightPointer) = Temp
# End WHILE
#==============================================================
#
# Pivot = Data(LeftPointer)
# While LeftPointer <> RightPointer:
#     If CurrentPointer = "right" Then
#         If Data(RightPointer) < Pivot Then
#             Data(LeftPointer) = Data(RightPointer)
#             LeftPointer = LeftPointer + 1
#             CurrentPointer = "Left"
#         Else:
#             RightPointer = RightPointer - 1
#         End If
#     Elif CurrentPointer = "Left" Then
#         If Data(LeftPointer) > Pivot Then
#             Data(RightPointer) = Data(LeftPointer)
#             RightPointer = RightPointer - 1
#             CurrentPointer = "right"
#         Else
#             LeftPointer = LeftPointer + 1
#         endif
#     Endif
# End While
# Data(LeftPointer) = Pivot

# QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the
# picked pivot. There are many different versions of quickSort that pick pivot in different ways.
#
# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.
# The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as
# pivot, put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put
# all greater elements (greater than x) after x. All this should be done in linear time.

def quickSort(arr):
    quickSort_Help(arr, 0, len(arr) -1)

def quickSort_Help(arr,first,last): # recursive call on the splitted list/s
    if first < last:
        splitPoint = partition(arr, first, last)
        quickSort_Help(arr, first, splitPoint-1) # first half before split point
        quickSort_Help(arr, splitPoint+1, last) # second half after split point

def partition(arr,first,last): # find the split point, and move items in apprioriate side of the list
    pivotValue = arr[first] # set first value as the pivot value
    leftMark = first+1 # left pointer is second item in the array
    rightMark = last # right pointer is last item in the array

    done = False
    while not done:
        while leftMark <= rightMark and arr[leftMark] <= pivotValue: # while left pointer <= right pointer and value is <= pivotValue value
            leftMark += 1  # move left pointer a position to the right
        while arr[rightMark] >= pivotValue and rightMark >= leftMark: #while value at right pointer >= pivot value and right pointer >= left pointer
            rightMark -= 1 # move right pointer to the left
        if rightMark < leftMark: # done/stop when right pointer is < left pointer
            done = True
        else:
            temp = arr[leftMark]  # swapping values in left pointer and right pointer (with following 2 lines)
            arr[leftMark] = arr[rightMark]
            arr[rightMark] = temp

    temp = arr[first] # swap first item with value at right pointer (with following 2 lines)
    arr[first] = arr[rightMark]
    arr[rightMark] = temp

    return rightMark # return split point

arr = [2,5,3,1,6,9,10,8,4,5,7]
quickSort(arr)
print(arr)