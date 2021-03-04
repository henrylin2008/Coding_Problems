# 11 essential Coding questions
# Write a function that returns True if one array is a notation of another
# ex: [1,2,3,4,5,6,7] is a notation of [4,5,6,7,1,2,3].
# Note: there are no duplicates in each of these arrays
# Reminder: We're going to use lists instead of arrays in Python for simplicity

# Run Time: O(n)
# Solution: check the length of both arrays first, if length are different, then return False; Next set a value from
# list1 (ex: 1st item) to be checked from list2, if same item found in list2, set the index from list2 as key_location;
# looping through the list, if no matching found on list2, return False; if matching is found on list2,
# check each item one by one until the last item in the list; at any moment if different item is found, return False;
# if reach the last item without False, then return True
def is_rotation(list1, list2):
    # if length of 2 lists don't match: return False
    if len(list1) != len(list2):
        return False

    key = list1[0]               # First element in list1
    key_loc = -1                 # index of same item (from list1) on list2
    for i in range(len(list2)):  # loop through list2
        if list2[i] == key:      # if same item found in list2
            key_loc = i          # put index on key_loc
            break
    if key_loc == -1:            # if not matching found on list2
        return False

    for i in range(len(list1)):  # loop through list1
        j = (key_loc + i) % len(list1)  # find index of same value (list1) on list2
        # ex: list1: [1,2,3,4,5,6,7]; list2: [4,5,6,7,1,2,3]
        # 5 in list1 (index: 4); (4 + 4) % 7 = 1 (index on list2)
        if list1[i] != list2[j]:  # if value of the indexes doesn't match
            return False
    # print("True")
    return True


# NOTE: The following input values will be used for testing your solution.
list1a = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.

is_rotation(list1a, list2f)
