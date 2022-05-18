# 367. Valid Perfect Square
# Link: https://leetcode.com/problems/valid-perfect-square/
# Easy

# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Follow up: Do not use any built-in library function such as sqrt.
#
#
#
# Example 1:
#
# Input: num = 16
# Output: true
# Example 2:
#
# Input: num = 14
# Output: false
#
#
# Constraints:
#
# 1 <= num <= 2^31 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            sqt = mid ** 2
            if sqt > num:
                r = mid - 1
            elif sqt < num:
                l = mid + 1
            else:
                return True
        return False
