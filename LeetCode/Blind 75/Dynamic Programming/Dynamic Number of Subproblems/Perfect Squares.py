# Perfect Squares
# https://algo.monster/problems/perfect_squares

# Given a number that is less than 10^5 determine the smallest amount of perfect squares needed to sum to a
# particular number? The same number can be used multiple times.
#
# Example 1:
# Input: 12
# Output: 3
# Explanation:
# 12 = 4 + 4 + 4
#
# Example 2:
# Input: 13
# Output: 2
# Explanation:
# 13 = 4 + 9

# Solution
# The answer is to use dynamic programming either bottom-up or top-down and to maintain the least number of numbers
# to get a certain sum. Alternatively you can use a graph theory algorithm such as bfs to solve this question as well
# using a queue. The solution displayed uses a bottom-up dynamic programming approach, the other solutions may serve
# as good practice for practicing other algorithms.

# Time Complexity: O(n*sqrt(n))

from math import sqrt


def perfect_squares(n: int) -> int:
    # set to arbitrarily high value, 10000 was chosen here but one only needs a sufficiently large value
    dp = [10000] * (n + 1)
    dp[0] = 0
    # we only need to loop up to the square root of the number so we don't exceed it
    for i in range(1, int(sqrt(n)) + 1):
        cur = i * i
        for j in range(cur, n + 1):
            dp[j] = min(dp[j], dp[j - cur] + 1)
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    res = perfect_squares(n)
    print(res)
