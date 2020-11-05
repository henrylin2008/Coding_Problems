# Largest Range
# Link: https://www.algoexpert.io/questions/Largest%20Range
# Difficulty: Hard

# Write a function that takes in an array of integers and returns an array of length 2 representing the largest range of
# integers contained in that array.
# The first number in the output array should be the first number in the range, while the second number should be the
# last number in the range.
# A range of numbers is defined as a set of numbers that come right after each other in the set of real integers. For
# instance, the output array [2, -6] represents the range {2,3,4,5,6}, which is a range of length 5. Note that numbers
# don't need to be sorted or adjacent in the input array in order to form a range.

# You can assume that there will only be one largest range.

# Sample Input
# array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

# Sample Output
# [0, 7]

# Time: O(n); 2 for loops, each loop is O(n) time, 2O(n) ==> O(n)
# Space: O(n); store every num in the hash table (nums)
# Solution: store all the values from the array into a hash table, and set every value as True (not visited) initially;
# Once the value has been explored, set the value to False (visited); return the first and last value in the range
def largestRange(array):
    bestRange = []  # largest range that holds first num and last num in the range
    longestLength = 0   # longest length
    nums = {}   # hash table to hold all the numbers in the array
    for num in array:
        nums[num] = True    # set every num to True
    for num in array:
        if not nums[num]:   # check if the num has been explored, if current num == False
            continue    # skip
        nums[num] = False   # set the value to False
        currentLength = 1   # current length = current num so far
        left = num - 1  # checking/exploring the num on the left
        right = num + 1  # checking the num on the right
        while left in nums:  # while left num is in the hash table (True)
            nums[left] = False  # set the left num to False
            currentLength += 1  # increase the currentLength
            left -= 1   # continue expanding to the left
        while right in nums:    # while right num is in the hash table (True)
            nums[right] = False  # set the right num to False
            currentLength += 1  # increase the currentLength
            right += 1  # continue expanding to the right
        if currentLength > longestLength:
            longestLength = currentLength   # set new longest length = current length
            bestRange = [left + 1, right - 1]   # left + 1: b/c left -= 1 in while (left in nums) loop
            # ex: [0, 7], left = 0 - 1 ==> -1 (exploring the left) ==> left += 1
    return bestRange