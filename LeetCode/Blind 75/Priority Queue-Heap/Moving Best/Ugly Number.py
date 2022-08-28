# Ugly Number
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
# Input:n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:
#   1. 1 is typically treated as an ugly number.
#   2. n does not exceed 1690.

# Solution
# Brute Force
# A brute force method would generate ugly numbers and store all possibilities for look up. We can generate them out
# of order and then sort them later.
#
# In theory this is impossible, but since there are limits on the size of datatypes, we only need to loop up to those
# limits:
