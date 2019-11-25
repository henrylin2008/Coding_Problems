# 38. Count and Say
#
# https://leetcode.com/problems/count-and-say/
#
# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
#     1. 1
#     2. 11
#     3. 21
#     4. 1211
#     5. 111221
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
#     Input: 1
#     Output: "1"
#
# Example 2:
#
#     Input: 4
#     Output: "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        seq = "1"   # initial sequence (first line)
        for i in range(n - 1): # locate number in nth line; range from 0 (i) to n-1
            seq = self.getNext(seq) # sequence of each line
        return seq

    def getNext(self, seq):
        i, next_seq = 0, ""  # i = index; next_seq = return result
        while i < len(seq): # go through every number in sequence; i <= len(seq)-1
            count = 1 # initial count; first item in sequence, always = 1
            while i < len(seq) - 1 and seq[i] == seq[i + 1]: # while 2 consecutive numbers are the same, and < len(seq) -1
                # break when 2 consecutive numbers are different
                count += 1 # increment count by 1
                i += 1 # move to next index/number
            next_seq += str(count) + seq[i] # combine count of current number and current number into the output
            i += 1 # next number
        return next_seq # result is provided to getNext(seq) in countAndSay function

