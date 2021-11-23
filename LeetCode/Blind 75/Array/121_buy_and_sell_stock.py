# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# 121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
#
#
# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Solution: use 2 pointers: left and right pointer, left pointer = buy (lowest), right pointer = sell (highest);
# set left pointer (lowest), then keep sliding the right pointer and find the max profit, update max profit when a
# higher right pointer is found; update left pointer if a lower value than left point is found, return the max profit

class Solution:
    # Time: O(n)
    # Space: O(1); only use 2 pointers
    def maxProfit(self, prices) -> int:  # prices: List[int]
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:    # if profitable? when left pointer is right pointer
                profit = prices[right] - prices[left]   # find the profit
                max_profit = max(max_profit, profit)    # compare the current max profit and the new profit
            else:   # when right pointer is lower than the left pointer
                left = right    # set the left pointer to the right pointer
            right += 1      # move the right pointer
        return max_profit
