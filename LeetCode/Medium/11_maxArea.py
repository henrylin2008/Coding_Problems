# 11. Container With Most Water
# link: https://leetcode.com/problems/container-with-most-water/
# Give n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
# drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
# a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

def maxArea(height):
    left = 0
    right = len(height) -1
    result = 0

    while left < right:
        area = min(height[left], height[right])*(right-left)
        # calculate temporary area; By using lowest height b/t 2 pointers (=highest of water can be contained), then
        # multiply it with the length (right-left)

        if area > result: # if area is > result, then set the area as new result
            result = area

        if height[left] < height[right]: # determine which pointer to move (left or right)
            # if the value of current (left) pionter is less than the right pointer
            left += 1 # move left pointer one position to the right
        else:
            right -= 1 # move right pointer one position to the left
    # print(result)
    return result

# maxArea([1,8,6,2,5,4,8,3,7])