# 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Medium

# A conveyor belt has packages that must be shipped from one port to another within days days.
#
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
# conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the
# ship.
#
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
# shipped within days days.
#
#
# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
#
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages
# into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
#
# Example 2:
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
#
# Example 3:
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
#
#
# Constraints:
# 1 <= days <= weights.length <= 5 * 104
# 1 <= weights[i] <= 500
from typing import List


class Solution:
    # Time:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)         # left boundary; minimum requirement to carry the max weight
        right = sum(weights)        # right boundary
        boundary = right

        while left <= right:
            mid = (left + right) // 2       # mid-point
            if self.can_ship(mid, weights, days):   # can ship the weight whatever the mid
                boundary = mid
                right = mid - 1
            else:       # if can't ship with the weight
                left = mid + 1  # shift the left pointer
        return boundary

    def can_ship(self, candidate, weights, days):
        current_weight = 0      # current_weight
        days_taken = 1          # days taken so far, at least one day

        for weight in weights:
            current_weight += weight    # add weight to the current_weight

            if current_weight > candidate:  # if current_weight exceed the weight that we are allowed to use
                days_taken += 1     # send the ship off without the last weight
                current_weight = weight     # reset the weight to the current weight
        return days_taken <= days       # return days_taken as long as it less than/equal to the given days


