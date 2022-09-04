# Coin Change
# Link: https://algo.monster/problems/coin_change
#
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation:
# 11 = 5 + 5 + 1, 3 total coins
#
# Example 2:
# Input: coins = [3], amount = 1
# Output: -1


# Solution
# Brute Force
# This is a classical problem very similar to the unbounded knapsack problem.
#
# A brute force method enumerates all possibilities with the use of backtracking. We start with a total sum of 0 and
# try every denomination. Since we can use each denomination more than once, after we use it we try every
# denomination again until we reach the target.

# The run time is O(n^{amount / T}) where T is the minimum denomination. The space complexity is amount / T since the
# recursive tree will be at most amount / T deep at any given time.

from math import inf


def min_coins(coins, amount, sum):
    if sum == amount:
        return 0

    if sum > amount:
        return inf

    ans = inf
    for coin in coins:
        result = min_coins(coins, amount, sum + coin)
        if result == inf:
            continue
        ans = min(ans, result + 1)

    return ans


def coin_change(coins: List[int], amount: int) -> int:
    result = min_coins(coins, amount, 0)
    return result if result != inf else -1


# DFS + Memoization
# We can optimize the brute force solution by storing answers that have already been computed in a 1D array called
# dp, where dp[i] is the minimum number of denominations required to get a sum of i. This is slightly different from
# our classical knapsack problems, but the idea is mostly similar. The reason we don't add an extra dimension is
# because the use of items is unbounded (i.e. every item can be used an infinite number of times). Thus, the number
# of items, as a dimension, holds no meaning in our specific implementation.

from math import inf


def min_coins(coins, amount, sum, memo):
    if sum == amount:
        return 0

    if sum > amount:
        return inf

    if memo[sum] != -1:
        return memo[sum]

    ans = inf
    for coin in coins:
        result = min_coins(coins, amount, sum + coin, memo)
        if result == inf:
            continue
        ans = min(ans, result + 1)

    memo[sum] = ans
    return ans


def coin_change(coins: List[int], amount: int) -> int:
    memo = [-1] * (amount + 1)
    result = min_coins(coins, amount, 0, memo)
    return result if result != inf else -1
