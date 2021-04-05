# link: https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication
# Longest Substring without Duplication
# Difficulty: hard
# Write a function that takes in a string and returns its longest substring without duplicate characters.
# You can assume that there will only be one longest substring without duplication.

# Sample Input:
string = "clementisacap"

# Sample Output:
# "mentisac"


# Time: O(n)
# Space: O(min(n, a))
def longestSubstringWithoutDuplication(string):
    lastSeen = {}   # hash map that keeps track of letters (and its index) that have seem so far
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            # startIdx is starting index of a longest substring;
            # max(startIdx, lastSeen[char] + 1): compares current start index and new start index (index of duplicate
            # letter)
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        lastSeen[char] = i
    return string[longest[0]: longest[1]]


longestSubstringWithoutDuplication(string)
