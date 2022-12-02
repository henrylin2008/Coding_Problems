# Problem Challenge 1: Search Bitonic Array (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628744190772_84Unit

# Problem Statement
#
# Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is
# monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for
# any index i in the array arr[i] != arr[i+1].
#
# Write a function to return the index of the ‘key’. If the 'key' appears more than once, return the smaller index.
# If the ‘key’ is not present, return -1.
#
# Example 1:
# Input: [1, 3, 8, 4, 3], key=4
# Output: 3
#
# Example 2:
# Input: [3, 8, 3, 1], key=8
# Output: 1
#
# Example 3:
# Input: [1, 3, 8, 12], key=12
# Output: 3
#
# Example 4:
# Input: [10, 9, 8], key=10
# Output: 0

# Solution
#
# The problem follows the Binary Search pattern. Since Binary Search helps us efficiently find a number in a sorted
# array we can use a modified version of the Binary Search to find the ‘key’ in the bitonic array.
#
# Here is how we can search in a bitonic array:
#   1. First, we can find the index of the maximum value of the bitonic array, similar to Bitonic Array Maximum. Let’s
#      call the index of the maximum number maxIndex.
#   2. Now, we can break the array into two sub-arrays:
#       - Array from index ‘0’ to maxIndex, sorted in ascending order.
#       - Array from index maxIndex+1 to array_length-1, sorted in descending order.
#   3. We can then call Binary Search separately in these two arrays to search the ‘key’. We can use the same
#      Order-agnostic Binary Search for searching.
#

def search_bitonic_array(arr, key):
    maxIndex = find_max(arr)
    keyIndex = binary_search(arr, key, 0, maxIndex)
    if keyIndex != -1:
        return keyIndex
    return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # at the end of the while loop, 'start == end'
    return start


# order-agnostic binary search
def binary_search(arr, key, start, end):
    while start <= end:
        mid = int(start + (end - start) / 2)

        if key == arr[mid]:
            return mid

        if arr[start] < arr[end]:  # ascending order
            if key < arr[mid]:
                end = mid - 1
            else:  # key > arr[mid]
                start = mid + 1
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1
            else:  # key < arr[mid]
                start = mid + 1

    return -1  # element is not found


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
