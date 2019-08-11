# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Share
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    num = 0
    a = abs(x)

    while (a != 0):
        temp = a % 10
        num = num * 10 + temp
        a = a //10

    if x >= 0 and x == num:
        return True
    else:
        return False

isPalindrome(5, 131)