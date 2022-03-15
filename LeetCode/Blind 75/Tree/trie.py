# Construct Trie

# Method 1:
# class Trie:
#     def __init__(self):
#         self.root = {"*": "*"}      # root is a dictionary
#
#     def add_word(self, word):
#         curr_node = self.root               # pointer at the root
#         for letter in word:                 # iterate through each letter to be added
#             if letter not in curr_node:
#                 curr_node[letter] = {}      # initiate a dictionary for letter not in current node
#             curr_node = curr_node[letter]   # move the pointer down/next
#         curr_node["*"] = "*"                # add "*" to the end of the word
#
#     def does_word_exist(self, word):
#         curr_node = self.root               # pointer at the root
#         for letter in word:                 # check each letter
#             if letter not in curr_node:     # if letter not in the current node children
#                 return False
#             curr_node = curr_node[letter]   # move pointer down if letter in the current node
#         return "*" in curr_node             # check if '*' at the end of the path


# Method 2:
class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False  # condition to check if it's end of the word, instead of "*"


class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:                # if letter not in current node children
                curr_node.children[letter] = TrieNode(letter)   # add the letter to the children
            curr_node = curr_node.children[letter]              # move the pointer down/next
        curr_node.is_end_of_word = True                         # add the condition to the end of the word

    def does_word_exist(self, word):
        if word == "":          # True if string is empty
            return True
        curr_node = self.root   # current pointer
        for letter in word:
            if letter not in curr_node.children:     # False if the letter not in the children
                return False
            curr_node = curr_node.children[letter]   # move the pointer down/next
        return curr_node.is_end_of_word


# trie = Trie()
# words = ["wait", "waiter", "shop", "shopper"]
# for word in words:
#   trie.add_word(word)
#
# print(trie.does_word_exist("wait")) #True
# print(trie.does_word_exist("")) #True
# print(trie.does_word_exist("waite")) #False
# print(trie.does_word_exist("shop")) #True
# print(trie.does_word_exist("shoppp")) #False
