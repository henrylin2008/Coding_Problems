# Longest Increasing Subsequence
# Link: https://algo.monster/problems/longest_increasing_subsequence

# Input
#   nums: the integer sequence
# Output
#   the length of longest subsequence
#
# Examples
# Example 1:
# Input:
#   nums = [50, 3, 10, 7, 40, 80]
# Output: 4
#
# Explanation:
# The longest subsequence is [3, 7, 40, 80] which has length 4.
#
# Example 2:
# Input:
# nums = [1, 2, 4, 3]
# Output: 3
#
# Explanation:
# Both [1, 2, 4] and [1, 2, 3] are longest subsequences which have length 3.

# Solution
# Brute Force
# A brute force method traverses through all 2^N possible subsequences, which is essentially generating all subsets.
# There are 2^N since, for every element, we either include it or exclude it. Then, for every subsequence,
# we check if it is increasing in O(N) time.
#
# The final time complexity is going to be O(N * 2^N) and the space complexity is also O(N * 2^N) since we must
# generate and store all O(2^N) subsets each of length O(N). The following is the implementation of this idea:

# function to generate all 2^N subsets and store them into the list subsets
def generate_subsets(nums):
    n = len(nums)
    res = [[]]

    def dfs(i, cur):
        if i == n:
            return
        res.append(cur + [nums[i]])
        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)

    dfs(0, [])
    return res


# function to check if list nums is strictly increasing
def is_increasing(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i - 1] >= nums[i]:
            return False
    return True


# function to get all subsequence and find longest increasing subsequence
def longest_sub_len(nums):
    subsets = generate_subsets(nums)
    mx_len = 0
    for subset in subsets:
        if is_increasing(subset):
            mx_len = max(mx_len, len(subset))
    return mx_len
