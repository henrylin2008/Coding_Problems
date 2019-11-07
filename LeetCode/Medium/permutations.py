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

    if len(nums) <= 1: # base case: return nums itself if the length <= 1
        return [nums]

    answer = []
    for i, num in enumerate(nums):
        n = nums[:i] + nums[i+1:] # leftover nums (in array) after picked num in i; ex: [1,2,3]: index(0), n = [2,3]
        for y in permute(n):  # recursive call, for loop for reminder nums
            answer.append([num] + y)  # combine result of reminder nums and result of first for loop 

    return answer