# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Hard

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
# water it can trap after raining.
#
#
#
# Example 1: Input: height = [0,1,0,2,1,0,1,3,2,1,2,1] Output: 6 Explanation: The above elevation map (black section)
# is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being
# trapped.
#
# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

# ex: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# using 2 pointers: left pointer, right pointer
# init: maxL = 0
#       maxR = 1
# note: always shift the  pointer with less value (min(maxL, maxR)), if both are equal, shift left pointer
#           L    L   L   L   L   L   L   L   R   R   R   R
#           [0,  1,  0,  2,  1,  0,  1,  3,  2,  1,  2,  1]
#   idx:     0   1   2   3   4   5   6   7   8   9   10  11
# water cap: 0   0   1   0   1   2   1   0   0   1   0   0    => 1 + 1 + 2 + 1 + 1 = 6 (total)
# idx 1: 0 (maxL) - 1 (current idx value) = -1 --> 0 (water); update maxL(0) --> 1
# idx 2: 1 (maxL) - 0 (current idx value) = 1; maxL: 1
# idx 3: 1 - 2 = -1 --> 0; update maxL: 2 (current idx value); 2 > 1 (previous maxL)
# shift to right: maxL(2) > maxR(1)
# idx 10: 1 - 2 = -1 --> 0; update maxR: 2 (current idx value)
# idx 4: 2 - 1 = 1
# idx 5: 2 - 0 = 2
# idx 6: 2 - 1 = 1
# idx 7: 2 - 3 = -1 --> 0 ; update maxL: 3
# shift to right: maxL(3) > maxR(2)
# idx 9: 2 - 1 = 1
# idx 8: 2 - 2 = 0
from typing import List


# Time: O(n); loop through entire height
# Space: O(1); using 2 pointers, no data structure used
# Logic: using 2 pointers: left (0), right(last idx); left_max and right_max to keep track of current max on each
#        side; shifting pointer based off min(left_max, right_max); if shifting left pointer: move left pointer to
#        the next position, calculate left_max based off left_max and current idx value (height[left]), if
#        the calculation is > 0, add it to the result, otherwise water capacity is 0; do the same for the right pointer
#        lastly return the result
def trap(self, height: List[int]) -> int:
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    res = 0
    while left < right:
        if left_max < right_max:  # update left pointer
            left += 1
            left_max = max(left_max, height[left])
            res += left_max - height[left]
        else:                    # update right pointer
            right -= 1
            right_max = max(right_max, height[right])
            res += right_max - height[right]
    return res
