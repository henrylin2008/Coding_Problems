# Link: https://leetcode.com/problems/min-cost-climbing-stairs/
# Min Cost Climbing Stairs: Easy
#
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost,
# you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#
#
# Constraints:
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

# solution: DP and calculate it from right to the left.
# ex: [10, 15, 20], add 0 to the end as the top of the array: [10, 15, 20], 0
# set the starting point at the second to the last index (ex: 15), then calculate the minimum cost between one step
# (ex: 15+20) or 2 steps jump (15+0);
# starting: 15, min((15+20), (15+0)) => 15
# next: 10: min((10+15), (10+20)) => 25
# return min(first, second idx) = min(25, 15) => 15

# Time: O(n); iterate through the array in reverse
# Space: O(1); only storing 2 variables
class Solution:
    def min_cost_climbing_stairs(self, cost) -> int: # cost: # List[int]
        cost.append(0)      # add 0 to the end of the array as the top of the floor

        for i in range(len(cost) - 3, -1, -1):  # reverse the array, starting from the top (len + 1), until it reaches
            # to the beginning of the array
            # ex: [10, 15, 20] 0; add 0 to the end of the array, as 0 is the top of the floor
            # len(cost) - 3: second to the last index (ex: 15), since it could jump 2 steps
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])
