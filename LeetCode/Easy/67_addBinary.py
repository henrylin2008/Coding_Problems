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
    # adding numbers from right to left, carryover numbers are added, and
    result, carry, val = '', 0, 0
    # result = string output;
    # carry = carryover value; if 1 + 1 ==> 1 0
    # val: (current) result of addition of 2 values in current index
    print(a,b)
    for i in range(max(len(a), len(b))): # use the longest length as the range, so it goes over each character
        print("i:", i)
        val = carry # check if there's carry(over) from last loop; if so, add it (in current loop)
        if i < len(a):
            print(a[-(i+1)])
            # print("a[-(i+1)]:", a[-(i+1)])
            # print("val before:", val)
            val += int(a[-(i+1)]) # int(): convert given string to int
            # a[-(i+1)]: move index from right to left
            print("val after a:", val)
            # print("")
            # a[-(i+1)]: reverse order, indexing from right to left,
        if i < len(b):
            print(b[-(i+1)])
            # print("(b[-(i+1)]):", (b[-(i+1)]))
            val += int(b[-(i+1)])
            print("val after b:", val)
            # print("")
        print("carry, val:", carry, val)
        carry, val = val//2, val%2
        # carry: when val is greater than 2, there's a carryover; otherwise (if val < 2), then no carry
        # val: % (mod) 2, reminder after carryover
        print("carry, val after:", carry, val)
        print("result before:", result)
        result += str(val) # append val (as string) into result
        print("result after:", result)
        print("")
    if carry: # if there's carryover value haven't been counted yet; For ex 2: it requires a 5th number into the result
        print("result in carry before", result)
        result += str(1) # add one into the result
        print("result in carry after:", result)
    print(result[::-1])
    print()
    return result[::-1] # reverse order

addBinary("1010", "1111")

