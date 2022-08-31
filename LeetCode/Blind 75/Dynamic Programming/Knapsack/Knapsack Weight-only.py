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
