# Subarray Sum
# https://algo.monster/problems/subarray_sum

# Given an array of integers and an integer target, find a subarray that sums to target and return the start and end
# indices of the subarray.
#
# Input: arr: 1 -20 -3 30 5 4 target: 7
#
# Output: 1 4
#
# Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).

# Intuition
# The brute force way is to find the sum of each subarray and compare it with the target. Let N be the number of
# elements in the array. There are N subarrays with size 1, N-1 subarrays with size 2 .. and 1 subarray with size N.
# Time complexity is O(N^2).
#
# A key observation is that the sum of a subarray [i, j] is equal to the sum of [0, j] minus the sum of [0, i - 1].
#
#
#
# The sum of elements from index 0 to i is called the prefix sum. If we have the subarray sum for each index,
# we can find the sum of any subarray in constant time.
#
# With the knowledge of the prefix sum under our belt, the problem boils down to Two Sum. We keep a dictionary of
# prefix_sum: index while going through the array calculating prefix_sum. If at any point, prefix_sum - target is in
# the dictionary, we have found our subarray.
#
# Time Complexity: O(n)
