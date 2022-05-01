# link: https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water
# Difficulty: Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
# water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1
#
# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# Note: shrinking window, left/right initially at endpoints, shift the pointer with min height;
from typing import List


# Time: O(n), loop through the height list
# Space: O(1), only using 2 pointers
# Note: using 2 pointers: left and right endpoints, move the pointer with a smaller value, height is the minimum between
# the 2 pointers; result is max between the result and the area
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])      # current area
            result = max(result, area)                      # max of the result or current area

            if height[l] < height[r]:           # if left < right: move left pointer to the next position
                l += 1
            else:                               # else: move right pointer to the next position (-1)
                r -= 1
        return result           # result
