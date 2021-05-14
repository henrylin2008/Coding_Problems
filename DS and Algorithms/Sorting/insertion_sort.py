# Insertion Sort
# link: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheInsertionSort.html#lst-insertion
# We begin by assuming that a list with one item (position 0) is already sorted. On each pass, one for each item 1
# through 𝑛−1, the current item is checked against those in the already sorted sublist. As we look back into the already
# sorted sublist, we shift those items that are greater to the right. When we reach a smaller item or the end of the
# sublist, the current item can be inserted.

# Worst complexity: O(n^2)
# Average complexity: O(n^2)
# Best complexity: O(n)
# Space complexity: O(1)
def insertionSort(alist):
    for index in range(1, len(alist)):

        currentValue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentValue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)
