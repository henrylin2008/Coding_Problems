# Coin Change II
# https://algo.monster/problems/coin_change_ii

# You are given coins of different denominations and a total amount of money amount. Write a function to compute the
# number of combinations that make up that amount. If that amount of money cannot be made up by any combination of
# the coins, return 0.
#
# You may assume that you have an infinite number of each kind of coin.
#
# Input
#   -coins: A list of the coins and their denominations.
#   -amount: The target amount
# Output
# The number of combinations that make up that amount.
#
# Examples
# Example 1:
# Input:
#   1. coins = [1, 2, 5]
#   2. amount = 11
# Output: 4
#
# Explanation:
# There are four ways to make up the amount:
#   5 = 5
#   5 = 2 + 2 + 1
#   5 = 2 + 1 + 1 + 1
#   5 = 1 + 1 + 1 + 1 + 1
#
# Example 2:
# Input:
#   1. coins = [2]
#   2. amount = 3
# Output: 0
#
# Explanation:
# The amount of 3 cannot be made up with just coins of 2.
#
# Constraints
#   1 <= len(coins) <= 300
#   1 <= amount <= 5000
#   1 <= coins[i] <= 5000

# Brute Force
# A brute force method enumerates through all possibilities. We start with a total sum of 0 and try every
# denomination. Since we can use each denomination more than once, after we retry every denomination again until we
# reach our target.
#
# We essentially use the same idea used in Combination Sum where we try every single denomination while removing
# duplicate combinations by maintaining the starting indices.

def num_of_ways(sum, amount, start, coins):
    if sum == amount:
        return 1

    if sum > amount:
        return 0

    res = 0
    for i in range(start, len(coins)):
        res += num_of_ways(sum + coins[i], amount, i, coins)
    return res


def coin_game(coins, amount):
    return num_of_ways(0, amount, 0, coins)

# The runtime is going to be O(n^{amount / T}) where T is the smallest denomination since each sum branches into n
# combinations with a maximum depth of amount / T. The space complexity is amount / T since the recursion stack
# contains at most amount / T calls.


# DFS + Memoization
# We can slightly improve our runtime by reusing solutions that have already been computed. We apply memoization on
# the starting position as one dimension and the current sum as a second dimension since our function is really just
# f(start, sum), where we want to find the number of ways to reach amount starting with sum and using all coins
# starting from index start. For further details as to why we use two dimensions, please visit the Knapsack
# Introduction article.

def num_of_ways(sum, amount, start, coins, dp):
    if sum == amount:
        return 1

    if sum > amount:
        return 0

    if dp[start][sum] != -1:
        return dp[start][sum]

    res = 0
    for i in range(start, len(coins)):
        res += num_of_ways(sum + coins[i], amount, i, coins, dp)

    dp[start][sum] = res
    return res


def coin_game(coins, amount):
    n = len(coins)
    dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]
    return num_of_ways(0, amount, 0, coins, dp)

