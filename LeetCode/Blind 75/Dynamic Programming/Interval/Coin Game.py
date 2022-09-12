# Interval Dynamic Programming | Coin Game
# https://algo.monster/problems/coin_game

# Interval DP is another sub-type of the dynamic programming technique that deals with ranges or intervals. In
# general, the final answer to interval DP problems will be the answer to the entire range [1, n], where subproblems
# are computed by finding the answer to all possible ranges, [l, r] where l <= r. Alternate names for interval DP are
# left-right DP or L-R DP.
#
# Interval DP is one of the more challenging types of dynamic programming problems. They might be too difficult for
# the real interviews. We are including them here for completeness. Don't sweat if you can't get it the firs time.
#
# Coin Game
# There are n coins in a straight line. The ith coin has a value of coins[i]. You play this game with a friend
# alternating turns, starting with you, remove one coin from one end of the line and add that coin's value to your
# score.
#
# If your friend plays perfectly in such a way that maximizes their score, what is your maximum possible score?
#
# Input
# coins: A list of the coins.
# Output
# Your maximum possible score, provided that you go first and your friend plays perfectly.
#
# Examples
# Example 1:
# Input:
#   coins = [4, 4, 9, 4]
# Output: 13
#
# Explanation:
# The coins start like this:
# 4, 4, 9, 4
# You always go first, so you take the 4 from the left side:
# 4, 9, 4
# Your friend takes any of the 4s (it doesn't matter)
# 9, 4
#
# Now you take the 9, and your friend takes the remaining 4.
#
# Your score in this case, is 4 + 9 = 13.
#
# Constraints
#   1 <= len(coins) <= 1000
#   1 <= coins[i] <= 5 * 10^5

# Solution
# Brute Force
# A brute force solution would enumerate through all possibilities. For each of the n turns, we either choose the
# left-most coin or the right-most coin and check which option maximizes our score.
#
# The 2 cases mentioned above are described as follows:
#   Case 1: We take coin l
#       -Coins in the range [l + 1, r] are left
#       -Since our opponent plays optimally, they will gain points equal to maxScore(l + 1, r)
#       -Since we get all other coins, our score will be sum(l, r) - maxScore(l + 1, r)
#   Case 2: We take coin r
#       -Coins in range [l, r - 1] are left
#       -Since our opponent plays optimally, they will gain points equal to maxScore(l, r - 1)
#       -Since we get all other coins, our score will be sum(l, r) - maxScore(l, r - 1)
#
# Next, we choose the case that gives us the greatest score, or minimizes the opponent's score. Therefore,
# the solution is either:
#   -maxScore(l, r) = max(sum(l, r) - maxScore(l + 1, r), sum(l, r) - maxscore(l, r - 1)) or
#   -maxScore(l, r) = sum(l, r) - min(maxScore(l + 1, r), maxScore(l, r - 1))
# Since there are n turns, 2 possibilities each turn, and takes O(n) to calculate the sum from l to r,
# the final runtime is O(n * 2^n).

def max_score(coins, l, r):
    if l == r:
        return coins[r]

    sum = 0
    for i in range(l, r + 1):
        sum += coins[i]

    left_pick = max_score(coins, l + 1, r)
    right_pick = max_score(coins, l, r - 1)
    return sum - min(left_pick, right_pick)


def coin_game(coins):
    n = len(coins)
    return max_score(coins, 0, n - 1)

# Slight Optimization
# So far, for each recursive call we are spending O(n) time to calculate the sum between the range [l, r]. However,
# instead of using O(n) every time we need the sum we can use a prefix sum array to get the range sum in O(1) time
# and a single O(n) pre-computation.

def max_score(coins, l, r):
    if l == r:
        return coins[r]
    sum = coins[r] - coins[l - 1]  # query sum from [l, r] in O(1)
    left_pick = max_score(coins, l + 1, r)
    right_pick = max_score(coins, l, r - 1)
    return sum - min(left_pick, right_pick)


def coin_game(coins):
    n = len(coins)
    prefix_sum = [0 for i in range(n + 1)]  # precompute prefix sum
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + coins[i - 1]
    return max_score(prefix_sum, 0, n - 1)


# Top-down DP

# In essence, the DP top-down solution is the brute force solution with memoization. You may have noticed maxScore(l,
# r) can be be memoized.
#
# Let’s formalize our idea above by specifying our DP state (i.e. what’s important that can lead us to our answer).
# In this case, let dp(l, r) be the maximum score we can achieve if coins in the range [l, r] are the only ones
# present and we go first.
#
# Furthermore, our base case is: dp(l, r) = v_r if l = r. That is, since the range contains only one coin,
# we simply take that coin.
#
# Now we deal with the transition. Exactly like our brute force solution, we consider two cases of picking either the
# left or right coin.
#
# Next, we choose the case that gives us the greatest score or minimizes the opponent's score. Therefore,
# the solution is either:
#   - dp(l, r) = max(sum(l, r) - dp(l + 1, r), sum(l, r) - dp(l, r - 1)) or
#   - dp(l, r) = sum(l, r) - min(dp(l + 1, r), dp(l, r - 1))

import sys
sys.setrecursionlimit(1500)


def max_score(dp, prefix_sum, l, r):
    if dp[l][r] != 0:
        return dp[l][r]

    sum = prefix_sum[r] - prefix_sum[l - 1]
    if l == r:
        dp[l][r] = sum
    else:
        dp[l][r] = sum - min(max_score(dp, prefix_sum, l + 1, r), max_score(dp, prefix_sum, l, r - 1))

    return dp[l][r]


def coin_game(coins):
    n = len(coins)
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    prefix_sum = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + coins[i - 1]
    return max_score(dp, prefix_sum, 1, n)


# Bottom-up DP
# The iterative version is a bit trickier. The idea is that we loop through all the possible lengths starting from 1
# to n. Then for each size, we consider all possible left starting positions and calculate the respective right
# ending position. We do it in this order because we are building solutions from the smallest case and building the
# solutions up. That is, first considering each item as an interval of length 1 then merging their solutions together
# to form larger and larger interval lengths until we get to an interval of size n.
#
# Note: There are slight tweaks in the implementation of this idea such as how we loop through the lengths.
from typing import List


def coin_game(coins: List[int]) -> int:
    n = len(coins)
    prefix_sum = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + coins[i - 1]

    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for size in range(0, n):
        for l in range(1, n - size + 1):
            r = l + size
            if l == r:
                dp[l][r] = prefix_sum[r] - prefix_sum[l - 1]
            else:
                dp[l][r] = prefix_sum[r] - prefix_sum[l - 1] - min(dp[l + 1][r], dp[l][r - 1])
    return dp[1][n]


if __name__ == '__main__':
    coins = [int(x) for x in input().split()]
    res = coin_game(coins)
    print(res)
