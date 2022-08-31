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
