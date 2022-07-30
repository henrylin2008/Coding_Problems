# Word Break
# https://algo.monster/problems/word_break

# Given a string and a list of words, determine if the string can be constructed from concatenating words from the
# list of words. A word can be used multiple times.
#
# Input:
# s = "algomonster"
# words = ["algo", "monster"]
# Output: true
#
# Input:
# s = "aab"
# words = ["a", "c"]
# Output: false


# 1. Identify the states
# To determine whether we have completely constructed target s, we have to find
#      1. What are the characters left to be matched using words in the list.
# To make a choice when we visit the current node's children, we don't need any additional states since we can use
# any word in the list unlimited number of times.
#
# 2. Draw the space-state tree
#
# Note that in the above figure, there are two paths that lead to an empty string, i.e., completely matching the
# target. When we DFS we would reach the left one first without visiting the other one since we just need one
# successful path to return true.
#
# 3. DFS on the space-state tree
# Using the backtracking template as a basis, we add the state we identified in step 1:
#      1. We use index startIndex to record the current position in the target we have matched so far. s[:startIndex]
#      is matched and s[startIndex:] is to be matched.

def word_break(s, words):
    def dfs(start_index):
        if start_index == len(s):  # we have constructed the entire target s
            return True

        for word in words:
            if s[start_index:].startswith(word):  # is this a valid path
                if dfs(start_index + len(word)):
                    return True  # any path leads to true is fine

        return False

    return dfs(0)


# Memoization

# Everything looks great. When we finish typing that last bracket/semicolon, we can almost hear angels singing and
# all tests passing.
#
# Except there is one pesky test case:
#   1. "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#       aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
#   2. ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
#
# Why does this one time out? We have 10 branches to check each level of the tree and there are 140 as in the target,
# in the worse case we'd be looking at 10^140 branches. Remember we talked about "combinatorial explosion" in the
# backtracking module. We have just been struck by it. The way to solve this is to use memoization to cache the
# branches we have already seen. We can even see duplicates in the above example.
#
#
#
# Time Complexity: O(s * w * max(w[i]))
#
# s is the length of the string, w is the length of the words array and max(w[i]) is the maximal possible word
# length. Here our time complexity is polynomial since we memoize and we iterate through the possibilities. At every
# position s we try every word in w which takes time proportionate to the word length.

def word_break(s, words):
    memo = {}

    def dfs(start_index):
        if start_index == len(s):
            return True
        if start_index in memo:
            return memo[start_index]
        ok = False
        for word in words:
            if s[start_index:].startswith(word):
                if dfs(start_index + len(word)):
                    ok = True
                    break
        memo[start_index] = ok
        return ok

    return dfs(0)
