# Algoexpert: https://www.algoexpert.io/questions/First%20Duplicate%20Value
# First Duplicate Value
# Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that
# returns the first integer that appears more than once (when the array is ready from left to right).
# In other words, out of all the integers that might occur more than once in the input array, your function should
# return the one whose first duplicate value has the minimum index.
# If no integer appears more than once, you function should return -1
# Note that you're allowed to mutate the input array
# Sample Input #1
# array = [2, 1, 5, 2, 3, 3, 4]
# Sample Output #1: 2  // 2 is the first integer that appears more than once.
# // 3 also appears more than once, but the second 3 appears after the second 2

# Sample Input #2
# array = [2, 1, 5, 3, 3, 2, 4]
# Sample Output #2: 3   // 3 is the first integer that appears more than once.
# // 2 also appears more than once, but the second 2 appears after the second 3

# Solution #2: store seen values in a set, if a value matches any value from the seen set, return the value; if it's a
# new value, store it in the set; otherwise return -1
# Time: O(n); linear time
# Space: O(n)
def firstDuplicateValue(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


# Solution #3:
# Brute-force solution: using 2 loops, first loop sets the pointer, while second loop loops through the rest of the
# array and find any matching value
# Time: O(n^2)
# Space: O(1)
def firstDuplicateValue(array):
    minimumSecondIndex = len(array)     # set minSecIdx = length of the array
    for i in range(len(array)):   # Outer loop
        value = array[i]
        for j in range(i+1, len(array)):  # rest of array: look for second occurrence of the value
            valueToCompare = array[j]
            if value == valueToCompare:
                minimumSecondIndex = min(minimumSecondIndex, j)

    if minimumSecondIndex == len(array):
        return -1

    return array[minimumSecondIndex]

