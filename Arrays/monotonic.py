# link: https://www.algoexpert.io/questions/Monotonic%20Array
# Monotonic Array

# Write a function that takes in an array of integers and returns a boolean representing whether the array is monotonic.
# An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely
# non-decreasing.
# Non-increasing elements aren't necessarily exclusively decreasing; they simply don't increase. Similarly, non-decreasing
# elements aren't necessarily exclusively increasing; they simply don't decrease.

# Note that empty arrays and arrays of one elements are monotonic.

# Sample input
# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

# Sample output:
# True

# Solution #1: compare 2 consecutive values and determine if it break the direction
# Time: O(n)
# Space: O(1)
# def isMonotonic(array):
#     if len(array) <= 2: # True for length is <= 2
#         return True
#
#     direction = array[1] - array[0] # determine the direction (upward or downward)
#     for i in range(2, len(array)):
#         if direction == 0:  # if 2 consecutive numbers are the same
#             direction = array[i] - array[i-1]   # finding the "new" direction
#             continue    # keep going
#         if breaksDirection(direction, array[i - 1], array[i]): # if it breaks the direction
#             return False
#     return True
#
#
# def breaksDirection(direction, previousInt, currentInt): # check if direction is going the same way
#     difference = currentInt - previousInt
#     if direction > 0:   # if trending upward
#         return difference < 0   # break direction only if it is going downward
#     return difference > 0   # if direction is going downward, it breaks direction only if it is going upward
#


# Solution #2: 2 checks: whether the array is entirely non-decreasing (upward), or entirely non-increasing (downward)
# Time: O(n)
# Space: O(1)
def isMonotonic(array):
    isUpward = True  # trending upward
    isDownward = True  # trending downward
    for i in range(1, len(array)):
        if array[i] < array[i-1]:  # if current value < previous value: then the array is decreasing
            isUpward = False
        if array[i] > array[i-1]:  # if current value > previous value, then the array is increasing
            isDownward = False

    return isUpward or isDownward
