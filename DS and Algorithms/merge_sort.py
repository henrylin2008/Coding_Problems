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
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                alist[k] = leftHalf[i]
                i = i + 1
            else:
                alist[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
