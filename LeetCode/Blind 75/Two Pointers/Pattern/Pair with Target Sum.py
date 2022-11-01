# Pair with Target Sum (easy)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743417172_1Unit

# Problem Statement
#
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
#
# Example 1:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
#
# Example 2:
# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

# Solution
#
# Since the given array is sorted, a brute-force solution could be to iterate through the array, taking one number at
# a time and searching for the second number through Binary Search. The time complexity of this algorithm will be O(
# N*logN)O(N∗logN). Can we do better than this?
#
# We can follow the Two Pointers approach. We will start with one pointer pointing to the beginning of the array and
# another pointing at the end. At every step, we will see if the numbers pointed by the two pointers add up to the
# target sum. If they do, we have found our pair; otherwise, we will do one of two things:

#   1. If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we
#      need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.
#   2. If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need
#      a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.


def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]

        if target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()


# Time Complexity
# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
#
# Space Complexity
# The algorithm runs in constant space O(1).

# An Alternate approach
#
# Instead of using a two-pointer or a binary search approach, we can utilize a HashTable to search for the required
# pair. We can iterate through the array one number at a time. Let’s say during our iteration we are at number ‘X’,
# so we need to find ‘Y’ such that “X + Y == TargetX+Y==Target”. We will do two things here:
#   1. Search for ‘Y’ (which is equivalent to “Target−X”) in the HashTable. If it is there, we have found the required
#      pair.
#   2. Otherwise, insert “X” in the HashTable, so that we can search it for the later numbers.

def pair_with_targetsum(arr, target_sum):
    nums = {}  # to store numbers and their indices
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

# Time Complexity
# The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
#
# Space Complexity
# The space complexity will also be O(N), as, in the worst case, we will be pushing ‘N’ numbers in the HashTable.
