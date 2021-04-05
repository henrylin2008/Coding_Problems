# link: https://www.algoexpert.io/questions/Longest%20Substring%20Without%20Duplication
# Longest Substring without Duplication
# Difficulty: hard
# Write a function that takes in a string and returns its longest substring without duplicate characters.
# You can assume that there will only be one longest substring without duplication.

# Sample Input:
string = "clementisacap"

# Sample Output:
# "mentisac"


# Time: O(n); n is length of the input string; iterate through the string, at any point, we only update start index,
# character and its index in lastSeen hashmap, and compare the length of 2 strings, these operations are constant
# Space: O(min(n, a)), n: length of the string; a: set of unique letters from given string
def longestSubstringWithoutDuplication(string):
    lastSeen = {}   # hash map that keeps track of letter and its index that have seem so far
    longest = [0, 1]  # longest substring: [starting index, ending index]
    startIdx = 0    # start index at the beginning
    for i, char in enumerate(string):   # keep track of the index and the character at current index
        if char in lastSeen:  # update startIdx if character is in lastSeen hashmap
            # max(startIdx, lastSeen[char] + 1): startIdx: initial start index;
            # lastSeen[char] + 1: index right after the first occurrence of the duplicate letter
            # ex: e at 2, e at 4, lastSeen[char] + 1 = 2 + 1 = 3; max(0, 3) => 3 (new starting index)
            startIdx = max(startIdx, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - startIdx:  # compare the length of current longest substring and new one
            # i + 1 - startIdx: potential new longest substring length
            # i + 1 b/c longest is set [0, 1], which is the index after i, i+1 is equivalent to longest[1]
            # startIdx equivalent to longest[0]
            longest = [startIdx, i + 1]     # update longest substring if new length is greater than existing longest
        lastSeen[char] = i  # update/add index of the character
    return string[longest[0]: longest[1]]   # longest[1] is excluded


longestSubstringWithoutDuplication(string)
