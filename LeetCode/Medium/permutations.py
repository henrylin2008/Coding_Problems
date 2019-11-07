# 46. Permutations
#
# https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

def permute(nums):

    if len(nums) <= 1: # return nums itself if the length = 1 or 0
        return [nums]

    answer = []
    for i, num in enumerate(nums):
        n = nums[:i] + nums[i+1:]
        for y in permute(n):
            answer.append([num] + y)

    return answer