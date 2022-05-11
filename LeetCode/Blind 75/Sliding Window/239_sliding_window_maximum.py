# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
# Hard

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of
# the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right
# by one position.
#
# Return the max sliding window.
#
# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
import collections
from typing import List


class Solution:
    # Time: O(n); loop through the nums list once
    # Space: O(n); output to store
    # Idea: Monotonically decreasing queue: sliding window (l, r), in the window: if smaller value exists in the queue,
    #       remove it from the queue, then add current index to the queue; if left index out of bound, pop most left
    #       value from the queue; while within the window, append left index value (most value) to the output and shift
    #       left pointer, always shift right pointer, then return the output
    #       -use a deque (O(1) for popleft and remove right)
    #       -while q (deque) not empty and rightmost value < current value: pop rightmost (smaller) value from the q
    #       -add new (larger) value at the right idx
    #       -edge case: left index > leftmost value in the queue: popleft from the queue
    #       -if window is valid: add leftmost value from the queue to the output and shift left pointer
    #       -shift right pointer
    #       -return output
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()     # index (instead of its value)
        l = r = 0

        while r < len(nums):    # while r still inbound
            # pop smaller values from q and append a larger value (r) to the q
            while q and nums[q[-1]] < nums[r]:  # q is not empty and rightmost value in the queue < right pointer value
                q.pop()     # remove rightmost value (smaller value)
            q.append(r)     # append new value to the queue (if no smaller value existing in the queue)
            # if left value is out of bound, remove left val from the window
            if q[0] < l:    # if leftmost value (q[0] in the queue) is out of bound (l)
                q.popleft()  # remove leftmost value from the queue

            if (r + 1) >= k:    # window is at least size of k
                output.append(nums[q[0]])   # append leftmost value (max value) to the output
                l += 1      # only increment left pointer once the window at least in size of k
            r += 1          # increment right pointer

        return output
