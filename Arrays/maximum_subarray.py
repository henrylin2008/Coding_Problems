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
    # return max value of nums if it's < 0
    if max(nums) < 0:
        return max(nums)

    # set current max value and global max value to 0
    current_max, global_max = 0, 0

    for i in nums:
        # current max is max between 0 and current_max + i
        current_max = max(0, current_max + i)
        global_max = max(current_max, global_max)
    return global_max

# Follow-up: what if the elements can wrap around? For ex, given [8, -1, 3, 4], return 15, as we choose the numbers 3, 4,
# and 8 where teh 8 is obtained from wrapping around
# We split the follow-up problem into 2 parts. The first part is the same as before: finding the maximum subarray sum
# that doesn't wrap around. Next, we compute the maximum subarray sum that does wrap around, and take the maximum of the 2.
# To get the largest wrap-around sum, we can use a little trick. For any subarray that wraps around, there must be some
# continguous elements that are excluded, and these elements actually form the minimum possible subarray! therefore,
# we can first find the minimum subarray sum using exactly the method above, and subtract this from the array's total.
# For ex, in the example above, the minimum subarray is [-1], with a total of -1. we then subtrack this from the array
# total, 14, to get 15.

def maximum_circular_subarray(arr):
    max_subarray_sum_wraparound = sum(arr) - min_subarray_sum(arr)

    return max(max_subarray_sum(arr), max_subarray_sum_wraparound)

def max_subarray_sum(arr):
    max_ending_here = max_so_far = 0

    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

def min_subarray_sum(arr):
    min_ending_here = min_so_far = 0

    for x in arr:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far
