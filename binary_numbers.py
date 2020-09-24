# link: https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.
#
# Input Format
#
# A single integer, .
#
# Constraints
#
# Output Format
#
# Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .
#
# Sample Input 1
#
# 5
# Sample Output 1
#
# 1
# Sample Input 2
#
# 13
# Sample Output 2
#
# 2
# Explanation
#
# Sample Case 1:
# The binary representation of  is , so the maximum number of consecutive 's is .
#
# Sample Case 2:
# The binary representation of  is , so the maximum number of consecutive 's is .


import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # covert input as an integer

    current_consecutive_ls = 0
    max_consecutive_ls = 0
    while n > 0:
        remainder = n % 2 # remainder = the power of the last digit
        if remainder == 1:  # when there's remainder == 1
            current_consecutive_ls += 1 # add 1 to current consecutive list
            if current_consecutive_ls > max_consecutive_ls: # if current consecutive list > max consecutive list
                max_consecutive_ls = current_consecutive_ls # set the current consecutive list as the max consecutive list
        else:
            current_consecutive_ls = 0 # reset current consecutive list
        n = n // 2  # result of floor division = the start point of next loop
    print(max_consecutive_ls)