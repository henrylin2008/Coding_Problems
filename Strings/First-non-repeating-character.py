# link: https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
# First Non-Repeating Character
# Difficulty: Easy
# Write a function that takes in a string of lowercase English-alphabet letter and returns the index of the string's
# first non-repeating character.
# The first non-repeating character is the first character in a string that occurs only once.

# Sample Input:
string = "abcdcaf"

# Sample Output:
# The first non-repeating character is "b" and is found at index 1


# Brute-force solution:
# time: O(n^2); 2 loops; each loop takes O(n) time, thus O(n) x O(n) -> O(n^2)
# space: O(1); not using any additional space
# Logic: nested traversal (2 loops), outer loop goes through each index/character, set a boolean variable; the inner
# loop to identify non duplicate character appeared, and return the index of first non-repeating character.
def firstNonRepeatingCharacter(string):
    for idx1 in range(len(string)):
        foundDuplicate = False
        for idx2 in range(len(string)):
            if string[idx1] == string[idx2] and idx1 != idx2:  # if same string found at a different index
                foundDuplicate = True

        if not foundDuplicate:  # if non duplicate string is found, return the index from outer loop
            return idx1
    return -1


firstNonRepeatingCharacter(string)