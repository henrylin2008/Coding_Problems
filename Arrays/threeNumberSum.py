# https://www.algoexpert.io/questions/Three%20Number%20Sum
# Three Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The
# function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all
# these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be
# ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the
# function should return an empty array.
# Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
# Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

# Time: O(n^2); one n is the for loop; 2 pointers (left & right) go through the array another loop
# space: O(n); n: worse case is to pair all number in the array
def threeNumberSum(array, targetSum):
    array.sort()  # sort the array
    triplets = []  # set an empty array
    for i in range(len(array) - 2): # range(len(array)-2): b/c look for 3 numbers, 2 pointers at the last number indexes
        left = i + 1 # next value next to i
        right = len(array) - 1
        while left < right: # before left and right pointers meet
            currentSum = array[i] + array[left] + array[right] # sum = current index value + left pointer + right pointer
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]]) # store 3 values to triplets array
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1 # incrase left pointer would give a greater currentSum
            elif currentSum > targetSum:
                right -= 1 # decrease right pointer would give a smaller currentSum
    # print(triplets)
    return triplets

# threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)
