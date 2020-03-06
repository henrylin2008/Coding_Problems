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
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# Method 2:
# Time: O(n)
# Space: O(n)
def ca