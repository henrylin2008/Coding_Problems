# https://www.algoexpert.io/questions/Smallest%20Difference
# Smallest Difference
# Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from
# the first array, one from the second array) whose absolute difference is closest to zero. The function should return an
# array containing these two numbers, with the number from the first array in the first position. Assume that there will
# only be one pair of numbers with the smallest difference.
#
# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
# Sample Output: [28, 26]

# Time:
# Space:

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    ptr1 = 0  # pointer 1, set at arrayOne[0]
    ptr2 = 0   # pointer 2, set at arrayTwo[0]
    smallestDiff = float('inf')  # smallest difference every time
    currentDiff = float('inf') # current difference
    smallestPair = []
    while ptr1 < len(arrayOne) and ptr2 < len(arrayTwo): # while both pointers are valid (within the length)
        numOne = arrayOne[ptr1]  # first index of ArrayOne
        numTwo = arrayTwo[ptr2]  # first index of ArrayTwo
        if numOne > numTwo:
            currentDiff = numOne - numTwo  # current difference between values at 2 arrays
            ptr2 += 1 # move pointer2 to next position to find a closer number to numOne
        elif numOne < numTwo:
            currentDiff = numTwo - numOne
            ptr1 += 1
        else:
            return [numOne, numTwo] # return 
        if smallestDiff > currentDiff:
            smallestDiff = currentDiff
            smallestPair = [numOne, numTwo]
    print(smallestPair)
    return smallestPair

smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])