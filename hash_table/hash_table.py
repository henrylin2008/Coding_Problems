# A hash table is a data structure that is used to store keys/value pairs. It uses a hash function to compute an index
# into an array in which an element will be inserted or searched. By using a good hash function, hashing can work well.

# Standard Implementation
# A more standard implementation of Hash Table with Python is presented below. We create three different functions to
# insert, search, and delete items from the hash table.
#
# Python’s built-in “hash” function is used to create a hash value of any key. This function is useful as it creates an
# integer hash value for both string and integer key. The hash value for integer will be same as it is, i.e. hash(10)
# will be 10, hash(20) will be 20, and so on.
#
# hash_key = hash('10')
# print (hash_key)  # Output: 6272037681056609
#
# hash_key = hash(10)
# print (hash_key)  # Output: 10
#
# hash_key = hash('10') % len(hash_table)
# print (hash_key) # Output: 9
#
# hash_key = hash(10) % len(hash_table)
# print (hash_key) # Output: 0

# Insert Data into the Hash Table
# While inserting a new element into the hash table, we first search if the key already exists in the hash table.
#
# - If the key is already present in the hash table, then we update its value with the new one.
# - Otherwise, we insert a new key-value pair into the hash table.


def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        bucket[i] = ((key, value))
    else:
        bucket.append((key, value))


insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)
# Output:
# [[(10, 'Nepal'), (20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]


# Search Data from the Hash Table

def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

# print (search(hash_table, 10))  # Output: Nepal
# print (search(hash_table, 20))  # Output: India
# print (search(hash_table, 30))  # Output: None


# Delete Data from the Hash Table
# While deleting any existing element from the hash table, we first search if the key already exists in the hash table.
#
# If the key is present (found) in the hash table, then we simply delete it. We delete that particular key-value pair
# from the hash table.
# Otherwise, no operation is done. We can simply print a message saying that the key was not found in the hash table.
def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))

#
# delete(hash_table, 100)
# print (hash_table)
# Output:
# Key 100 not found
# [[(10, 'Nepal'), (20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]
#
# delete(hash_table, 10)
# print (hash_table)
# Output:
# Key 10 deleted
# [[(20, 'India')], [], [], [], [], [(25, 'USA')], [], [], [], []]