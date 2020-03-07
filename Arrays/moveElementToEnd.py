# https://www.algoexpert.io/questions/Move%20Element%20To%20End
# Move Element To End
# You are given an array of integers and an integer. Write a function that moves all instances of that integer in the
# array to the end of the array. The function should perform this in place and does not need to maintain the order of the
# other integers.
#
# Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
# Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be ordered differently)

# Time: O(n); n = length of the array
# Space O(1); constant time, b/c all the operations happening at the same array
#
def moveElementToEnd(array, toMove):
    i = 0 # left pointer
    j = len(array) - 1 # right pointer
    while i < j:
        while i < j and array[j] == toMove: # when i < j and value at j == toMove
            j -= 1  # move right pointer to a position to the left
        if array[i] == toMove: # when value at i == toMove:
            array[i], array[j] = array[j], array[i] # swap value in i and j
        i += 1  # move left pointer to a position to the right
    # print(array)
    return array

# moveElementToEnd([2, 1, 2, 2, 2, 3, 4, 2], 1)