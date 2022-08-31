# Knapsack, Weight-Only
# https://algo.monster/problems/knapsack_weight_only

# Given a list of n items and their weights, find all sums that can be formed using their weights.
#
# Input
# weights: A list of items and their weights.
# Output
# A list of possible sums using the weights.
#
# Examples
# Example 1:
# Input: weights = [1, 3, 3, 5]
# Output: [0, 1, 3, 4, 5, 6, 7, 8, 9, 11, 12]
#
# Explanation:
# We can form all sums from 0 to 12 except 2 and 10. Here is a short explanation for the sums:
# 0: use none of the weights
# 1: use item with weight 1
# 3: use item with weight 3
# 4: use weights 1 + 3 = 4
# 5: use item with weight 5
# 6: use weights 3 + 3 = 6
# 7: use weights 1 + 3 + 3 = 7
# 8: use weights 3 + 5 = 8
# 9: use weights 1 + 3 + 5 = 9
# 11: use weights 3 + 3 + 5 = 11
# 12: use all weights
#
# Constraints
# 1 <= len(weights) <= 100
# 1 <= weights[i] <= 100

# Solution
# Brute Force
# A brute force method enumerates all possibilities. We start with a total sum of 0 and process every item by either
# choosing to include it into our sum or not into our sum. Once no more items are left to process, we can include the
# final sum in a list of sums. Additionally, we will store these sums in a set since there can be repeating sums.
#
# By going through every possibility, we're generating all possible subsets, so we guarantee that we are also
# generating all possible sums.
#
# Since there are n items, two possibilities each, and it takes O(1) to compute each possibility, the final runtime
# is O(2^n).
#
# The following is the space-state tree for this idea using input [1, 3, 3, 5]. Each level i of the tree represents a
# binary decision to include or not include the ith number. For example, we have two branches in level i = 1,
# the left branch means not picking the ith item 3, and the right branch means picking it.

def generate_sums(weights, sums, sum, n):
    if n == 0:
        sums.add(sum)
        return
    generate_sums(weights, sums, sum, n - 1)
    generate_sums(weights, sums, sum + weights[n - 1], n - 1)


def knapsack_weight_only(weights):
    sums = set()
    n = len(weights)
    generate_sums(weights, sums, 0, n)
    return list(sums)


# Top-down Dynamic Programming
# First, the "top-down" solution is, basically, the brute force solution but with memoization. We store results that
# have already been computed and return them once needed. But in precisely what way should we store/represent the
# data? Going back to the idea of dynamic programming, we should consider what is important so far and if any of the
# information has been recomputed.
#
# Memoization, identifying the state
# To memoize, we need to find the duplicate subtrees in the state-space tree.
#
# Notice that the duplicate subtrees are of the same level for this problem. This isn't a coincidence.
#
# Unlike Word Break and Decode Ways in the backtracking section, the items in the knapsack problem can only be used
# once.
#
# Node A's subtree has leaf values of 3 and 8. And Node B's subtree has leaf values of 3, 8, 6, 11. They are clearly
# not the same subtree. This is because the meaning of a node's value is the weight sum by considering items from 0
# to i.
#
# Therefore, the state we need to memoize consists of the level/depth of the node and the node value itself. We will
# use (i, sum) to denote this.
#
# Thus, we will store a 2D boolean array memo where memo[i][sum] = true if the (i, sum) pair has already been
# computed and false otherwise. The size of the array is n * total_sum where n is the number of items and total_sum
# is the weight sum of all items. We need a slot for each possible weight we can make up, and all the possible
# weights are in the range of 0 to total_sum.

def generate_sums(weights, sums, sum, n, memo):
    if memo[n][sum]:
        return
    if n == 0:
        sums.add(sum)
        return
    generate_sums(weights, sums, sum, n - 1, memo)
    generate_sums(weights, sums, sum + weights[n - 1], n - 1, memo)


def knapsack_weight_only(weights):
    sums = set()
    n = len(weights)
    # find total sum of weights
    total_sum = sum(weights)
    memo = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    generate_sums(weights, total_sums, 0, n, memo)
    return list(sums)


# Since there are n * totalSum states, each state depends on O(1) subproblems, and each state takes O(1) to compute,
# and the final runtime is O(n * totalSum).

# Bottom-up Dynamic Programming
# Now let's talk about the "bottom-up" solution. Recall that the idea of any bottom-up The solution is to work from
# the smallest cases, "combine" them together, and continue this until we get to our desired solution. Thus,
# by looping through each item, we determine which sums we can construct based on if there exists a smaller sum that
# we can build on top of. For example, suppose we already built all possible sums using [1, 3, 3], and we wanted to
# know which sums we can build using all of [1, 3, 3, 5] now. The following is an illustration of this idea:


def knapsack_weight_only(weights):
    n = len(weights)
    total_sum = sum(weights)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            # vertical blue arrow in the above slides
            dp[i][w] = dp[i][w] or dp[i - 1][w]
            # diagonal blue arrow in the above slides
            if w - weights[i - 1] >= 0:  # make sure the current item's weight is smaller than the target weight w
                dp[i][w] = dp[i][w] or dp[i - 1][w - weights[i - 1]]
    ans = []
    # check the last row for all possible answers
    for w in range(0, total_sum + 1):
        if dp[n][w]:
            ans.append(w)
    return ans


# The final runtime of this program is O(n * totalSum) because there is O(n * totalSum) states, each state depends on
# O(1) subproblems, and each state takes O(1) to compute.

# Space Optimization (optional)
# Finally, there is a slight memory optimization that we can perform. Observe that dp[i][w] depends on, at most,
# the previous row (dp[i][w] = dp[i][w] || dp[i - 1][w - weights[i - 1]]). Thus, instead of storing the entire 2D
# array, we can simply store two 1D arrays, one to keep track of the previous and one to for the current. This
# improves our memory usage from O(n * totalSum) to O(totalSum).
#
# Here's the implementation:

from typing import List


def knapsack_weight_only(weights: List[int]) -> int:
    n = len(weights)
    total_sum = sum(weights)  # get maximum sum possible

    # initialize 2 1D arrays (2 * N array)
    dp = [[False for _ in range(total_sum + 1)] for _ in range(2)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for w in range(0, total_sum + 1):
            # current row is dp[1], previous row is dp[0]
            dp[1][w] = dp[1][w] or dp[0][w]
            if w - weights[i - 1] >= 0:
                dp[1][w] = dp[1][w] or dp[0][w - weights[i - 1]]
        for w in range(0, total_sum + 1):  # update previous row to current row
            dp[0][w] = dp[1][w]

    # dp[0][w] = true if `w` is an attainable weight, thus add it to our answer
    ans = []
    for w in range(0, total_sum + 1):
        if dp[0][w]:
            ans.append(w)
    return ans


if __name__ == '__main__':
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    res.sort()
    for i in range(len(res)):
        print(res[i], end='')
        if i != len(res) - 1:
            print(' ', end='')
    print()

# The space optimization is a nice trick but it's also easy to get the row swapping wrong. It's great to mention this
# to the interviewer after you have perfected your regular solution and confirm that with the interviewer. Pre-mature
# optimization is the root of all evil in software engineering.
