# 67. Add Binary
# link: https://leetcode.com/problems/add-binary/
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary(a, b):
    # adding numbers of both of (a and b) from the right to left, add carryover numbers
    result, carry, val = '', 0, 0
    # result = (string) output;
    # carry = carryover value; if 1 + 1 ==> 1 0
    # val: (current) result of addition of 2 values in current index
    print(a,b)
    for i in range(max(len(a), len(b))): # use the longest length as the range, so it goes over each character
        val = carry # check if there's carry(over) from last loop; if so, add it into the value
        if i < len(a):
            val += int(a[-(i+1)]) # int(): convert given string to int
            # a[-(i+1)]: move index from right to left; adding bits from right to the left
        if i < len(b):
            val += int(b[-(i+1)]) # moving index from right to the left
        # (current) value = sum of (current index) carry, a, and b
        carry, val = val//2, val%2
        # carry: when val is greater than 2, there's a carryover; otherwise (if val < 2), then no carry
        # val: % (mod) 2, reminder (after carryover)
        result += str(val) # append val (as string) into result at the end
    if carry: # if there's carryover value haven't been counted yet; For ex 2: it inserted 5th (index 1) into the result
        result += str(1) # add one (at the end) of the result
    return result[::-1] # reverse order

# addBinary("1010", "1111")

