# 69. Sqrt(x)
# link: https://leetcode.com/problems/sqrtx/
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
#
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

def sqrt(x):
    if x < 2: # anything less than 2, return its own value
        return x

    left, right = 1, x//2 # right = (for sure) from 1 to middle (whole number) of x
    # while loop: move left pointer to the right, and right pointer to the left, until both pointers meet
    while left <= right: # while left value <= right value, find new left/right value
        mid = left + (right-left)//2  # locate middle value again in between left and right
        if mid > x/mid: # relationship: mid^2 <= x
            # if mid > x/mid, then right (value) is too large, mid-1 as the new value of right
            right = mid - 1
        else: # otherwise (if) left <= x/mid, the left value is too small, then mid+1
            left = mid + 1
    return left - 1

# sqrt(18)
