# Subsets
# https://algo.monster/problems/subsets_backtracking

# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example 1:
# Input: nums = [1,2,3]
#
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


# State-space tree
# Similar to permutations, we make a binary choice of whether to include the number in the subset at each level.


#                                  []
#                include /                  \ Don't include
#                   [1]                       []
#        include /      \ don't            /       \
#          [1, 2]        [1]             [2]        []
#  include /     \      /    \         /    \      /    \
#   [1,2,3]   [1,2] [1,3]   [1]    [2,3]   [2]   [3]    []

# Implementation
# We can use a state i to keep track of the index of the current char we are at.

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    res = []

    def dfs(i, cur):
        if i == n:
            res.append(cur)
            return

        dfs(i + 1, cur + [nums[i]])
        dfs(i + 1, cur)

    dfs(0, [])

    return res


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = subsets(nums)
    res = [' '.join(str(x) for x in sorted(subset)) for subset in res]
    res.sort()
    for row in res:
        print(row)
