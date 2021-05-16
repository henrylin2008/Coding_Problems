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


def h_str(s):  # add all the character numeric values up and modulo 11 to get the slot number
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
#       * Rehashing: go to a certain distance to the right (skip distance)
#           ** rehash(pos) = (pos + skip) % sizeOfTable
#       * Quadratic probing: add a constant to skip  every time
#           ** rehash(pos) = pos + skip, skip = i^2
#              ex: H, H+1^2, H+2^2, H+3^2, H+4^2, H+5^2 => h+0, h+1, h+4, h+9, h+16, h+25
#   -Chaining: create a list when insert a item; if conflict at the same slot, add the new item to the end of the list.
#       * Use single linked nodes to chain


# Implementing the Map Abstract Data type:
#   The structure is an unordered collection of associations between a key and a data value. The
#   keys in a map are all unique so that there is a one-to-one relationship between a key and a value. The operations
#   are given below.
#   * Map(): Create a new, empty map. It returns an empty map collection.
#   * put(key,val): Add a new key-value pair to the map. If the key is already in the map then replace the old value
#                   with the new value
#   * get(key): Given a key, return the value stored in the map or None otherwise
#   * del: Delete the key-value pair from the map using a statement of the form del map[key].
#   * len() Return the number of key-value pairs stored in the map.
#   * in: Return True for a statement of the form key in map, if the given key is in the map, False otherwise.
#   * [] operator will do get and put using __getitem__, and __putitem__
class HashTable:
    """Implement Hash table with 2 lists: one for keys, another one for its data value"""
    def __init__(self):
        """Initialize table size, two lists:one for key items, one for its data values"""
        self.size = 11
        self.slots = [None] * self.size  # hashtable
        self.data = [None] * self.size  # values

    def put(self, key, data):
        """assumes that there will eventually be an empty slot unless the key is already present in the self.slots."""
        hashValue = self.hashfunction(key, len(self.slots))

        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:  # non-empty slot
                self.data[hashValue] = data  # replace
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextSlot] is not None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data  # replace the data

    def hashFunction(self, key, size):
        """simple remainder method"""
        return key % size

    def rehash(self, oldHash, size):
        """linear probing with a plus 1 rehash function"""
        return (oldHash + 1) % size

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startSlot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# H=HashTable()
# H[54]="cat"
# H[26]="dog"
# H[93]="lion"
# H[17]="tiger"
# H[77]="bird"
# H[31]="cow"
# H[44]="goat"
# H[55]="pig"
# H[20]="chicken"
# H.slots
# [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
# H.data
# ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
# H[20]
# 'chicken'
# H[17]
# 'tiger'
# H[20]='duck'
# H[20]
# 'duck'
# H.data
# ['bird', 'goat', 'pig', 'duck', 'dog', 'lion',
#        'tiger', None, None, 'cow', 'cat']
# print(H[99])
# None
