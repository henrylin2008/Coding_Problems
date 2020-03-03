# link: https://www.algoexpert.io/questions/Selection%20Sort
# Selection Sort:
# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection
# Sort algorithm to sort the array.
# hint: Divide the input array into two subarrays in place. The first subarray should be sorted at all times and should
# start with a length of 0, while the second subarray should be unsorted. Find the smallest (or largest) element in the
# unsorted subarray and insert it into the sorted subarray with a swap. Repeat this process of finding the smallest (or
# largest) element in the unsorted subarray and inserting it in its correct position in the sorted subarray with a swap
# until the entire array is sorted
# Sample input: [8, 5, 2, 9, 5, 6, 3]
# Sample output: [2, 3, 5, 5, 6, 8, 9]
# time: O(N^2); N = length of the array; iterate through the array, every loop -1 value from the array
# Space: O(1); swap numbers in the array
def selectionSort(array):
    currentIndx = 0  # index of first num in unsorted list
    while currentIndx < len(array) - 1: #last index is at final position after loops, and last item is in sorted array
        smallestIndx = currentIndx  # initialize smallestIndex = currentIndex, first index on unsorted list
        # For loop: find the smallest number
        for i in range(currentIndx+1, len(array)): # iterating through unsorted list from second index to last index
            if array[smallestIndx] > array[i]:  # if num at array[smallestIndx] > num at array[i] - current index
                smallestIndx = i # update smallestIndx = current index (i)
        array[smallestIndx], array[currentIndx] = array[currentIndx], array[smallestIndx]
        # swap values at smallestIndx and currentIndx, append smallestindx value from unsorted list to sorted list
        currentIndx += 1 # move to next index in unsorted list
    return array

selectionSort([8,2,5,3,9,7,4])