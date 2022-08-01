# Palindrome Partitioning
# https://algo.monster/problems/palindrome_partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example 1:
# Input: aab
#
# Output:
#   [
#   ["aa","b"],
#   ["a","a","b"]
#   ]


# Explanation
#
# We try to remove prefix at each possible position and only continue if the prefix is a palindrome (since every
# substring has to be a palindrome).
#
#           a      |     a          b
#       Palindrome |
#           a            a     |    b
#           Palindrome         |
#           a            a          b   |
#           Not palindrome              |
#
# Space-state Tree
#                            aab
#                  a/        aa|    \ aab (x not Palindrome)
#                 ab           b
#               a/  \ab(x)   b/
#              b             '' (yes)
#           b /
#           '' (yes)
#
# We prune the tree by not branching out when the prefix is not a palindrome.
#
# Time Complexity: O(2^n)
#
# This is because once we determine a palindrome we work backwards to consider the other palindromes and enumerate them
# accordingly.


from typing import List


def partition(s: str) -> List[List[str]]:
    ans = []

    n = len(s)

    def is_palindrome(word):
        return word == word[::-1]

    def dfs(start, cur_path):
        if start == n:
            ans.append(cur_path[:])
            return

        for i in range(start + 1, n + 1):
            prefix = s[start: i]
            if is_palindrome(prefix):
                dfs(i, cur_path + [prefix])

    dfs(0, [])
    return ans


if __name__ == '__main__':
    s = input()
    res = partition(s)
    for row in res:
        print(' '.join(row))
