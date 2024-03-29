# Remove Duplicates (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743424499_2Unit

# Problem Statement
#
# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element
# appears only once. The relative order of the elements should be kept the same and you should not use any extra
# space so that the solution have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after moving return the length of the subarray that
# has no duplicate in it.
#
# Example 1:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
#
# Example 2:
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].

# Solution
#
# In this problem, we need to separate the duplicates in-place such that the resultant length of the array remains
# sorted. As the input array is sorted, therefore, one way to do this is to shift the elements left whenever we
# encounter duplicates. In other words, we will keep one pointer for iterating the array and one pointer for placing
# the next non-duplicate number. So our algorithm will be to iterate the array and whenever we see a non-duplicate
# number we move it next to the last non-duplicate number we’ve seen.

def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 0
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()


# Time Complexity
# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
#
# Space Complexity
# The algorithm runs in constant space O(1).


# Similar Questions
# Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return
# the new length of the array.

def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement


def main():
    print("Array new length: " +
          str(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_element([2, 11, 2, 2, 1], 2)))


main()

# Time and Space Complexity: The time complexity of the above algorithm will be O(N), where ‘N’ is the total
# number of elements in the given array.
#
# The algorithm runs in constant space O(1).
