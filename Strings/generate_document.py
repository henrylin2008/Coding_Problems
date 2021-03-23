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


# solution 1: optimal
# Time: O(n + m);   n: length of characters; m: length of document
# Space: O(c);  c: unique character
# Loop through the characters in characters and add each character to the hash map; then loop through document, and
# remove 1 of the character count from the hash map
def generateDocument(characters, document):
    characterCounts = {}    # hash map

    for character in characters:
        if character not in characterCounts:    # if character not in the hash map
            characterCounts[character] = 0      # add the character to the hash map
        characterCounts[character] += 1         # count the character

    for character in document:
        # if character not in the hash map or character count == 0, return False
        if character not in characterCounts or characterCounts[character] == 0:
            return False
        characterCounts[character] -= 1     # subtract 1 from the hash map

    return True


# Solution 2
# Time: O(c * (n + m))  # c: unique character in document,
# Space: O(c)
# Similar to solution # 3, but only add character once in the alreadyCounted set
# def generateDocument(characters, document):
#     alreadyCounted = set()      # create a set to add new character
#
#     for character in document:   # Time: initial m in O(m * (n+m))
#         if character in alreadyCounted:     # skip the character if it's already counted
#             continue
#
#         documentFrequency = countCharacterFrequency(character, document)    # m time from O(n+m)
#         charactersFrequency = countCharacterFrequency(character, characters)    # n time from O(n+m)
#         if documentFrequency > charactersFrequency:
#             return False
#
#         alreadyCounted.add(character)       # add new character to the set
#     return True
#
#
# def countCharacterFrequency(character, target):     # same as document.count(character), O(n)
#     frequency = 0
#     for char in target:
#         if char == character:
#             frequency += 1
#     return frequency


# Solution 3: Least optimal
# Time: O(m * (n + m)); m: length of document; n: length of characters,
# Space: O(1); constant space
# Count the number of appearance for each character from characters and document, then compare the count result
# def generateDocument(characters, document):
#     for character in document:   # Time: initial m in O(m * (n+m))
#         # loop through the character frequency in characters/document
#         documentFrequency = countCharacterFrequency(character, document)    # m time from (n+m)
#         charactersFrequency = countCharacterFrequency(character, characters)    # n time from (n+m)
#         if documentFrequency > charactersFrequency:
#             return False
#     return True
#
#
# def countCharacterFrequency(character, target):     # same as document.count(character), O(n)
#     frequency = 0
#     for char in target:
#         if char == character:
#             frequency += 1
#     return frequency
