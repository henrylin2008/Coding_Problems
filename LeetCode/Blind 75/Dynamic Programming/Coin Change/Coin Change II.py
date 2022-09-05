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


# Bottom-Up DP
# This can also be done iteratively in a similar way to the unbounded knapsack problem. Once again, the idea of
# bottom-up DP is to, instead of going from top-down, we build our solution from the bottom-up. Here is the iterative
# implementation:
def coin_game(coins, amount):
    N = len(coins)

    dp = [[0 for _ in range(amount + 1)] for _ in range(N + 1)]

    dp[0][0] = 1  # there is only 1 way to make a sum of 0 using none of the coins
    for i in range(1, N + 1):
        for s in range(0, amount + 1):
            dp[i][s] = dp[i - 1][s]  # first take the number of ways to make `s` without the `i`th item
            if s - coins[i - 1] >= 0:
                dp[i][s] += dp[i][s - coins[i - 1]]  # then, try the `i`th item (if it's valid to use)

    return dp[N][amount]


# Once again, the idea for this solution is extremely similar to that of the Unbounded Knapsack.
#
# Note the order of the loops. We first loop through all coins, then amounts. You may think that with our top-down
# recursive solution, we would first loop through all amounts then coins. However, that would be incorrect.
#
# Why? Because then we would be overcounting the number of ways since our DP definition actually changes to be dp[i][
# s] is the number of ways to construct the amount s using all coins. This is akin to the start value we pass in the
# function in Combination Sum to remove duplicates. We must keep our definition to be dp[i][s] is the number of ways
# to construct the amount s using the first i coins, otherwise there will be duplicates.


# Memory Optimization
# Notice that our transition dp[i][s] += dp[i][s - coins[i - 1]] only depends on the previous row. Thus,
# we can optimize our solution from O(n * amount) to O(amount) by only storing the previous and current row. Once
# again, for a detailed explanation, visit the Knapsack Introduction article.
#
# Here is the implementation:
from typing import List


def coin_game(coins: List[int], amount: int) -> int:
    N = len(coins)

    # dp[0][...] is the previous row
    # dp[1][...] is the current row
    dp = [[0 for _ in range(amount + 1)] for _ in range(2)]

    dp[0][0] = 1  # there is only 1 way to make a sum of 0 using none of the coins
    for i in range(1, N + 1):
        for s in range(0, amount + 1):
            dp[1][s] = dp[0][s]  # first take the number of ways to make `s` without the `i`th item
            if s - coins[i - 1] >= 0:
                dp[1][s] += dp[1][s - coins[i - 1]]  # then, try the `i`th item (if it's valid to use)

        for s in range(0, amount + 1):  # current row becomes previous row for the next iteration
            dp[0][s] = dp[1][s]

    return dp[0][amount]


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_game(coins, amount)
    print(res)

# The time complexity is still O(n * amount) where n is the number of items, but now the space complexity is O(
# amount) since we only have two amount sized 1D arrays.
