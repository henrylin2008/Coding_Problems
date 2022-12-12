# Find all Missing Numbers (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743711992_31Unit

# Problem Statement
# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates,
# which means some numbers will be missing. Find all those missing numbers.
#
# Example 1:
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
#
# Example 2:
# Input: [2, 4, 1, 2]
# Output: 3
#
# Example 3:
# Input: [2, 3, 2, 1]
# Output: 4

# Solution
#
# This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number with one
# difference. In this problem, there can be many duplicates whereas in ‘Find the Missing Number’ there were no
# duplicates and the range was greater than the length of the array.
#
# However, we will follow a similar approach though as discussed in Find the Missing Number to place the numbers on
# their correct indices. Once we are done with the cyclic sort we will iterate the array to find all indices that are
# missing the correct numbers.

def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    missingNumbers = []

    for i in range(len(nums)):
        if nums[i] != i + 1:
            missingNumbers.append(i + 1)

    return missingNumbers


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
