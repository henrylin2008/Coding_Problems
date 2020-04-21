# Kadane's Algorithm
# https://www.algoexpert.io/questions/Kadane's%20Algorithm
# Difficulty: Medium
#
# Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained by summing
# up all the integers in a non-empty subarray of the input array. A subarray must only contain adjacent numbers
#
# Sample Input:
# array = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]

# Sample Output
# 19

# Kadane's Algorithm
# maxEndingHere = max(maxEndingHere + num, num)
# maxSoFar = max(maxSoFar, maxEndingHere)

# Sample input:  [3,5,-9,|1,3,-2,3,4,7,2,-9,6,3,1,|    -5,4]
# maxEndingHere: [3,8,-1,|1,4,2,5,9,16,18,9,15,18,19,| 14,18]
# maxSoFar:      [3,8, 8, 8,8,8,8,9,16,18,18,18,18,19, 19,19]

# Time: O(N); N = length of array
# Space: O(1); only stores maxEndingHere and maxSoFar values
def maxSubarraySum(array):
    maxEndingHere = array[0] # first item in array as maxEndingHere
    maxSoFar = array[0] # first item in array as maxSoFar
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num) # max of current num and sum of current num and last maxEndingHere value
        maxSoFar = max(maxSoFar, maxEndingHere)
    # print(maxSoFar)
    return maxSoFar

# maxSubarraySum([2,3,5,-15,3,2,3,4,-7])
