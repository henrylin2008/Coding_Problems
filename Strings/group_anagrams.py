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


# Solution #2
# Time: O(w * n * log(n) + n * w* log(w)); best sorting time: nlog(n); wnlog(n): w(ord) * n * log(n)
# Space: O(wn); wn + w = w*(n + 1) ==> wn
# w: # of word/strings; n: length of longest word
# solution: 2 loops; first loop sorts words with alphabetic order; second loop sorts the index of anagram word together.
#  index: [ 0 ,  1 ,  2 ,   3 ,  4  , 5 ,  6]
# loop 1: [oy, act, flop, act, act, oy, flop]
#  index: [ 1 ,  3 ,  4 ,  2  ,  6  , 0 , 5 ]
# loop 2: [act, act, act, flop, flop, oy, oy]
def groupAnagrams(words):
    if len(words) == 0:     # edge case; return [] if given words is empty
        return []

    sortedWords = ["".join(sorted(w)) for w in words]   # sort words in alphabetic order
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])  # sorting index by comparing words; group same word together

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)    # append same word into a group
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]    # create a new group
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result


# groupAnagrams(words)