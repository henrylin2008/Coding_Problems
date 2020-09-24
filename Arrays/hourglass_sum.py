# https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Objective
# Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!
#
# Context
# Given a 6 x 6 2D Array, A:
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
#
# a b c
#   d
# e f g
#
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
#
# Input Format
#
# There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A
# will be in the inclusive range of -9 to 9.
#
# Constraints
#  * -9 <= A[i][j] <= 9
#  * 0 <= i,j <= 5

# Output Format
#
# Print the largest (maximum) hourglass sum found in A.
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
#
# Explanation
#
# A contains the following hourglasses:
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
#
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
#
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum (19) is:
#
# 2 4 4
#   2
# 1 2 4


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    def _get_hourglass_sum(matrix, row, col): # helper method to get the maxtrix/hourglass sum
        sum = 0
        sum += matrix[row - 1][col - 1]
        sum += matrix[row - 1][col]
        sum += matrix[row - 1][col + 1]
        sum += matrix[row][col]
        sum += matrix[row + 1][col - 1]
        sum += matrix[row + 1][col]
        sum += matrix[row + 1][col + 1]
        return sum

    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split()))) # append input as the list into arr
        # arr:[[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

    max_hourglass_sum = -63 # constrains from the question -9 * 7 = -63
    for i in range(1, 5): # row: second row to 5th row
        for j in range(1, 5): # column: second column to 5th column
            current_hourglass_sum = _get_hourglass_sum(arr, i, j) # get the sum of current hourglass
            if current_hourglass_sum > max_hourglass_sum: # if current sum > max sum:
                max_hourglass_sum = current_hourglass_sum   # set new max sum = current sum

    print(max_hourglass_sum)
