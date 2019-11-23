# 66. Plus One
# https://leetcode.com/problems/plus-one/
#
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plusOne(digits):
    # Corner case: when adding 1 to a 9, change the value of 9 to 0; then increase 1 on next loop
    # change digits[0] to 1 and append o to the end of digits
    for i in reversed(range(len(digits))):
        if digits[i] == 9: # if the value of an index is 9, change its value 0
            digits[i] = 0
        else:  # otherwise increase 1 to the index during next iteration
            digits[i] += 1
            return digits
    digits[0] = 1  # update the value of first index to 1
    digits.append(0) # then append 0 to the end of digits

    return digits