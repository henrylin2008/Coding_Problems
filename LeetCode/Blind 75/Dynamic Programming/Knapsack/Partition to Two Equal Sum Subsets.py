# Partition to Two Equal Sum Subsets
# https://algo.monster/problems/partition_equal_subset_sum
#
# Input
#   nums: the array
# Output
# if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal
#
# Examples
# Example 1:
# Input:
#   nums = [3, 4, 7]
# Output: true
#
# Explanation:
# The array can be partitioned as [3,4] and [7].
#
# Example 2:
# Input:
# nums = [1, 5, 11, 5]
# Output: true
#
# Explanation:
# The array can be partitioned as [1, 5, 5] and [11].

# Solution
# Brute Force
# First, the sum of each subset should be the sum of the entire array divided by 2, sum(nums) / 2, we will call it
# target. If the original sum is odd, we can immediately return false as it is impossible to find two equal subset
# sums where the sum is odd by parity rules.
#
# The immediate approach would be to brute force all possible sums and check if a sum of target is possible. The
# following is a space-state tree of this idea:
#
# In the figure, we continue search despite already having found target, but once we find it, we can return true.
# Furthermore, if we notice that the current sum is greater than target, we also don't need to keep searching,
# but is not done in the figure for clarity. The following is an implementation of all these ideas combined:

def target_exists(n, nums, target_sum, current_sum):
    # target sum is possible
    if current_sum == target_sum:
        return True

    # impossible if no more elements or current sum exceeds target sum
    if n == 0 or current_sum > target_sum:
        return False

    # use or dont use element
    exists = target_exists(n - 1, nums, target_sum, current_sum + nums[n - 1]) or \
             target_exists(n - 1, nums, target_sum, current_sum)
    return exists


def can_partition(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(nums)
    return target_exists(n, nums, target, 0)

# The runtime is O(2^n) in the worst case since there are n items, and each item has two possibilities: either
# include it in the sum or don't. Since this is implemented recursively, the space complexity is O(n) since there are
# at most n items on the memory stack at any given moment.
