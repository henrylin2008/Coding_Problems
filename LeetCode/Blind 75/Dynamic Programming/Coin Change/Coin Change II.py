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
