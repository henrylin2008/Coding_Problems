# Reorganize String
# https://algo.monster/problems/reorganize_string

# Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are
# not the same.
#
# If possible, output any possible result. If not possible, return the empty string.
#
# Example 1:
# Input:s = "aab"
# Output: aba
# Example 2:
# Input:s = "aaab"
# Output: ``
# Note:
# s will consist of lowercase letters and have length in range [1, 500].

# Solution
# We divide the indices of the string into two: odds and evens. In that case, elements with odd indices can only be
# adjacent to elements with even indices, and vice versa. Note that because the index starts at zero, there will
# always be more or equal evens than odds. If there are more of one character than the number of evens,
# it is impossible to rearrange the string so no adjacent characters are the same. Otherwise, we can start from the
# character that occurs the most and fill out spots with even indices. Once we run out of spots to fill, we fill out
# the spots with odd indices. In this case, the result will guarantee to have no same adjacent characters.
#
# For the implementation, we use a heap to guarantee the character that is repeated the most is processed first,
# and because the character repeated the most changes as we process more characters.
