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


# The runtime is O(n * amount) since there are O(amount) states, each state takes O(n) to compute. The space
# complexity is O(amount) due to the 1D dp array.

# Bottom-up DP
# This can be done iteratively as well.
#
# First, similar to the top-down solution, let dp[i] be the minimum number of denominations required to get a sum of i.
#
# The idea is that we begin with dp[0] = 0 since it takes 0 coins to get a sum of 0. Next, we build up:
#   dp[1] = dp[0] + 1 = 1: We can build a sum of 1 using a coin of denomination 1 on top of the minimum number of coins
#   to get a sum of 0
#   dp[2] = dp[0] + 1 = 1: Similar to above, but we use a coin of denomination 2 on top of the answer for a sum of 0
#   dp[3] = dp[2] + 1 = 2: coin of denomination 1 on top of the answer for a sum of 2 or a 2 on top of a sum of 1.
#   Either case, the minimum is 2 coins.
#   dp[4] = dp[2] + 1 = 2: coin of denomination 2 on top of the answer for a sum of 2
#   dp[5] = min(dp[0], dp[3], dp[4]) + 1 = 1: either a coin of 5 on top of 0, a coin of 2 on top of 3, or a coin of 1 on
#   top of 4. The minimum is a 5 on top of 0.
#   dp[6] = min(dp[1], dp[4], dp[5]) + 1 = 2: either a coin of 5 on top of 1, a coin of 2 on top of 4, or a coin of 1 on
#   top of 5. The minimum is a 1 on top of 5.
#   ...
#   dp[n] = min(dp[n - 1], dp[n - 2], dp[n - 5]) + 1: We use a coin of denomination of either 1, 2, or 5 on top of the
#   minimum answer between the sums of n - 1, n - 2, or n - 5.


# Implementation
from math import inf
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    if amount == 0: return 0
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i - coin] + 1, dp[i])

    return dp[-1] if dp[-1] < inf else -1


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)

# Notice the small details in the implementation.
#
#      -We start with all values being maximum number possible to mean that the amount cannot be made up and to ensure
#      those values are not taken when we do min.
#      -If the target value is smaller than current coin value then the coin cannot be used since it would yield a
#      negative new target.
