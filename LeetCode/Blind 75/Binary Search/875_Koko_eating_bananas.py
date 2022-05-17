# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Medium

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone
# and will come back in h hours.
#
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
# bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more
# bananas during this hour.
#
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
#
# Return the minimum integer k such that she can eat all the bananas within h hours.
#
#
#
# Example 1:
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#
# Example 2:
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#
# Example 3:
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#
#
# Constraints:
#
# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
import math


class Solution:
    # Time: O(log(max(p))*p); p: piles; log(max(p)): binary search
    # Space: O(1)
    # Solution: binary search, each loop, find mid-point (k), can we eat banana with k and less than current h
    #           -Ex: [3,6,7,11], H=8; k=(1+11)//2=6; l,r=1,11; hrs=[3/6,6/6,7/6,11/6]=1+1+2+2=6(<8); res: 6
    #            next loop: k=3; l,r=1,5; hrs=[3/3,6/3,7/3,11/3]=1+2+3+4=10(>8); took too long, search right portion
    #            next loop: k=4, l,r=4,5; hrs=[3/4,6/4,7/4,11/4]=1+2+2+3=8; res: 4 (4<6, update res)
    #           -if hrs (6) <= h (8); shift right pointer to (m-1); 6 is valid, is it minimum? keep trying left portion,
    #            update result if a minimum value is found, and shift right pointer (k - 1)
    #           -if hrs > h, k is too small, not enough time to eat all bananas, search right portion (increase k)
    def minEatingSpeed(self, piles, h: int) -> int:
        l, r = 1, max(piles)  # left, right pointer
        res = r  # r: at least max(piles) would work, and we are looking for the minimum, thus can't use 0 initially

        while l <= r:
            k = (l + r) // 2  # mid point
            hours = 0  # how many hours to eat all the bananas
            for p in piles:  # for every pile
                hours += math.ceil(p / k)  # total hours; p/k: how many hours take to eat bananas in a pile; round up

            if hours <= h:  # if hours < given input h
                res = min(res, k)  # get the min of res and k (mid-pointer)
                r = k - 1  # search left portion
            else:
                l = k + 1  # search right portion

        return res  # return min in the res
