# link: https://www.algoexpert.io/questions/Group%20Anagrams
# Difficulty: Medium
# Group Anagrams
# Write a function that takes in an array of strings and groups anagrams together. Anagrams are strings made up of
# exactly the same letters, where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly,
# "foo" and "ofo" are anagrams.
# Your function should return a list fo anagram groups in no particular order.

# Sample Input:
words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

# Sample Output:
# [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]


# Solution #1
# Time: O(w * n * log(n)); w: number of words; n*log(n): best sorting time
# Space: O(wn); w: # of words; n: length of longest word
# solution: create a hash table to store anagrams, loop through the words, sorted each word, if sortedWord not in
# anagrams hash table, create a new anagram group and stores it; otherwise, append sortedWord into same anagrams group;
# then return a list of grouped anagram values
def groupAnagrams(words):
    anagrams = {}   # hash table
    for word in words:  # for every word
        sortedWord = "".join(sorted(word))  # sorted each word
        if sortedWord in anagrams:  # if sortedWord in anagrams hash table
            anagrams[sortedWord].append(word)   # add sortedWord into same anagram group
        else:
            anagrams[sortedWord] = [word]   # if first time encounters the word, then create new anagrams group
    return list(anagrams.values())  # return list of anagrams groups


# Solution #2
# Time: O(w * n * log(n) + n * w * log(w)); best sorting time: nlog(n); wnlog(n): w(ord) * n * log(n)
# Space: O(wn); wn + w = w*(n + 1) ==> wn
# w: # of word/strings; n: length of longest word
# solution: 2 loops; first loop sorts each string with alphabetic order; second loop sorts the index of same
# word in alphabetic order; then sort original string in alphabetic order and compare to sorted word, if they are the
# same, append to currentAnagramGroup, else append it to the result.
#  index: [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6,  7 ]
# loop 1: [oy, act, flop, act, foo, act, oy, flop]
#  index: [ 1 ,  3 ,  5 ,  2 ,  7  ,  4 ,  0 ,  6]
# loop 2: [act, act, act, flop, flop, foo, oy, oy]
# def groupAnagrams(words):
#     if len(words) == 0:     # edge case; return [] if given words is empty
#         return []
#
#     sortedWords = ["".join(sorted(w)) for w in words]   # sort each string in alphabetic order
#     # sortedWords: ['oy', 'act', 'flop', 'act', 'foo', 'act', 'oy', 'flop']
#     indices = [i for i in range(len(words))]    # indices represent total index in given words
#     indices.sort(key=lambda x: sortedWords[x])  # compare and sort strings that have same value in alphabetic order
#     # indices: [ 1 ,  3 ,  5 ,  2 ,  7  ,  4 ,  0 ,  6] (sample data)
#     #    word: [act, act, act, flop, flop, foo, oy, oy]
#     result = []   # result array, append all grouped anagrams in this array
#     currentAnagramGroup = []    # current anagram group
#     currentAnagram = sortedWords[indices[0]]   # current Anagram starting index
#     for index in indices:   # for each index
#         word = words[index]  # original word at current index
#         sortedWord = sortedWords[index]   # sorted word at the current index
#
#         if sortedWord == currentAnagram:        # if sorted word is same as current anagram group
#             currentAnagramGroup.append(word)    # append sorted word into the group
#             continue                            # exit the loop
#
#         result.append(currentAnagramGroup)   # add current anagram group into the result
#         currentAnagramGroup = [word]    # create a new (anagram) group from the word after last group
#         currentAnagram = sortedWord     # set the new anagram
#
#     result.append(currentAnagramGroup)
#
#     return result


groupAnagrams(words)
