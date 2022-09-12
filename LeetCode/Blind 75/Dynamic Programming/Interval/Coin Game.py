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
