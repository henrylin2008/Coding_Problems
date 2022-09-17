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
