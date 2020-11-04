# Subarray Sort
# Difficulty: Hard
# Link: https://www.algoexpert.io/questions/Subarray%20Sort

# Write a function that takes in an array of at least two integers and that returns an array of the starting and ending
# indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire input
# array to be sorted (in ascending order).
# If the input array is already sorted, the function should return [-1, 1].

# Sample input:
# array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]

# sample output:
# [3, 9]

# Time: O(n)
# Space: O(1)
# Compare current number with adjacent numbers to determine if it's out of order (ex: 10, 7, 12)
def subarraySort(array):
    minOutOfOrder = float("inf")    # smallest num in unsorted subarray
    maxOutOfOrder = float("-inf")   # greatest num in unsorted subarray
    for i in range(len(array)):  # Go through the entire array
        num = array[i]  # num = current number
        if isOutOfOrder(i, num, array):  # helper function to check if current num is out of order,
            # previous num <= current num <= next num
            minOutOfOrder = min(minOutOfOrder, num)  # update minOutOfOrder, min(float('inf'), num) => num
            maxOutOfOrder = max(maxOutOfOrder, num)  # update maxOutOfOrder, max(float('-inf'), num) => num
    if minOutOfOrder == float("inf"):  # Edge case (already sorted) from the instruction; can use either values
        return [-1, -1]
    subarrayLeftIdx = 0
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
    return [subarrayLeftIdx, subarrayRightIdx]


def isOutOfOrder(i, num, array):  # helper function to determine out of order
    if i == 0:  # first num in the array
        return num > array[i + 1]  # num > next num ==> out of order
    if i == len(array) - 1:  # last num in the array
        return num < array[i - 1]  # num < previous num ==> out of order
    return num > array[i + 1] or num < array[i - 1]  # return True if current num > next num or current num < pre num
