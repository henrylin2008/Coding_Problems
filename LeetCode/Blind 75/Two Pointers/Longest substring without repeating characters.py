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


# To improve on brute force, we have to skip unnecessary operations. For a substring starting with start that already
# contains one duplicate character, we want to stop checking more substrings with the start index. When this happens
# we want to increment start and look at the next set of substrings.
#
# This makes it a classic sliding window problem. A sliding window is defined by two pointers moving in the same
# direction. We move the window (incrementing pointers) whilst maintaining a certain invariant. For this particular
# problem, the invariant is the characters inside the window being unique. We use a set to record what's in the
# window. And when we encounter a character that's already in the window, we want to move the left pointer until it
# goes past the last occurrence of that character.
#
# Time Complexity: O(n)

def longest_substring_without_repeating_characters(s: str) -> int:
    n = len(s)
    longest = 0
    l = r = 0
    window = set()
    while r < n:
        if s[r] not in window:
            window.add(s[r])
            r += 1
        else:
            window.remove(s[l])
            l += 1
        longest = max(longest, r - l)
    return longest


if __name__ == '__main__':
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)