# Difficulty: Medium
# Category: Arrays
# Link: https://www.algoexpert.io/questions/Longest%20Peak

# Longest Peak
# Write a function that takes in an array of integers and returns the lenght of the longest peak in the array
# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip (the heightest
# value in the peak), at which point they become strictly decreasing. At least three integers are required to from a peak.

# For example, the integer 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1,2,2,0.
# Similarly, the integers 1,2,3 don't form a peak because there aren't any strictly decreasing integers after the 3.

# Sample input
# array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]

# sample output
# 6 // [0, 10, 6, 5, -1, -3]

# Time: O(n)
# Space: O(1)
# logic: find the peak, then expanding to the left and expanding to the right, and calculate longest Peak length
def longestPeak(array):
    longestPeakLength = 0  # initialize the longest length
    i = 1  # initial starting point at index 1, per definition of Peak
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]  # compare current value with adjacent values
        if not isPeak:  # if it's not a peak, moving along
            i += 1
            continue

        # expanding to the left from the peak
        leftIdx = i - 2  # left starting point from the peak
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            # leftIdx is still inbound, left value < right value
            leftIdx -= 1  # continue expanding to the left
        # expanding to the right from the peak
        rightIdx = i + 2  # right starting point from the peak
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            # rightIdx still inbound, left value > right value
            rightIdx += 1  # continue expanding to the right

        currentPeakLength = rightIdx - leftIdx - 1  # current longest Peak length
        longestPeakLength = max(longestPeakLength, currentPeakLength)  # set the longest Peak length
        i = rightIdx    # new starting point (no need to explore visited values)
    return longestPeakLength
