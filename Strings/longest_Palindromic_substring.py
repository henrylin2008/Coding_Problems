# Link: https://www.algoexpert.io/questions/Longest%20Palindromic%20Substring
# Longest Palindromic Substring
# Difficulty: Medium
#
# Write a function that, given a string, returns its longest palindromic substring.
# A palindrome is defined as a string that's written the same forward and backward. Note that single-character strings
# are palindromes.
# You can assume that there will only be one longest palindromic substring.

# Sample Input:
string = "abaxyzzyxf"

# Sample Output:
# "xyzzyx"


# Time: O(n^2); Iterate through the array is O(n); 2 expansions each iteration: one expansion is center at the given
# letter; another expansion is center between given letter and previous letter; Both expansion takes at most O(n) time
# Space: O(n); we have to slice and store the final substring
# Solution: treat each character as a potential palindrome, then compare the character left and right to see if they are
# the same. Center point can be the current character, or in between of current and previous character.
def longestPalindromicSubstring(string):
    currentLongest = [0, 1]  # current longest palindrome indexes
    for i in range(1, len(string)):  # loop through the string; Index starts at 1, b/c nothing on the left of 1st index
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)  # odd length, expansion center at the current index
        # i-1: left index; i+1: right index
        even = getLongestPalindromeFrom(string, i - 1, i)  # even length, center in between current and previous index
        # compare odd and even to find out which one has the longest; key metric is the length (x[1] - x[0])
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        # get the current longest by comparing longest and currentLongest
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]  # return the longest string, second idx is exclusive


def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):  # if we are still within the range of the string
        if string[leftIdx] != string[rightIdx]:     # if letter in leftIdx and rightIdx are not the same
            break                       # exit the loop
        leftIdx -= 1                    # move left
        rightIdx += 1                   # move right
    return [leftIdx + 1, rightIdx]  # leftIdx+1: after while loop, current left idx is one too far from leftIdx; idx=-1
    # rightIdx: not rightIdx-1, b/c currentLongest has 1 on index 1
    # if rightIdx + 1, then return string[currentLongest[0]:currentLongest[1]+1] (main function)

# longestPalindromicSubstring(string)
