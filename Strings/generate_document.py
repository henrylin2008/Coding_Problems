# https://www.algoexpert.io/questions/Generate%20Document
# Difficulty: Easy
# Generate Document
# You're given a string of available characters and a string representing a document that you need to generate. Write a
# function that determines if you can generate the document using the available characters. If you can generate the
# document, your function should return true; otherwise, it should return false.
# You're only able to generate the document if the frequency of unique characters in the characters string is greater
# than or equal to the frequency of unique characters in the document string. For example, if you're given
# characters = "abcabc" and document = "aabbccc" you cannot generate the document because you're missing one c.
# The document that you need to create many contain any characters, including special characters, capital letters,
# numbers, and spaces.
# Note: you can always generate the empty string ("").

# Sample Input:
# characters = "Bste!hetsi ogEAxpelrt x"
# document = "AlgoExpert is the Best!"

# Sample Output:
# true

# Solution 3: Least optimal
# Time: O(m * (n + m)); m: length of document; n: length of characters,
# Space: O(1); constant space
# Count the number of appearance for each character from characters and document, then compare the count result
def generateDocument(characters, document):
    for character in document:   # Time: initial m in O(m * (n+m))
        # loop through the character frequency in characters/document
        documentFrequency = countCharacterFrequency(character, document)    # m time from O(n+m)
        charactersFrequency = countCharacterFrequency(character, characters)    # n time from O(n+m)
        if documentFrequency > charactersFrequency:
            return False
    return True


def countCharacterFrequency(character, target):     # same as document.count(character), O(n)
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency
