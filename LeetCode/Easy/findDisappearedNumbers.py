# 448. Find All Numbers Disappeared in an Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

def findDisappearedNumbers(nums):
    len_array = len(nums) + 1    # total length of array; +1 b/c range() = len() - 1
    a = set([i for i in range(1, len_array)])  # find all
    b = set