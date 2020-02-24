# link: https://www.algoexpert.io/questions/Two%20Number%20Sum
#
# ​Two Number Sum
#
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array.
# If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at
# most one pair of numbers summing up to the target sum.
#
# Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
# Sample output: [-1, 11]

# Method 1:
# Time: O(n^2)
# Space: O(1)
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return[firstNum, secondNum]
    return[]


# Method 2:
# Time: O(n)
# Space: O(n)
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


# Method 3:
# Time: O(nlog(n))
# Space: O(1)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -=1
    return []

