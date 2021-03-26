# https://www.algoexpert.io/questions/Run-Length%20Encoding
# Run-Length Encoding
# Difficulty: Easy
# Write a function that takes in a non-empty string and returns its run-length encoding.
# From Wikipedia, "run-length encoding is a form of lossless data compression in which runs of data are stored as a
# single data value and count, rather than as the original run." For this problem, a run of data is any sequence of
# consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".
# To make things more complicated, however, the input string can contain all sorts of special characters, including
# numbers. And since encoded data must be decodable, this means that we can't naively run-length-encode long runs. For
# example, the run "AAAAAAAAAAAA" (12 As), can't naively be encoded as "12A", since this string can be decoded as either
# "AAAAAAAAAAAA" or "1AA". Thus long runs (run of 10 or more characters) should be encoded in a split fashion; the
# aforementioned run should be encoded as "9A3A".

# Sample Input:
# string = "AAAAAAAAAAAAABBCCCCDD"
# Sample Output:
# "9A4A2B4C2D"


# Time: O(n)
# Space: O(n): n is the length of the input string
def runLineEncoding(string):
    encodedStringCharacters = []    # list for better time complexity, O(n) (vs time complexity of string is O(n^2))
    currentRunLength = 1    # index starts 1, so we can compare current letter and previous letter

    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]
        # when current character != previous character or when current run length is 9 (reach the limit)
        if currentCharacter != previousCharacter or currentRunLength == 9:
            # convert current run length to a string and added the (return) list
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)   # add the previous character to the list
            currentRunLength = 0   # reset current run length count

        currentRunLength += 1     # add one to the current run length if current character == previous character

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])   # last item in the given string

    return "".join(encodedStringCharacters)


# runLineEncoding(string)