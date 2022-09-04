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