# Longest Common Subsequence
# https://algo.monster/problems/longest_common_subsequence

# Given two strings word1 and word2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
# while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
# Input:
#   word1 = "abcde"
#   word2 = "ace"
#
# Output: 3
# Explanation:
# The longest common subsequence is ace and its length is 3.
#
# Example 2:
# Input:
#   word1 = "almost"
#   word2 = "algomonster"
# Output: 6
# Explanation:
# The longest common subsequence is almost and its length is 6.
#
# Example 3:
# Input:
# word1 = "abc"
# word2 = "def"
# Output: 0
# Explanation:
# There is no such common subsequence, so the result is 0.

# Solution
# Brute Force
# The brute force solution is to generate every possible subsequence, which is essentially generating subsets of the
# string, in O(2^n) time, where n is the length of the string, using a combinatorial search. Once we have every
# subsequence of both strings of length n and length m, we compare every pair of subsequences in O(n * m) time,
# keeping track of which matching pair has the longest length. The final time complexity would be O(2^n + 2^m + n *
# m) which simplifies to O(2^n + 2^m).

def generate_subsequences(s, n, ans, subsequences):
    if n == 0:
        subsequences.append(ans)
        return
    generate_subsequences(s, n - 1, s[n - 1] + ans, subsequences)
    generate_subsequences(s, n - 1, ans, subsequences)


def longest_common_subsequence(word1, word2):
    word1_subsequences = []
    word2_subsequences = []
    generate_subsequences(word1, len(word1), "", word1_subsequences)
    generate_subsequences(word2, len(word2), "", word2_subsequences)

    longest_match_length = 0
    for subsequence1 in word1_subsequences:
        for subsequence2 in word2_subsequences:
            if subsequence1 == subsequence2:
                length = len(subsequence1)
                longest_match_length = max(longest_match_length, length)

    return longest_match_length
