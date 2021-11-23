# link: https://leetcode.com/problems/majority-element/
# Majority Element: easy
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
#
# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1
#
# Follow-up: Could you solve the problem in linear time and in O(1) space?
class Solution:
    # Idea: set 2 variables: result and count, set the first number as the initial result, then increment the count, if
    # the next is the same number, increment the count, otherwise decrement the count; when the count reaches to 0,
    # then update the result with the number that has the majority count; this would work if a valid array with a
    # majority element is in place.
    # Time: O(n)
    # Space: O(1); no additional space, because we're using a count variable to get the most frequent number
    def majorityElement(self, nums) -> int:  # nums: List[int]
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)     # increment count if n == result, otherwise count - 1
        return result

    # Solution # 2: use hashmap to get count of each value
    # Time: O(n)
    # Space: O(n); extra space needed to store count, result, max_count
    def majorityElement(self, nums) -> int:  # nums: List[int]
        count = {}
        result, max_count = 0, 0

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # update/increment count for each value, default value of 0
            result = n if count[n] > max_count else result  # update count when its value is > max_count
            max_count = max(count[n], max_count)
        return result
