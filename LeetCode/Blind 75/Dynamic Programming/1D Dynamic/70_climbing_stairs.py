# link: https://leetcode.com/problems/climbing-stairs/
# Climbing stairs: Easy
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
# Constraints:
#
# 1 <= n <= 45

# Solution idea: dynamic programming - Bottom up and memoization/cache (use the previous calculated values)
# ex: n = 5:
# stairs:      0      1       2      3        4       5
# DP:        5+3=8   3+2=5   2+1=3  1+1=2     1       1
# from:      1,2     2,3     3,4    4,5     (base cases)
#                                             one    two
#                                 one+two    two
#                           one+two  two
#                 one+two   two
#          one+two   two
# Time: O(n); looping through the ints
# Space: O(1); only using 2 variables 
class Solution:
    def climb_stairs(self, n: int) -> int:
        one, two = 1, 1     # base cases

        for i in range(n - 1):  # range is 0 - 3, outside from 2 base cases
            temp = one      # temp variable for var one
            one = one + two  # update one (sum of 2 previous variables)
            two = temp      # move two to the original one position (temp)

        return one
