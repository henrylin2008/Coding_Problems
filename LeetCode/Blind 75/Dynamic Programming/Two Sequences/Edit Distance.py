# Edit Distance
# https://algo.monster/problems/edit_distance

# There are two words word1 and word2, you have to find the minimum number of operations required to convert word1 to
# word2.
#
# You are allowed to use the following 3 operations on a word:
#   1. Insert a character
#   2. Delete a character
#   3, Replace a character
#
# Example 1:
# Input:
# word1 = "almost"
# word2 = "algomonster"
# Output:5
# Explanation:
#   1. almost    ->  algmost    (insert 'g')
#   2. algmost   ->  algomost   (insert 'o')
#   3. algomost  ->  algmonst   (insert 'n')
#   4. algomonst ->  algomoste  (insert 'e')
#   5. algomoste ->  algomoster (insert 'r')
#
# Example 2:
# Input:
#   word1 = "intention"
#   word2 = "execution"
# Output:5
# Explanation:
#   1. intention  ->  inention   (remove 't')
#   2. inention   ->  enention   (replace 'i' with 'e')
#   3. enention   ->  exention   (replace 'n' with 'x')
#   4. exention   ->  exection   (replace 'n' with 'c')
#   5. exection   ->  execution  (insert 'u')

# Solution
# This is the classic "Two Sequence DP".
#
# Let dp[i][j] be the minimum edit distance to change from substring of word1 ending at index i to substring of word2
# ending at index j.
#
# If word1[i] == word2[j], then edit distance d[i][j] = dp[i - 1][j - 1] since we don't have to pay any cost if the
# current character is the same.
#
# To get dp[i][j], we can do three things
#   1. match word1[i] to word2[j] and pay the replacement cost
#   2. match word1[i] to blank (delete word2[j])
#   3. match word2[j] to blank (add word1[i])

