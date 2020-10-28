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
    while arrIdx < len(array) and seqIdx < len(sequence):  # while both pointers are still within the length
        if array[arrIdx] == sequence[seqIdx]:  # when 2 pointers are matched
            seqIdx += 1  # move the seqIdx pointer to the next
        arrIdx += 1  # move the arrIdx pointer to the next
    return seqIdx == len(sequence)  # return True if it reaches to the end of the sequence


# Solution 2
def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:  # for every value in the (main) array
        if seqIdx == len(sequence):  # break if it reaches to the end of the sequence
            break
        if sequence[seqIdx] == value:  # if value in array matches the value in seqIdx
            seqIdx += 1  # move seqIdx to the right
    return seqIdx == len(sequence)  # return true if it reaches to the end of the sequence
