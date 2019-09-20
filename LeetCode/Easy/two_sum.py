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
        # Solution #1: runtime 1132ms (too long)
        # for i in nums:
        #     # reminder (j) = target - i
        #     j = target - i
        #     # starting index
        #     start_index = nums.index(i)
        #     # next index
        #     next_index = start_index + 1
        #     # new subarray after start_index; [7, 11, 15]
        #     subArray = nums[next_index: ]
        #     # if reminder (j) in new subArray
        #     if j in subArray:
        #     # return(index of i, index of j)
        #         return(nums.index(i), next_index + temp_nums.index(j))


        # Solution #2: two hash tables
        dict = {}

        for i in range(len(nums)):
            # If the reminder/sum is not in the dictionary, store the index of i in the dictionary
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            # Otherwise, return the index/position of i and the reminder in the dictionary
            else:
                return [dict[target-nums[i]], i]