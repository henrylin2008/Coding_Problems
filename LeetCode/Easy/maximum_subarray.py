# 53. Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Youtube: https://leetcode.com/problems/maximum-subarray/
# https://www.youtube.com/watch?v=eQGgk8zwIGI&list=PL2rWx9cCzU84eBz9Xfp9Rah5Fexq5yrh8&index=17&t=0s
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which
# is more subtle.
# Kadane's Algorithm, run O(n) time

def max_Subarray(nums):
    # initial max_current and max_global as first item in the array
    # max_current, max_global = A[0]
    # for i from 1 to length(A)-1:
    #     # max value between current index or sum of previous index and current index
    #     max_current = max(A[i], max_current + A[i])
    #     if max_current > max_global:
    #         max_global = max_current
    # return max_global

    if max(nums) < 0:
        return max(nums)

    current_max, global_max = 0, 0

    for i in nums:
        current_max = max(0, current_max + i)
        global_max = max(current_max, global_max)
    return global_max

