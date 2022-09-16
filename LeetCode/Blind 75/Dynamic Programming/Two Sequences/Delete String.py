# Delete String
# https://algo.monster/problems/delete_string

# Given 2 strings determine the minimum cost required to delete characters from either string to make them equal. We
# also assign a particular cost to each character so that in order to remove one instance of that character from
# either string it will inccur that cost. Only lower-case English letters will be used. The answer is guarenteed to
# fit in a 32-bit integer.
#
# Input
#   costs: An array of size 26 that contains the cost for each character in the order of a-z
#   s1: First string
#   s2: Second string
# Output
# Minimum cost to make the strings equal
#
# Examples
# Example 1:
# Input:
#   costs = [1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#   s1 = abb
#   s2 = bba
# Output: 2
#
# Explanation:
# We can remove a from both string to make bb in both strings with only a cost of 2.

# Solution
# This problem is very similar to Edit Distance. The difference is now the only operation is delete and there is a
# cost for it.
#
# Let dp[i][j] denote the minimum total cost to make substrings s1[:i] and s2[:j] equal. To get dp[i][j],
#
# If s1[i] and s2[j] are the same character, then we don't have to incur any delete cost, we simply use the total
# cost without the last character dp[i - 1][j - 1].
#
# Else, we can delete the last character from either s1 or s2 and add the cost. We take the minimum of the two.
#
# dp[i][j] = min(dp[i - 1][j] + cost_to_remove_last_character_from_s1, dp[i][j - 1] +
# cost_to_remove_last_character_from_s2)
