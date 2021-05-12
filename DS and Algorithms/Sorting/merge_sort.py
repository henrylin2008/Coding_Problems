# Time: O(nlog(n))
# Space: O(n); linear, bc it copies values into new arrays

# Logic:
# If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item,
# we split the list and recursively invoke a merge sort on both halves.
# First divide the list into the smallest unit (1 element), then compare each element with the adjacent list to sort
# and merge the two adjacent lists. Finally all the elements are sorted and merged.
def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i = 0
        j = 0
        k = 0
        # merging sorted list
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:  # first item on leftHalf <= first item on rightHalf
                alist[k] = leftHalf[i]  # store smaller value (leftHalf) on the alist
                i = i + 1   # move to next index
            else:
                alist[k] = rightHalf[j]  # store smaller value (rightHalf) on the alist
                j = j + 1
            k = k + 1   # move alist to next index

        while i < len(leftHalf):  # if only leftHalf left (no rightHalf)
            alist[k] = leftHalf[i]  # store next value in leftHalf in the alist
            i = i + 1   # move to next value in leftHalf list
            k = k + 1   # move to next index of alist

        while j < len(rightHalf):   # if only rightHalf left (no leftHalf)
            alist[k] = rightHalf[j]  # store next value in rightHalf in the alist
            j = j + 1   # move to next value in rightHalf list
            k = k + 1   # move to next index of alist
    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
