# link: https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
# Caesar Cipher Encryptor
#
# Given a non-empty string of lowercase letters and a non-negative integer value representing a key, write a function that
# returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is
# the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z" shifted by 1 returns the
# letter "a".

# Sample input: "xyz", 2
# Sample output: "zab"

# Method 1:
# Time: O(n)
# Space: O(n)
def caesarCipherEncryptor(string, key):
    newLetters = [] # array for new letters
    newKey = key % 26
    for letter in string: # for every letter, apply helper function that shifts letters and calculate the letter code
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters) # join array to a string

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key # orc(): get the unicode value of letter
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)
        # chr() returns a character (a string) from an integer (represents unicode code point of the character).
        # unicode for lower letters from a to z: 97 - 122


# Method 2:
# Time: O(n)
# Space: O(n)
def caesarCipherEncryptor(string, key):
    newLetters = [] # new array to store letters
    newKey = key % 26 # 26 letters in alphabet
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet)) # append every letter to the string
    return "".join(newLetters) # combine all the letters

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key # getting the index of letter's new location
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[-1 + newLetterCode % 25]
    # newLetterCode <= 25 if that's within index of alphabet or before the wrapper; other calculate its new index