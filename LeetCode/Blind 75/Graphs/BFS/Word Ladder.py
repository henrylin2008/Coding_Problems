# Word Ladder
# https://algo.monster/problems/word_ladder

# Word Ladder is "a puzzle begins with two words, and to solve the puzzle one must find a chain of other words to
# link the two, in which two adjacent words (that is, words in successive steps) differ by one letter."
#
# For example: COLD → CORD → CARD → WARD → WARM

# Given a start word, an end word, and a list of dictionary words, determine the minimum number of steps to go from
# the start word to the end word using only words from the dictionary.
#
# Input:
# start = "COLD"
# end = "WARM"
# word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
#
# Output:
# 4
# Explanation: We can go from COLD to WARM by going through COLD → CORD → CARD → WARD → WARM

# Intuition

# We start from a word. In each step we can only go from one word in the list to another, and we want to end up on
# some word. This suggests that we can represent each word with a node in a graph. In order to do this simply replace
# every character in the string with a new character and see if we have generated this word before. We can use a set
# to keep track of which words we have already made as nodes. Each step that transforms a word to another then
# becomes an edge between the corresponding nodes:
#
#
#
# Now the problem becomes "find the minimum distance from one node in a graph to the other", which is a problem that
# BFS handles very easily.
#
# Conceptually, we now have an algorithm that is a 2-step process:
#
# build a graph that represents the words and transformations
# use BFS on the graph to find the minimum distance
#
# In the actual algorithm, however, we do not need to build up the graph before using BFS: we can build the graph as
# we go: instead of storing the edges, we calculate the set of neighbors for the current node only when we need to
# visit them.
#
# Our get_neighbors function looks like this:
#
# from string import ascii_letters
# #
# def get_neighbors(word):
#     for i in range(len(word)):
#         # replace word[i] with every ascii letter
#         for c in ascii_letters:
#             next_word = word[:i] + c + word[i + 1:]
#             if in_wordlist(next_word):
#                 process(next_word)
