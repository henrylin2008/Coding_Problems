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
    if x < 2:
        return x

    left, right = 1, x//2
    while left <= right:
        mid = left + (right-left)//2
        print("mid:", mid)
        if mid > x/mid:
            right = mid - 1
            print('right:', right)
        else:
            left = mid + 1
            print('left:', left)
    print("left -1:", left-1)
    return left - 1

sqrt(8)