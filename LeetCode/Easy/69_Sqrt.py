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
    print(x)
    if x < 2: # anything less than 2, return its own value
        return x

    left, right = 1, x//2 # right = (for sure) less than middle value of x
    # while loop: move left pointer to the right, and right pointer to the left, until both pointers meet
    while left <= right:
        print("left, right:", left, right)
        mid = left + (right-left)//2  # locate middle value again
        print("(right-left)//2:", (right-left)//2)
        print("mid:", mid)
        print("x/mid:", x/mid)
        if mid > x/mid: # if mid > x/mid, the right (value) is too large, then mid-1
            right = mid - 1
            print('right:', right)
        else: # otherwise (if) left <= x/mid, the left value is too small, then mid+1
            left = mid + 1
            print('left:', left)
        print("")
    print("final:", left-1)
    print('')
    return left - 1

# sqrt(1)
sqrt(18)
