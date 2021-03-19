# Algoexpert: https://www.algoexpert.io/questions/Non-Constructible%20Change
# Difficulty: Easy
# Non-Constructable Change
# Given an array of positive integers representing the values of coins in your possession, write a function that returns
# the minimum amount of change (the minimum sum of money) that you cannot create. The given coins can have any positive
# integer value and aren't necessarily unique (i.e., you can have multiple coins of the same value).
# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're
# given no coins, the minimum amount of change that you can't create is 1.
# Sample Input:
# coins = [5, 7, 1, 1, 2, 3, 22]
# Sample Output:
# 20

# time: O(nLog(n))
# space: O(1)
# Solution: sort coins in ascendant order, loop through the coins, if sum of seem coin/s + 1 < next coin, then return
# sum of seem coins + 1
# equation: if V > c + 1; then can't make c + 1 change
# c = change can be made with these coins
# V = next coin in sorted coins array
def nonConstructibleChange(coins):
    coins.sort()        # O(nlog(n)) time

    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:     # if current coin > sum of previous coins + 1
            # print(currentChangeCreated + 1)
            return currentChangeCreated + 1     # return sum of previous coins + 1
        currentChangeCreated += coin    # adds up the coins
    return currentChangeCreated + 1


# coins = [1, 1, 2, 3, 18]
# coins = [5, 7, 1, 1, 2, 3, 22]
# nonConstructableChange(coins)
