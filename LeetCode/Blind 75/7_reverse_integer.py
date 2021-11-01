# Link: https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Category: Medium
#
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Example 4:
# Input: x = 0
# Output: 0
#
# Constraints:
#
# -2^31 <= x <= 2^31 - 1

# Solution: % to get last digit, // to get digits before last digit
# ex: 123
# last digit: 123 % 10 = 3; reminder digits: 123//10 = 12
# last digit: 12 % 10 = 2; reminder digit: 12//10 = 1
# 3 * 10 = 30 + 2 = 32 + 1 (last reminder digit) = 321
# Constrains: -2^31 = -2147483648; 2^32 - 1 = 2147483647
import math


class Solution:
    def reverse(self, x: int) -> int:
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8 )

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  # 2^31 - 1

        res = 0
        while x:  # when x is not 0
            digit = int(math.fmod(x, 10))  # last digit; using math.fmod b/c of -1 %  10 = 9;
            x = int(x / 10)  # digits before last digit; (python dumb) -1 // 10 = -1

            if (res > MAX // 10 or  # if last digit > last digit of current max value, it's going to be overflow
                    (res == MAX // 10 and digit >= MAX % 10)):
                # if everything matched before last digit, and last digit > last digit of MAX
                return 0
            if (res < MIN // 10 or
                    (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return res
