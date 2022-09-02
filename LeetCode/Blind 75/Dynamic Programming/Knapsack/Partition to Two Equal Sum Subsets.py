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


# Partition DP
# Top-down
# First, let's take a look at the following image:
#
# We can see that when we consider elements [3, 4, 7], the sum of 7 can be generated in two different ways. We can
# also see that the subtree beneath the nodes where the sum is 7, highlighted as node A and node B, are the exact
# same. Despite node A and node B being parts of different subtrees, adding level/number of items considered to the
# state makes the nodes 7 unique (are all the same). So, instead of recomputing these values everytime the sum is 7,
# we can immediately stop before going to deeper. Thus, we can store, in a table, if a subtree has been computed
# already and its value. A fully pruned space-state tree looks like this:
#
# We see that nodes that have already been computed still appear or are greater than the target sum still appear,
# but do not go deeper in their computation. This is the code for the following idea:

def target_exists(n, nums, target_sum, current_sum, dp):
    # target sum is possible
    if current_sum == target_sum:
        return True
    if n == 0 or current_sum > target_sum:
        return False
    if dp[n][current_sum] != 0:
        if dp[n][current_sum] == 1:
            return True
        else:
            return False

    exists = target_exists(n - 1, nums, target_sum, current_sum + nums[n - 1], dp) or \
             target_exists(n - 1, nums, target_sum, current_sum, dp)  # dont use element

    if exists:
        dp[n][current_sum] = 1
    else:
        dp[n][current_sum] = 2
    return exists


def can_partition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
    return target_exists(n, nums, target, 0, dp)

# The runtime of this solution is O(n * target) since there there are O(n * target) states, each state depends on O(
# 1) subproblems, and each state takes O(1) to compute. The runtime is also O(n * target + n) = O(n * target) because
# of the O(n * target) DP table and O(n) recursion stack depth.


# Bottom-Up
# The top-down solution may exceed the recursive stack depth So, we can implement the idea above iteratively. Once
# again, the idea of iterative or bottom-up dynamic programming is to start from the smallest case(s), and build our
# way up to the final solution.
#
# We will maintain a 2D table where dp[i][s] = true if we can form the sum s when considering the first i items.
# Otherwise, dp[i][s] = false. We can take our idea from the top-down solution by thinking about each item having two
# possibilities: including it in our sum or not. Thus, dp[i][s] = true if:
#
# the sum s can be formed without including the ith element, dp[i - 1][s] == true; or
# the sum s can be formed including the ith element, dp[i - 1][s - nums[i]] == true
# The following figures presents this idea when considering all elements [3, 4, 7, 6]:

# Notice that the base case dp[0][0] = true since we can always make a sum of 0 by choosing none of the elements.
# Here's the implementation:

def can_partition(nums):
    total_sum = sum(nums)

    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    n = len(nums)

    dp = [[False for s in range(target + 1)] for i in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for s in range(target + 1):
            if s < nums[i - 1]:
                dp[i][s] = dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s] or dp[i - 1][s - nums[i - 1]]

    return dp[n][target]
# The runtime of the code above is O(n * target) since there are O(n * target) states, each state depends on O(1)
# subproblems, and each state takes O(1) to compute. The space complexity is also O(n * target) with the use of the
# 2D DP table.
