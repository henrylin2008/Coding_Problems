# One Away Strings: https://www.udemy.com/11-essential-coding-interview-questions/learn/v4/t/quiz/379168
# Write a function that takes 2 strings and returns True if they are one away from each other
# There are one away from each other if a single operation (changing a character, deleting a character
# or adding a character) will change one of the strings to the other
# Ex: "abcde" and "abcd" are one away (delteing a character)
# "a" and "a" are one away (changing the only character 'a' to the equivalent character 'a').
# "abc" and "bcc" are NOT one away. (2 operations away)

# Main function 
def is_one_away(s1, s2):
    if len(s1) - len(s2) >= 2 or len(s2) - len(s1) >= 2:   # False if length difference between strings > 1
        # print("False")
        return False
    elif len(s1) == len(s2):                    # case if length are the same for both strings
        return is_one_away_same_length(s1, s2)
    elif len(s1) > len(s2):                     # case 2: len(s1) = len(s2) + 1
        return is_one_away_diff_lengths(s1, s2)
    else:                                       # case 2.2: len(s2) = len(s1) + 1
        return is_one_away_diff_lengths(s2, s1)


# Case 1: len(s1) == len(s2); s1 = "abcde"; s2="abcee"
# Compare character by character between strings; return False if more than one character different; else if 0 or 1
# character difference, return True
# Time: O(n)
def is_one_away_same_length(s1, s2):
    count_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:        # if character in same index of s1 and s2 are different
            count_diff += 1
            if count_diff > 1:    # more than 2 characters different
                # print("False")
                return False
    # print("True")
    return True


# Case 2: len(s1) == len(s2) + 1; s1="abcde"; s2="abde"
# compare character by character; if different characters, move pointer of longer string to next item, remind the
# pointer of shorter string; if more than 2 characters difference, return False
# Time: O(n)
def is_one_away_diff_lengths(s1, s2):     # len(s1) > len(s2)
    i = 0                                 # keep track of which index is examing in s2
    count_diff = 0                        # counter for number of different characters so far
    while i < len(s2):
        if s1[i + count_diff] == s2[i]:   # if character in s1[i+0|1] == s2[i]
            i += 1                        # move to next index
        else:                             # if 2 characters are not the same
            count_diff += 1               # increment counter by 1
            if count_diff > 1:            # more than one character different
                # print("False")
                return False
    # print("True")
    return True


# NOTE: The following input values will be used for testing your solution.
is_one_away("abcde", "abcd")  # should return True
is_one_away("abde", "abcde")  # should return True
is_one_away("a", "a")  # should return True
is_one_away("abcdef", "abqdef")  # should return True
is_one_away("abcdef", "abccef")  # should return True
is_one_away("abcdef", "abcde")  # should return True
is_one_away("aaa", "abc")  # should return False
is_one_away("abcde", "abc")  # should return False
is_one_away("abc", "abcde")  # should return False
is_one_away("abc", "bcc")  # should return False
