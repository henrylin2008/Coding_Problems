# https://www.algoexpert.io/questions/Insertion%20Sort
# Insertion Sort:
# hint: Divide the input array into two subarrays in place. The first subarray should be sorted at all times
# and should start with a length of 1, while the second subarray should be unsorted. Iterate through the unsorted
# subarray, inserting all of its elements into the sorted subarray in the correct position by swapping them into place.
# Eventually, the entire array will be sorted.
# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Insertion Sort
# algorithm to sort the array.
# Sample input: [8, 5, 2, 9, 5, 6, 3]
# Sample output: [2, 3, 5, 5, 6, 8, 9]

# Best: O(n) time | O(1) space - where n is the length of the input array
# Average: O(n^2) time | O(1) space - where n is the length of the input array
# Worst: O(n^2) time | O(1) space - where n is the length of the input array

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]