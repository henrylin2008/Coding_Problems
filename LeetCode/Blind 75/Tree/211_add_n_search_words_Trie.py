# 211. Design Add and Search Words Data Structure
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 3 dots in word for search queries.
# At most 104 calls will be made to addWord and search.

# Note: if char = "." run search for remaining portion of word on all of curr nodes children;

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()     # insert a TrieNode
            curr_node = curr_node.children[letter]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):       # dfs calls on the children
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":            # when curren char is a "."
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # recursive calls on the children; input: starting index, current node
                            return True        # if one path matches
                    return False               # False if no match
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]      # shift pointer down
            return cur.end_of_word             # True if reach the end of the word
        return dfs(0, self.root)               # recursive calls, start index at 0, and the root node
