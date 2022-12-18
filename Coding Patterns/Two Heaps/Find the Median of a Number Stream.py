# Find the Median of a Number Stream (medium)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743994867_62Unit

#
# Problem Statement
#
# Design a class to calculate the median of a number stream. The class should have the following two methods:
#   1. insertNum(int num): stores the number in the class
#   2. findMedian(): returns the median of all numbers inserted in the class
#
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
#
# Example 1:
#
# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
# 7. findMedian() -> output: 3.5
