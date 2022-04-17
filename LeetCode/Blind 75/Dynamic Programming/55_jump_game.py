# 55. Jump Game
# https://leetcode.com/problems/jump-game/
# Medium

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in
# the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it
# impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

# Note: visualize the recursive tree, cache solution for O(n) time/mem complexity, iterative is O(1) mem,
# just iterate backwards to see if element can reach goal node, if yes, then set it equal to goal node, continue;

from typing import List


# Greedy solution
# Idea: solve the problem in the reverse order, set the goal on the last num, using the Greedy approach, check if
# previous num can reach the goal, if so, move the goal to the previous num, repeat the process until it reaches to the
# first num
# Time: O(n); only shifting the goal position (from right to left) if there's a path
# Space: O(1); no data structure used
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1        # goal = last position
        for i in range(len(nums) - 1, -1, -1):  # reverse loop through the nums
            if i + nums[i] >= goal:     # if current index + value at current idx >= goal (meaning can reach the goal)
                goal = i                # move goal to current i position (goal = i + 1)
        return True if goal == 0 else False     # True if the goal reaches to the first position else False
