# Construct Trie

# Method 1:
class Trie:
    def __init__(self):
        self.root = {"*": "*"}      # root is a dictionary

    def add_word(self, word):
        curr_node = self.root               # pointer at the root
        for letter in word:                 # iterate through each letter to be added
            if letter not in curr_node:
                curr_node[letter] = {}      # initiate a dictionary for letter not in current node
            curr_node = curr_node[letter]   # move the pointer down/next
        curr_node["*"] = "*"                # add "*" to the end of the word

    def does_word_exist(self, word):
        curr_node = self.root               # pointer at the root
        for letter in word:                 # check each letter
            if letter not in curr_node:     # if letter not in the current node children
                return False
            curr_node = curr_node[letter]   # move pointer down if letter in the current node
        return "*" in curr_node             # check if '*' at the end of the path
