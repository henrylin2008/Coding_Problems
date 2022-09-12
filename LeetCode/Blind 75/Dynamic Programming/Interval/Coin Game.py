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
