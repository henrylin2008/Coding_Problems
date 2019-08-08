'''
1. Two Sum
Easy

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution:
    def twoSum(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Solution #1
        # for i in nums:
        #     j = target - i
        #     start_index = nums.index()
        #     next_index = start_index + 1
        #     temp_nums = nums[next_index: ]
        #     if j in temp_nums:
        #         return(nums.index(i), next_index + temp_nums.index(j))

        # Solution #2
        dict = {}

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target-nums[i]], i]