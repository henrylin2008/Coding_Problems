# 7. Reverse Integer
# Easy
# https://leetcode.com/problems/reverse-integer/
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
# [-2^31, (2^31)-1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
# class Solution(object):
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    # -214783648 ~ 214783647
    num = 0
    a = abs(x)

    while(a != 0):
        temp = a % 10
        # print("begin a: ", a)
        # print("temp: ", temp)
        num = num * 10 + temp
        # print("num: ", num)
        a = int(a/10)
        # print("end a: ", a)
        # print("")

    if x > 0 and x < 214783647:
        return num
    elif x < 0 and x <= 214783647:
        return -num
    else:
        return False


# reverse(53, -543)