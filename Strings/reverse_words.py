# link: https://www.algoexpert.io/questions/Reverse%20Words%20In%20String
# Reverse Words in string
# Difficulty: Medium
# Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has
# these words in reverse order. For example, given the string "tim is great", your function should return "great is tim"
# For this problem, a word can contain special characters, punctuation, and numbers. The words in the string will be
# separated by one or more whitespaces, and the reversed string must contain the same whitespaces as the original
# string. For example, given the string "whitespaces    4" you would be expected to return "4    whitespaces".
# Note that you're not allowed to use any built-in split or reverse methods/functions. However, you are allowed to use
# a built-in join method/function.
# Also note that the input string isn't guaranteed to always contain words.

# Sample Input:
string = "AlgoExpert is the best!"

# Sample Output:
# "best! the is AlgoExpert"


# Solution 1:
# Time: O(n); loop through words in the given string is O(n); loop through words/result list is also takes O(n) time
# Space: O(n); n: length of the string; keep track of length of words list, at most of length of given string
# Solution: find each word in the given string, including an empty string, then append each word into the words list;
# use a helper function to reverse each word by swapping first and last item in the list, then continue going inward
# def reverseWords(string):
#     words = []  # list to store all words from string, including ' '
#     startOfWord = 0  # start of a word
#     for idx in range(len(string)):
#         character = string[idx]     # character at current index
#
#         if character == " ":    # if current character is an empty string " ", which mean a word is found
#             words.append(string[startOfWord:idx])   # add characters up to this point as a word into the words list
#             startOfWord = idx   # reset starting index
#         elif string[startOfWord] == " ":    # if start of word is an empty string (" "), including starting string
#             words.append(" ")   # add an empty string to the words list
#             startOfWord = idx   # reset starting index
#
#     words.append(string[startOfWord:])  # add last word into the words list, b/c no space after last word (for loop)
#
#     reverseList(words)   # reverse the words in the words list
#     return "".join(words)   # join all the words together
#
#
# # function to reverse the words in a list
# def reverseList(list):
#     start, end = 0, len(list) - 1
#     while start < end:
#         list[start], list[end] = list[end], list[start]
#         start += 1
#         end -= 1


# Solution #2
# Time: O(n); loop through all characters in the given string
# Space: O(n); requires same length/space of given string to store reverse string
# Logic: reverse all characters in the string, then loop through it; Set 2 variables, startOfWord (tracks start of the
# word) and endOfWord (tracks end of the word), place startOfWord pointer at the beginning of each word, then moving the
# endOfWord pointer, as long as it is still within the range and the character is not a " ", move endOfWord pointer to
# the next position; otherwise reverse the characters within current word with a helper function; place startOfWord at
# the position after endOfWord; repeat the process until it reaches the end of the string. Then join all characters
# with .join function.
def reverseWordsInString(string):
    characters = [char for char in string]  # all characters in string, and use list to manipulate the characters
    reverseListRange(characters, 0, len(characters) - 1)  # reverse all characters in the string

    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord  # end of word pointer
        # while end of word is within characters and endOfWord is not an empty string
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1  # move to next character

        # reverse characters at current word; endOfWord-1, b/c endOfWord is currently at an emtpy string (" "),
        # so -1 moves a position back to be at end of the last word
        reverseListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1  # place startOfWord right after endOfWord, as beginning of a new word

    return "".join(characters)  # join all characters together


# function to reverse a list
def reverseListRange(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


reverseWordsInString(string)
