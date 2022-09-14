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


# Brute Force v2

# The next brute force solution will be slightly slower but will lead us to the dynamic programming solution
# smoother. The idea is to consider both strings at the "same" time. Remember that the overall problem is: What is
# the length of the LCS between strings word1 and word2?
#
# Recall: a prefix of a string is a substring that starts at the first character
#
# Let lcs(i, j) represent the length of the LCS between a prefix of word1 of length i and a prefix of word2 of length j.
#
# The most obvious solution we have is that if i = 0 or j = 0, then lcs(i, j) = 0 since there cannot be an LCS if one
# of the strings is empty.
#
# Next, let's try solving lcs(i, j) if i != 0 and j != 0. We can try splitting the problem into two cases:
#       1. word1[i] == word2[j]
#       2. word1[i] != word2[j]
#
# In case (1), since the letters match, we try keeping these letters as a part of our LCS and then find the LCS of
# the rest of the letters. So, lcs(i, j) = lcs(i - 1, j - 1) + 1, where lcs(i - 1, j - 1) is the LCS of the rest of
# the letters and the + 1 since the letters match.
#
# In case (2), since the letters don't match, we cannot keep these pair of letters and have to find the length of the
# longest LCS with the rest of the letters possible including letters i or j. So, lcs(i, j) = max{
#       lcs(i - 1, j)
#       lcs(i, j - 1)
#       lcs(i - 1, j - 1)}
#
# where lcs(i - 1, j) means keeping the jth letter but skipping the ith letter, lcs(i, j - 1) means keeping the ith
# letter but skipping the jth letter, and lcs(i - 1, j - 1) means skipping both letters.

# We can actually omit lcs(i - 1, j - 1) from case (2) since both lcs(i - 1, j) and lcs(i, j - 1) already depend on
# it. So, if lcs(i - 1, j - 1) is already optimal, its answer will be in either of the first two solutions.

def lcs(i, j, word1, word2):
    if i == 0 or j == 0:
        return 0

    res = 0
    if word1[i - 1] == word2[j - 1]:
        res = lcs(i - 1, j - 1, word1, word2) + 1
    else:
        res = max(lcs(i - 1, j, word1, word2), lcs(i, j - 1, word1, word2))
    return res


def longest_common_subsequence(word1, word2):
    n = len(word1)
    m = len(word2)
    return lcs(n, m, word1, word2)

# The reason this is slower than our first brute force solution is because this one runs in O(2^{n + m}) time since
# we are recursing through both strings at the same time instead of seperately.

