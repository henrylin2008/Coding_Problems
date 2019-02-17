# Non-Repeating Character: https://www.udemy.com/11-essential-coding-interview-questions/learn/v4/t/quiz/380026
# Implement a function that takes a string and returns the first character
# that does not appear twice or more. 
# Ex: "abacc" --> 'b'
#     "xxyzx" ---> 'y' (first non-repeating character)
# If there is no non-repeating character, return None. def non_repeating(given_string):
def non_repeating(given_string):
    char_count = {} #Dictionary character count
    for c in given_string:
        if c in char_count: # If c is already in char_count, increment c by 1, c += 1; ex, c: 2
            char_count[c] += 1
        else:  # Otherwise, first occurrence = 1, 
            char_count[c] = 1
    for c in given_string: # Go through the string, if charcter appears once, then return the character
        if char_count[c] == 1:
            return c
    return None # if nothing found, return null/none

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'