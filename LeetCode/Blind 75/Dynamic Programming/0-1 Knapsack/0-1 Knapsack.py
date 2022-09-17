# 0-1 Knapsack
# https://algo.monster/problems/knapsack_intro

# We want to discuss a classic dynamic programming problem, which is 0-1 knapsack. Given a series of objects with a
# weight and a value and a knapsack that can carry a set amount of weight, what is the maximum object value we can
# put in our knapsack without exceeding the weight constraint?
#
# Input
#   weights: an array of integers that denote the weights of objects
#   values: an array of integers that denote the values of objects
#   max_weight: the maximum weight capacity of the knapsack
# Output
# the maximum value in the knapsack
#
# Examples
# Example 1:
# Input:
#   1. weights = [3, 4, 7]
#   2. values = [4, 5, 8]
#   3. max_weight = 7
# Output: 9
#
# Explanation:
# We have a knapsack of max limit 7 with 3 objects of weight-value pairs of [3,4], [4,5], [7,8], then the maximal
# value we can achieve is using the first 2 objects to obtain value 4 + 5 = 9.
#
# The other possibilities would all be only 1 object in our knapsack, which would only yield values 4, 5, and 9.

# Solution
# Brute Force | DFS | Combinatorial Search
# A brute force method would enumerate all the possibilities such that for every object we try including it into our
# knapsack which would result in time complexity O(2^n) where n is the total number of objects. This can be done with
# a recursive combinatorial search where, for every item, we either choose to include it or not, then checking which
# possibility results in the greatest value while not exceeding the maximum weight.

# Note that the largest value while not exceeding the maximum weight is 9.
# helper function that returns the maximum value when considering
# the first n items and remaining available weight remaining_weight
def knapsack_helper(weights: List[int], values: List[int], remaining_weight: int, n: int) -> int:
    # base case: if there are no items or no available weight in the knapsack to use, the maximum value is 0
    if n == 0 or remaining_weight == 0:
        return 0
    # if the weight of the current item exceeds the available weight,
    # skip the current item and process the next one
    if weights[n - 1] > remaining_weight:
        return knapsack_helper(weights, values, remaining_weight, n - 1)
    # recurrence relation: choose the maximum of two possibilities:
    #   (1) pick up the current item: current value + maximum value with the rest of the items
    #   (2) give up the current item: maximum value with the rest of the items
    return max(values[n - 1] + knapsack_helper(weights, values, remaining_weight - weights[n - 1], n - 1),
               knapsack_helper(weights, values, remaining_weight, n - 1))


def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    n = len(weights)
    return knapsack_helper(weights, values, max_weight, n)


# DFS + Memoization
# We can optimize the brute force solution by storing answers that have already been computed in a 2D array called
# dp. In this case dp[n][remaining_weight] stores the maximum value when considering the first n items with a maximum
# available weight of remaining_weight. If the answer already exists for dp[n][remaining_weight], then we immediately
# use that result. Otherwise, we recurse and store the result of the recurrence.
def knapsack_helper(weights: List[int], values: List[int], memo: List[List[int]], remaining_weight: int, n: int) -> int:
    if n == 0 or remaining_weight == 0:
        return 0
    if memo[n][remaining_weight] != -1:
        return memo[n][remaining_weight]
    res = 0
    if weights[n - 1] > remaining_weight:
        res = knapsack_helper(weights, values, remaining_weight, n - 1)
    else:
        res = max(values[n - 1] + knapsack_helper(weights, values, remaining_weight - weights[n - 1], n - 1),
                  knapsack_helper(weights, values, remaining_weight, n - 1))
    memo[n][remaining_weight] = res
    return res


def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    n = len(weights)
    memo = [[-1 for i in range(max_weight + 1)] for j in range(n + 1)]
    return knapsack_helper(weights, values, memo, max_weight, n)


# The time and space complexity will be O(n * w) where n is the number of items and w is the max weight because we
# have O(n * w) states and the time complexity of computing each state is O(1). Similarly, the only additional memory
# we use is an n * w array, so the space complexity is O(n * w).

def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    n = len(weights)
    # 2D dp array, where maxValue[i][j] is the maximum knapsack value when
    # considering the first i items with a max weight capacity of j
    max_value = [[0 for i in range(max_weight + 1)] for j in range(n + 1)]
    # iterate through all items
    for i in range(n + 1):
        # and all possible available weights
        for w in range(max_weight + 1):
            # if we consider no items or no weight, the max value is 0
            if i == 0 or w == 0:
                max_value[i][w] = 0
            # if the weight of the current item exceeds the max available weight,
            # then the answer is the max value when considering the first i - 1 items
            elif w < weights[i - 1]:
                max_value[i][w] = max_value[i - 1][w]
            # otherwise, we choose the best option between either:
            # picking up: item's value + max value when considering the rest of the items and a new weight
            # giving up: similar to the condition above
            else:
                max_value[i][w] = max(values[i - 1] + max_value[i - 1][w - weights[i - 1]],
                                      max_value[i - 1][w])
    # the answer is the max value when considering all n items and available weight of max_weight
    return max_value[n][max_weight]


# For an intuitive explanation, consider the recursive version again. If we were to translate it to an iterative
# version while maintaining the same recurrence, we need to build our solution from the bottom-up since maxValue[i][
# w] depends on the values in the previous row maxValue[i - 1]. Also, since the weights for the items are arbitrary,
# we will need to calculate the maximum value for all weights from 0 to max_weight to ensure we have the answer for
# the recurrence, since maxValue[i][w] depends on maxValue[i - 1][w - weights[i - 1]] where 0 <= weights[i - 1] <= w .

# 2D to 1D Optimization
# We have discussed how to do knapsack using 2-D DP but now we discuss how we can optimize this into 1-D DP. We
# realize that for the first dimension keeping track of the objects that we only ever use the previous row so
# therefor, we can simply remove that dimension from out DP without consequence.
#
# The basic idea is to maintain a 1-D array that keeps track of the maximal value we can get for a certain amount of
# weight. We can loop from the largest value to the smallest value to ensure we do not use a given object twice.
# Looping backwards ensures we only ever use DP values from the previous row which is equivalent to the 2-D DP except
# we can save some memory.
#
# The dp state can then be calculated using dp[j] = max(dp[j], dp[j - weight[i]] + value[i]). We first set each array
# element to be -1 which means we have not reached that weight. If we have not reached that weight we should skip it
# and make sure to not compute the value for that index.
#
# Here is a graphic to demonstrate this idea. Note that when a weight is smaller than the array index we stop
# considering the index as it means our weight is greater than the current capacity of the knapsack.

from typing import List


def knapsack(weights: List[int], values: List[int], max_weight: int) -> int:
    # initialize the array and set values to -1 except for index 0
    dp = [-1] * (max_weight + 1)
    dp[0] = 0
    # loop through the objects
    for i in range(len(weights)):
        # loop through the dp indexes from largest value to smallest one
        for j in range(max_weight, weights[i] - 1, -1):
            # check if we have reached the weight value before
            if dp[j - weights[i]] != -1:
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    return max(dp)


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    max_weight = int(input())
    res = knapsack(weights, values, max_weight)
    print(res)
