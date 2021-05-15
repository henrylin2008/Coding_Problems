# -Hashing: building a data structure that can be searched in 𝑂(1) time
# -A hash table is a collection of items which are stored in such a way as to make it easy to find them later. Each
# position of the hash table, often called a slot, can hold an item and is named by an integer value starting at 0.
# -The mapping between an item and the slot where that item belongs in the hash table is called the hash function. The
# hash function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1
#   * perfect hash function: a hash function that maps each item into a unique slot
# -Folding method: dividing the item into equal-size pieces (last piece may not be of equal size), then added these
# pieces together to give the resulting hash value.
#   * ex: 436-555-4601 --> 43+65+55+46+01 = 210 % 11 -> 1 (slot #)
# -Mid-square method: square the item, then extract some portion of the resulting digits
#   * ex: 44^2 = 1,936; extract middle 2 digits:93 => 93%11 = 5
#
hash_table = [None] * 11


def h(item):
    return item % 11


def put(item):
    hash_table[h(item)] = item


def contains(item):
    return hash_table[h(item)] == item


put(54)
put(26)
put(93)
put(17)
put(77)
put(31)

print(hash_table)

print("contains(22):", contains(22))
print("contains(17):", contains(17))


# -Hash of string data: each string has a Unicode value; use ord() function get the integer value of the string
#   * ex: ord('c') -> 99, ord('a') -> 87
def strToNum(s):
    strSum = 0
    for c in s:
        strSum += ord(c)
    return strSum


def h_str(s):   # add all the character numeric values up and modulo 11 to get the slot number
    strToNum(s) % 11


# any 2 strings with the same letters (anagram) will sum to the same number creating a collision, if you apply a weight
# to each letter this can be solved.
def strToWeightNum(s):
    strSum = 0
    for i in range(len(s)):
        sum += (i + 1) * ord(s[i])
    return strSum

# Collision & resolution: put 2 items in the same slot
# Collision Resolutions:
#   -Open Addressing types: (data in table)
#       * Linear probing
#           ** when inserting the item into the hash:
#               1. detect if an item is already in the slot
#               2. If yes, then find the  next slot to right that is empty and use it for  the  next  item
#           ** when checking if  the  item  is  in the hash
#               1. go to the slot for the hash function and check
#               2. if it is not in that slot, then check each slot to right, if a slot is empty return false, if a slot
#                  has the item then return true
#       * Rehashing
#       * Quadratic probing
#   -Chaining
