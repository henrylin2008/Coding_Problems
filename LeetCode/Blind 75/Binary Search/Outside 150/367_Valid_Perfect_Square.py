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
    # Time: O(log(n)); use binary search
    # Space: O(1); no data structure is used
    # Solution: use a binary search to find the middle point, then compare squared of the middle point with the num;
    #           if squared of middle pointer < num: update left pointer to middle + 1, search right portion
    #           elif squared of middle pointer > num: update right pointer to middle - 1, search left portion
    #           else if squared of middle pointer == num: return True
    #           return False if no match is found
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
