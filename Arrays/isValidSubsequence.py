# Validate Subsequence
# Difficulty: Easy
# link: https://www.algoexpert.io/questions/Validate%20Subsequence

# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence
# of the first one.
# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that they are in the
# same order as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1,2,3,4],
# and so do the numbers [2, 44]. Note that a single number in an array and the array itself are both valid subsequences
# of the array.

# Sample input:
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]

# Sample output
# true

# Time: O(N), iterate through the main array
# Space: O(1), not storing anything but the 2 pointers
# Solution: set 2 pointers, one on the main array and one on the sequence, starting from the beginning, then iterate
# through the array and the sequence to find matched and ordered items from the sequence

# Solution 1
def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence) - 1


