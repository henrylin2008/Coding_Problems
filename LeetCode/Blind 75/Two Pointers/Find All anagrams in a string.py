# Find All Anagrams in a String
# https://algo.monster/problems/find_all_anagrams

# Given a string original and a string check, find the starting index of all substrings of original that is an
# anagram of check. The output must be sorted in ascending order.
#
# Parameters
#   -original: A string
#   -check: A string
# Result
#   -A list of integers representing the starting indices of all anagrams of check.

# Examples
# Example 1
# Input: original = "cbaebabacd", check = "abc"
# Output: [0, 6]
# Explanation: The substring from 0 to 2, "cba", is an anagram of "abc", and so is the substring from 6 to 8, "bac".
#
# Example 2
# Input: original = "abab", check = "ab"
# Output: [0, 1, 2]
# Explanation: All substrings with length 2 from "abab" is an anagram of "ab".
#
# Constraints
#   -1 <= len(original), len(check) <= 10^5
#   -Each string consists of only lowercase characters in standard English alphabet.

# Solution
# This is a classical sliding window problem. The sliding window is maintained at the size of check, and we keep
# track of the number of each type of characters inside the window in a hashmap. Every cycle, we move the window to
# the right, pushing the rightmost character while popping the leftmost character. We check that at any given time,
# if the content of the set matches the character count of check, by definition, that substring is an anagram,
# and we can insert the index into the resulting list.
#
# Below is a graphical explanation:
#
# Time Complexity: O(n)

from typing import List


def find_all_anagrams(original: str, check: str) -> List[int]:
    original_len, check_len = len(original), len(check)
    if original_len < check_len:
        return []

    res = []
    # stores the frequency of each character in the check string
    check_counter = [0] * 26
    # stores the frequency of each character in the current window
    window = [0] * 26
    a = ord('a')  # ascii value of 'a'
    # first window
    for i in range(check_len):
        check_counter[ord(check[i]) - a] += 1
        window[ord(original[i]) - a] += 1
    if window == check_counter:
        res.append(0)

    for i in range(check_len, original_len):
        window[ord(original[i - check_len]) - a] -= 1
        window[ord(original[i]) - a] += 1
        if window == check_counter:
            res.append(i - check_len + 1)
    return res


if __name__ == '__main__':
    original = input()
    check = input()
    res = find_all_anagrams(original, check)
    print(' '.join(map(str, res)))
