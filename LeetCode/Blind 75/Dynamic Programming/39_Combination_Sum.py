# 39. Combination Sum
# Link: https://leetcode.com/problems/combination-sum/
# Medium

# Given an array of distinct integers candidates and a target integer target, return a list of all unique
# combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency of at least one of the chosen numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the
# given input.
#
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
#
#
# Constraints:
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):  # i: candidate; cur: current combination; total: target/sum
            if total == target:  # base case: if target is found
                res.append(cur.copy())  # add copy of current combination to the res
                return  # break out of the function
            if i >= len(candidates) or total > target:  # edge cases: out of bound, or total > target
                return  # exit
            # left branch: include current candidate
            print('cur, candidates[i]', cur, candidates[i])
            cur.append(candidates[i])  # add candidate to the current combination
            print('cur:', cur)
            dfs(i, cur,
                total + candidates[i])  # i, current(include the new candidate), new total (include new candidate)
            print('res:', res)
            # right branch: not include current candidate
            cur.pop()  # remove candidates[i]
            dfs(i + 1, cur, total)  # i+1, current combination, total

        dfs(0, [], 0)  # call dfs with 0 as starting index, empty array, 0 as current total
        return res
