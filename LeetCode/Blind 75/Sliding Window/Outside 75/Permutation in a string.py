# Permutation in a String (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541055153_6Unit

# Problem Statement
#
# Given a string and a pattern, find out if the string contains any permutation of the pattern.
#
# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following
# six permutations:
#   1. abc
#   2. acb
#   3. bac
#   4. bca
#   5. cab
#   6. cba
#
# If a string has ‘n’ distinct characters, it will have n!n! permutations.
#
# Example 1:
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
#
# Example 2:
# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
#
# Example 3:
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
#
# Example 4:
# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.


# Solution
# This problem follows the Sliding Window pattern, and we can use a similar sliding window strategy as discussed in
# Longest Substring with K Distinct Characters. We can use a HashMap to remember the frequencies of all characters in
# the given pattern. Our goal will be to match all the characters from this HashMap with a sliding window in the
# given string. Here are the steps of our algorithm:
#   1. Create a HashMap to calculate the frequencies of all characters in the pattern.
#   2. Iterate through the string, adding one character at a time in the sliding window.
#   3. If the character being added matches a character in the HashMap, decrement its frequency in the map. If the
#      character frequency becomes zero, we got a complete match.
#   4. If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (
#      i.e., total characters in the HashMap), we have gotten our required permutation.
#   5. If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s
#      size. At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.

def find_permutation(str1, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # our goal is to match all the characters from the 'char_frequency' with the current
    # window try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True

        # shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()