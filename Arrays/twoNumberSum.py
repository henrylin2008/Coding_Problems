# link: https://www.algoexpert.io/questions/Two%20Number%20Sum
#
# ​>Two Number Sum
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
# Traverse all numbers twice, if sum of first Num and second num equal to targetSum, then return first num, sec num
def twoNumberSum(array, targetSum):
    for i in range(len(array)-1): # go all the way before the last value
        firstNum = array[i]
        # print("first num:", firstNum)
        for j in range(i+1, len(array)): # j goes all the way to the last value
            secondNum = array[j]
            # print("second num: ", secondNum)
            if firstNum + secondNum == targetSum:
                # print("firstNum + secondNum == targetSum:", firstNum, ",", secondNum)
                return[firstNum, secondNum]
    return[]


# Method 2:
# Time: O(n)
# Space: O(n)
# Ex: [3,5,-4,8,11,1,-1,6], 10
# use hash table to store seem values; traverse each value in the array, and store the value into the hash table(Key:
# value); when match is found, print matched value and the value of the current index; else just set the value of current
# index to True
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
# sort the array then set a left pointer and a right pointer; create a currentSum by adding values at left and right pointer
# compare currentSum to targetSum, if currentSum is equal to targetSum, return the value at left and right pointer;
# elif currentSum < targetSum, move left pointer to a position to the right; b/c moving left pointer is going to get a
# bigger value than currentSum; elif currentSum > targetSum, move the right pointer to a position to the left
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

# twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
