# link: https://www.algoexpert.io/questions/Bubble%20Sort
# Bubble Sort: start from first num and compare it to the next num, if current num is greater than next num, swap 2 nums,
# and do the same thing for the rest of the array; and repeat the process until the entire array is sorted
# Write a function that takes in an array of integers and returns a sorted version of that array. Use the Bubble Sort
# algorithm to sort the array.
# If you're unfamiliar with Bubble Sort, we recommend watching the Conceptual Overview section of this question's video
# explanation before starting to code.
# Sample input: [8, 5, 2, 9, 5, 6, 3]
# Sample output: [2, 3, 5, 5, 6, 8, 9]

# Time: O(n^2), average/worst case
# Space: O(1)
def bubbleSort(array):
    isSorted = False   # assuming array is not sorted
    counter = 0  # use it to skip last num in each loop, since we know last num is always sorted
    while not isSorted:  # while array is not sorted
        isSorted = True  # assuming array is sorted
        for i in range(len(array) -1-counter): # len(array)-1: b/c it'd be comparing i and i+1; -counter: - last num
            if array[i] > array[i+1]: # if current num > next num
                swap(i, i+1, array)   # helper function to swap i and i+1
                isSorted = False    # array is not sorted if running in this loop
        counter += 1
    # print(array)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# bubbleSort([8, 5, 2, 9, 5, 6, 3])