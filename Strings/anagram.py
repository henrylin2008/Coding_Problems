# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
# Check whether two strings are anagram of each other
# Last Updated: 27-12-2019
# Write a function to check whether two given strings are anagram of each other or not. An anagram of a string is another
# string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc”
# are anagram of each other.
#
# Method 1 (Use Sorting)
#
# Sort both strings
# Compare the sorted strings
# Time Complexity: O(nLogn)
def areAnagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)

    # If lenght of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 0

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0

    return 1


# Driver program to test the above function
str1 = "test"
str2 = "ttew"
if areAnagram(str1, str2):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")

# Output:
# The two strings are not anagram of each other


# Method 2 (Count characters)
# This method assumes that the set of possible characters in both strings is small. In the following implementation,
# it is assumed that the characters are stored using 8 bit and there can be 256 possible characters.

# 1. Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.
# 2. Iterate through every character of both strings and increment the count of character in the corresponding count arrays.
# 3. Compare count arrays. If both count arrays are same, then return true.

NO_OF_CHARS = 256

# Function to check whether two strings are anagram of
# each other
def areAnagram(str1, str2):
    # Create two count arrays and initialize all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS

    # For each character in input strings, increment count
    # in the corresponding count array
    for i in str1:
        count1[ord(i)] += 1

    for i in str2:
        count2[ord(i)] += 1

    # If both strings are of different length. Removing this
    # condition will make the program fail for strings like
    # "aaca" and "aca"
    if len(str1) != len(str2):
        return 0

    # Compare count arrays
    for i in xrange(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0

    return 1

# Driver program to test the above functions
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if areAnagram(str1, str2):
    print
    "The two strings are anagram of each other"
else:
    print
    "The two strings are not anagram of each other"

# Output:
# The two strings are anagram of each other
