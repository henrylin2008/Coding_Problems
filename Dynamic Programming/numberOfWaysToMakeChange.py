# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change
# Number Of Ways To Make Change
# Level: Medium
# Given an array of positive integers representing coin denominations and a single non-negative integer representing a
# target amount of money, implement a function that returns the number of ways to make change for that target amount
# using the given coin denominations. Note that an unlimited amount of coins is at your disposal.

# Sample input: 6, [1, 5]
# Sample output: 2 (1x1 + 1x5 and 6x1)

# Time: O(nd)
# Space: O(n)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)]
    way[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]