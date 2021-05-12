# https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html
# A quick sort first selects a value, which is called the pivot value. Although there are many different ways to choose
# the pivot value, we will simply use the first item in the list. The role of the pivot value is to assist with
# splitting the list. The actual position where the pivot value belongs in the final sorted list, commonly called the
# split point, will be used to divide the list for subsequent calls to the quick sort.

# The algorithm can be broken down into three parts:
# 1. Partitioning the array about the pivot.
# 2. Passing the smaller arrays to the recursive calls.
# 3. Joining the sorted arrays that are returned from the recursive call and the pivot.
def QuickSort(arr):
    elements = len(arr)

    # Base case
    if elements < 2:
        return arr

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if arr[i] <= arr[0]:
            current_position += 1
            temp = arr[i]
            arr[i] = arr[current_position]
            arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position]
    arr[current_position] = temp  # Brings pivot to it's appropriate position

    left = QuickSort(arr[0:current_position])  # Sorts the elements to the left of pivot
    right = QuickSort(arr[current_position + 1:elements])  # sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right  # Merging everything together

    return arr


array_to_be_sorted = [4, 2, 7, 3, 1, 6]
print("Original Array: ", array_to_be_sorted)
print("Sorted Array: ", QuickSort(array_to_be_sorted))