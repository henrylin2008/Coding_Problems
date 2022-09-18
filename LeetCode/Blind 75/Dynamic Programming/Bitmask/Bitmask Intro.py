# Bitmask and Dynamic Programming
# https://algo.monster/problems/bitmask_intro

# What is a bitmask?
# Binary Numbers
# At the smallest scale in computers, data are stored as bits. A bit stores either 0 or 1. A binary number is a
# number expressed in the base-2 system. Each digit can be either 0 or 1. The integer types we use in programming
# languages are actually stored as binary numbers. Here is how binary numbers converts to decimal numbers:
# You can check that in python:
# >>> bin(21)
# '0b10101'
# Note that 0b means it's a binary number. The leading 0s are omitted and that's why we have 10101 instead of 010101.

# Bit-wise AND
# We can AND two binary numbers by comparing each digits. If they are both 1 then the resulting digit is 1,
# otherwise it's 0.

# Bitmask
# Now finally, what's a mask? We can construct a binary number such that certain digit is set to 1 and other digits
# are all set to 0. This creates a "mask" that when we AND it to another binary it "turns off" (set to 0) all digits
# except the 1 digit in the mask.
