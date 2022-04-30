# 322. Coin Change
# Link: https://leetcode.com/problems/coin-change/
# Medium

# You are given an integer array coins representing coins of different denominations and an integer amount
# representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up
# by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
# Input: coins = [2], amount = 3
# Output: -1
#
# Example 3:
# Input: coins = [1], amount = 0
# Output: 0
#
#
# Constraints:
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

# Logic: Dynamic Programming - Button up; base case is dp[0] = 0 (zero coin), and an array with max value (amount + 1),
# go through every amount and every given coin, if the amount - current coin >= 0, then find the min coins to get to the
# amount (min(dp[a], 1 + dp[a - c])); return dp[amount] if it's not the default value else return -1
from typing import List


# Time: O(amount * len(coins)); given amount, given number of coins
# Space: O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)        # [max val]; [0, max_val, max_val, .... amount]
        dp[0] = 0   # base case
        for a in range(1, amount + 1):  # reverse order, going from 1 to amount; for every amount
            for c in coins:     # for every coin
                if a - c >= 0:  # if remainder of amount - current coin is not negative, continue searching
                    dp[a] = min(dp[a], 1 + dp[a - c])   # min coins; min(itself, 1(current coin) + dp[a-c](amt - c))
        return dp[amount] if dp[amount] != amount + 1 else -1   # return if the value is not the default value else -1
