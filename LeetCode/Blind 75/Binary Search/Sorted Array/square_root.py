# Square Root
# https://algo.monster/problems/sqrt

# Given an integer, find its square root without using the built-in square root function. Only return the integer
# part (truncate the decimals).
#
# Input: 16
# Output: 4
#
# Input: 8
# Output: 2
#
# Explanation: square root of 8 is 2.83..., return integer part 2

# The problem is equivalent to finding the boundary of elements < n and elements >= n. Now the problem is reduced to
# finding the last true element in a boolean array. And we already know how to do this from Find the Boundary module.
#
# Time Complexity: O(log(n))
def square_root(n: int) -> int:
    if n == 0:
        return 0
    left, right = 1, n
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)


# Test case #1
# Input
# 4
# Output
# 2

# Test case #2
# Input
# 8
# Output
# 2

# Test case #3
# Input
# 10
# Output
# 3
