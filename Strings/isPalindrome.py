# https://www.algoexpert.io/questions/Palindrome%20Check
# Palindrome Check
# Write a function that takes in a non-empty string and that returns a boolean representing whether or not the string is
# a palindrome. A palindrome is defined as a string that is written the same forward and backward.
# Sample input: "abcdcba"
# Sample output: True (it is a palindrome)
#
# Optimal Space & Time Complexity
# O(n) time | O(1) space - where n is the length of the input string

# Method 1: string
# Time: O(n^2): b/c new += string[i], re-creating new string and iterate characters in new and adding them to new string
#       and adding them to the string
# Space: O(n), n is input strings
# idea: create an empty reverse string, add each char to string and compare it with string
def isPalindrome(string):
    reverseString = ""
    for i in reversed(range(len(string))):
        reverseString += string[i]
    return string == reverseString

# Method 2: Array
# Time: O(n)
# Space: O(n)
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])  # appending to char is constant time operation
    return string == "".join(reversedChars)


# Method 3: recursion
# Time: O(n): iterate only half of string: O(n/2) = O(n)
# Space: O(n): using call stack, abcdcba --> bcdcb --> cdc --> d: O(n/2) = O(n)
# is first letter == last letter the same? or is the letters/strings in between/middle Palindrome?
def isPalindrome(string, i=0):
    j = len(string) - 1 - i # first letter compares to last letter, and so on
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)
    # if i >= j: # Get to middle of strings
    #   return True
    # else string[i] != string[j]:
    #   return False
    # return isPalindrome(string, i+1):
    #

# Method 4: iterative (best time complexity)
# Time: O(n)
# Space: O(1)
# using pointers, compare first letter and last later, then increase the left pointer and decrease the right pointer
def isPalindrome(string):
    leftIndex = 0
    rightIndex = len(string) - 1
    while leftIndex < rightIndex: # before hitting middle value 
        if string[leftIndex] != string[rightIndex]: # if string at leftIdx != string at rightIdx
            return False
        leftIndex += 1
        rightIndex -= 1
    return True
