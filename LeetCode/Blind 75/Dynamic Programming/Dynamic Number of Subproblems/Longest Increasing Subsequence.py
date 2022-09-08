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


# DFS + Memoization
# The keywords "longest" and "sequence" are good indicators of dynamic programming.
#
# Let's try thinking about a dp solution. First, what is the overall problem that we want to solve? It's "what is the
# LIS of a sequence of N numbers?"
#
# What is the dp state? Typically when you think of a dp solution for sequences, we consider a prefix of the original
# sequence. In this case the state is: considering the first i numbers (nums[1], nums[2], ... nums[i]), what is the
# longest increasing subsequence that contains nums[i]?
#
# Next, the transition. If we want to build an LIS that ends with nums[i], then we need to find a previously
# exisiting LIS that ends with a number less than nums[i]. In order words, find the largest existing LIS (j < i)
# where nums[j] < nums[i], and simply append nums[i] to that LIS!

# A simple base case would be if i = 0 then return 0 since if we don't have any elements the longest increasing
# subsequence is of length 0.
#
# Here's a summary of the dp relationship:
#   -state: f(i) is the longest increasing subsequence that ends/contains nums[i].
#   -base case: f(0) = 0: an empty list has an LIS of length 0.
#   -transition: f(i) = max(f(j) + 1) for j = 0 ... i-1 as long as nums[j] < nums[i] (extend a pre-existing LIS)

# As usual with problems with recursive relations, we store a memo table to store answers that may be reused to stop
# unnecessary recomputations.

global lis  # global variable to store answer


def f(i, nums, memo):
    global lis

    if i == 0:
        return 0

    if memo[i] != 0:  # if already computed, use said answer
        return memo[i]

    len = f(0, nums, memo) + 1  # begin with starting a new LIS
    ni = nums[i - 1]
    for j in range(1, i):  # try building upon a pre-existing LIS
        nj = nums[j - 1]
        f_of_j = f(j, nums, memo)  # compute f(j), otherwise if nums[i] < nums[j] then f(j) will never be computed
        if nj < ni:
            len = max(len, f_of_j + 1)

    # LIS can end anywhere in the sequence due to the definition of our state, so update each time
    lis = max(lis, len)

    memo[i] = len
    return len


def longest_sub_len(nums):
    global lis
    lis = 0
    n = len(nums)
    memo = [0] * (n + 1)
    f(n, nums, memo)
    return lis
