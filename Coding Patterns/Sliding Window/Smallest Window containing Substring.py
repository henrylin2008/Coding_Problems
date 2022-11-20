# Smallest Window containing Substring (hard)
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628541068682_8Unit

# Problem Statement
#
# Given a string and a pattern, find the smallest substring in the given string which has all the character
# occurrences of the given pattern.
#
# Example 1:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
#
# Example 2:
# Input: String="aabdec", Pattern="abac"
# Output: "aabdec"
# Explanation: The smallest substring having all characters occurrences of the pattern is "aabdec"
#
# Example 3:
# Input: String="abdbca", Pattern="abc"
# Output: "bca"
# Explanation: The smallest substring having all characters of the pattern is "bca".
#
# Example 4:
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern

# Solution
#
# This problem follows the Sliding Window pattern and has a lot of similarities with Permutation in a String with one
# difference. In this problem, we need to find a substring having all characters of the pattern which means that the
# required substring can have some additional characters and doesn’t need to be a permutation of the pattern. Here is
# how we will manage these differences:
#   1. We will keep a running count of every matching instance of a character.
#   2. Whenever we have matched all the characters, we will try to shrink the window from the beginning, keeping track
#      of the smallest substring that has all the matching characters.
#   3. We will stop the shrinking process as soon as we remove a matched character from the sliding window. One thing to
#      note here is that we could have redundant matching characters, e.g., we might have two ‘a’ in the sliding window
#      when we only need one ‘a’. In that case, when we encounter the first ‘a’, we will simply shrink the window
#      without decrementing the matched count. We will decrement the matched count when the second ‘a’ goes out of the
#      window.

def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll
                # decrement the matched count only when a useful occurrence of a matched
                # character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()

# Time Complexity
# The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in
# the input string and the pattern respectively.
#
# Space Complexity
# The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct
# characters which will go into the HashMap. In the worst case, we also need O(N) space for the resulting
# substring, which will happen when the input string is a permutation of the pattern.
