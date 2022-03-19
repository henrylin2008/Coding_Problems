# 347. Top K Frequent Elements
# Link: https://leetcode.com/problems/top-k-frequent-elements/
# Difficultly: Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any
# order.
#
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# Bucket Sort:
#   -index: i(count), count/appearance of each value
#   -values: the value that associates with the count
# Ex: [1,1,1,2,2,3]; k = 2
#
# i (count): |  0  |  1  |  2  |  3  |  4  |  5  |  6  |     <-- size of given array; frequency of a value
# values:    |     | [3] | [2] | [1] |     |     |     |     <-- value that associates to the count (above ^)
#
# Top k (top 2 values):
#   - i (count): 2, 3; 3: most frequent element
#   - values:   [2, 1] --> [1, 2]

# Time: O(n); linear time; O(n) for input array, O(n) for values row, O(n) + O(n) -> O(n)
# Space: O(n); hashmap to count the input array
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}          # hashmap for count of occurrence of each value
        freq = [[] for i in range(len(nums) + 1)]  # array for values associate with the count, same size of input array
        for n in nums:      # counting the occurrence of each value
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():      # associate number and count in count hashmap
            freq[c].append(n)           # n(number) occurs c(count) times
        res = []
        for i in range(len(freq) - 1, 0, -1):  # descending order (most frequent elements)
            for n in freq[i]:                  # go through n value in the freq array
                res.append(n)                  # if n is not empty, append n (times) to the res
                if len(res) == k:              # when length of res == k: return res
                    return res
