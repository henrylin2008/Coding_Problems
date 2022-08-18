# Minimum Window Substring
# https://algo.monster/problems/minimum_window_substring

# Given two strings, original and check, return the minimum substring of original such that each character in check,
# including duplicates, are included in this substring. By "minimum", I mean the shortest substring. If two
# substrings that satisfy the condition has the same length, the one that comes lexicographically first are smaller.
#
# Parameters
#   -original: The original string.
#   -check: The string to check if a window contains it.
# Result
#   -The smallest substring of original that satisfy the condition.
#
# Examples
# Example 1
# Input: original = "cdbaebaecd", check = "abc"
# Output: baec
# Explanation: baec is the shortest substring of original that contains all of a, b, and c.
#
# Constraints
#   * 1 <= len(check), len(original) <= 10^5
#   * original and check both contains only upper case and lower case characters in English. The characters are case
#   sensitive.

# Solution
# The solution is similar to Find All Anagrams in a String, except instead of matching exactly, we are to find a
# window that contains all characters in check.
#
# In this case, the comparison for checking valid window is changed to compare that for every character in check,
# see if the window contains more of that character.
#
# In addition, the moving conditions of the window changes as well. Instead of two pointers moving at once,
# maintaining the size of the window, each pointer moves independently. When the window does not contain check,
# we move the end pointer until it does (or it reaches the end), then we move the start pointer until the window no
# longer contains check. In this case, just before moving the window was the local minimal substring. Then it's a
# simple matter of comparing local minimal substrings and find the minimum one.
#
# Time Complexity: O(n)

from typing import Counter


def get_minimum_window(original: str, check: str) -> str:
    # Counts the number of each character of "check"
    check_count = Counter[check]
    # Counts the number of each character in the sliding window
    window_count = {}
    # Count the number of entries in "check_count" that is smaller than or equal to
    # that in "window_count"
    # If "satisfy_count" is equal to the number of entries in "check_count",
    # that window contains "check". We then just need to check if its the minimum.
    satisfy_count = 0
    original_len = len(original)
    # Two pointers pointing to the window (inclusive start, exclusive end)
    start_ptr = 0
    end_ptr = 0
    # The number of entries in "check_count". Used to check if "window_count" contains
    # "check_count"
    match_req = len(check_count.keys())
    # The smallest recorded string that satisfies the conditions.
    smallest_str = None

    # Change the number of "char" inside the window by "delta"
    # Automatically increase or decrease "satisfy_count" to reflect the current value.
    def delta_char(char, delta):
        nonlocal satisfy_count
        if char not in window_count:
            window_count[char] = 0
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count -= 1
        window_count[char] += delta
        if window_count[char] >= check_count.get(char, 0):
            satisfy_count += 1

    while end_ptr < original_len:
        # Moves the end pointer until it contains "check" or it reaches the end
        while end_ptr < original_len and satisfy_count < match_req:
            delta_char(original[end_ptr], 1)
            end_ptr += 1
        # If the window reaches the end and does not contain "check", break loop
        if end_ptr == original_len and satisfy_count < match_req:
            break
        # Otherwise, the window contains "check", so we move the start pointer
        # until it no longer does. Then, the one before failing the check is the local
        # minimal substring.
        while satisfy_count >= match_req:
            delta_char(original[start_ptr], -1)
            start_ptr += 1
        valid_window = original[start_ptr - 1: end_ptr]
        # Compare the local minimum to the stored smallest string
        # If there is nothing stored, or the condition outlined is true, we store the string
        if smallest_str is None or (len(smallest_str) > len(valid_window)):
            smallest_str = valid_window
        elif len(smallest_str) == len(valid_window) and valid_window < smallest_str:
            smallest_str = valid_window
    return smallest_str or ""


if __name__ == '__main__':
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)
