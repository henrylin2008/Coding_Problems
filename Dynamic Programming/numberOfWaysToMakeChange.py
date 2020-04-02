# https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Make%20Change
# Number Of Ways To Make Change
# Level: Medium
# Given an array of positive integers representing coin denominations and a single non-negative integer representing a
# target amount of money, implement a function that returns the number of ways to make change for that target amount
# using the given coin denominations. Note that an unlimited amount of coins is at your disposal.

# Sample input: 6, [1, 5]
# Sample output:  2 (1x1 + 1x5 and 6x1)


# Time: O(nd); d is number of denomination
# Space: O(n); n is target amount

def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for amount in range(n+1)] # build an array (0) represents ways
    ways[0] = 1 # only one way to get 0, doing nothing
    for denom in denoms: # for every value in denoms
        for amount in range(1, n+1): # for every amount upto n (given amount)
            if denom <= amount: # when the denom is less or equal to the amount
                # print('ways[amount], ways[denom], ways[amount-denom]:', ways[amount], ways[denom], ways[amount-denom])
                ways[amount] += ways[amount - denom] # ways of current amount + ways for previous amount
                # print('ways[amount]:', ways[amount])
                # print()
    # print("ways[n]", ways[n])
    return ways[n]

# numberOfWaysToMakeChange(6, [1,5])