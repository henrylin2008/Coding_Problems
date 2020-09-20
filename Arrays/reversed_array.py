# Link: https://www.hackerrank.com/challenges/30-arrays/problem?h_r=next-challenge&h_v=zen
# Objective
# Today, we're learning about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
#
# Input Format
#
# The first line contains an integer,  (the size of our array).
# The second line contains  space-separated integers describing array 's elements.
#
# Constraints
#
# , where  is the  integer in the array.
# Output Format
#
# Print the elements of array  in reverse order as a single line of space-separated numbers.
#
# Sample Input
#
# 4
# 1 4 3 2
# Sample Output
#
# 2 3 4 1

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    reversed_arr = []
    for i in range(n):
        reversed_arr.append(arr[n - i - 1])

    print(' '.join(str(i) for i in reversed_arr))