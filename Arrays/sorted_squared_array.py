# https://www.algoexpert.io/questions/Sorted%20Squared%20Array
# Sorted Squared Array
# Difficulty: Easy
# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new
# array of the same length with the squares of the original integers also sorted in ascending order.
#
# Sample Input:
array1 = [1, 2, 3, 4, 5, 6, 8, 9]
# array2 = [-4, -2, 0, 1, 3]

# Sample Output:
# array1: [1, 4, 9, 25, 36, 64, 81]
# array2: [0, 1, 4, 9, 16]


# Solution #2: Brute-force solution
# Time: O(nlog(n)): n is the length of the input array
# Space: O(n)
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]  # set all values to 0 in the array

    for idx in range(len(array)):   # loop through the array and squared each item
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    # print(sortedSquares)
    return sortedSquares


sortedSquaredArray(array1)
