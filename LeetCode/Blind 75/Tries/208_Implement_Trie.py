# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Category: Medium

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in
# a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
# otherwise.
#
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix
# prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.

# Note: node has children characters, and bool if its an ending character, node DOESN’T have or need char,
#       since root node doesn’t have a char, only children;

# Time: O(m); m: key length
# Space: O(1)
class TrieNode:
    def __init__(self):
        self.children = {}      # dict to store child node/s
        self.end_word = False   # mark for the node as the end of the word


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_word            # True if curr.end_word == True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:  # if character not in the tree, return False
                return False
            curr = curr.children[c]     # move the pointer to the child
        return True                     # no need to check end of word, since we only look for prefix
