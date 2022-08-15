# Longest Substring without Repeating Characters
# https://algo.monster/problems/longest_substring_without_repeating_characters

# Find the length of the longest substring of a given string without repeating characters.
#
# Input: abccabcabcc
# Output: 3
#
# Explanation: longest substrings are abc, cab, both of length 3
#
# Input: aaaabaaa
# Output: 2
#
# Explanation: ab is the longest substring, length 2

# Explanation
# Intuition

# The brute force way is to check every single substring and count the ones with non-repeating characters. A
# substring is defined by a start index and an end index.


def longest_substring_without_repeating_characters(s: str) -> int:
    n = len(s)
    longest = 0
    for start in range(n):
        for end in range(n):
            sub = s[start: end + 1]
            if len(set(sub)) == len(sub):
                longest = max(longest, end + 1 - start)
    return longest


if __name__ == '__main__':
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)
